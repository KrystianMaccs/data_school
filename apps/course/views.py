from django.shortcuts import render
from rest_framework import viewsets, permissions, validators, generics
from apps.common import permissions as custom_permissions
from apps.course.models import Course, Review
from apps.users.models import InstructorProfile
from django.contrib.auth import get_user_model
from apps.course.serializers import CourseSerializer, ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_auto_prefetching import AutoPrefetchViewSetMixin
from rest_framework.filters import OrderingFilter, SearchFilter
from apps.course.filters import CourseFilter
from apps.course.pagination import CustomPagination
from apps.course.renderers import CustomRenderer
from django.shortcuts import get_object_or_404
from django.db.models import Avg 
from django.db import IntegrityError

User = get_user_model()
# Create your views here.

class CourseViewSet(AutoPrefetchViewSetMixin,viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    search_fields = ["name", "instructor__user__first_name", "instructor__user__last_name"]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ["reviews", "price"]
    filterset_class = CourseFilter
    pagination_class = CustomPagination 
    renderer_classes = [CustomRenderer]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return super().get_queryset().filter(instructor__user__is_active=True)
    
    def get_permissions(self):
        
        if self.action == "create":
            self.permission_classes = [permissions.IsAuthenticated]  
        elif self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [custom_permissions.IsCreatorOrReadOnly]
        else:
            self.permission_classes = [permissions.AllowAny]
            
        return super().get_permissions()
    
    def perform_create(self, serializer):
        # Assign users with is_instructor field to create courses
        if not self.request.user.is_instructor:
            raise validators.ValidationError(
                                            {
                                            "detail": "User must have is_instructor = True to create a course"
                                            }
                                            )
        instructor_profile = InstructorProfile.objects.filter(user=self.request.user).first()
        serializer.save(instructor=instructor_profile) 

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    pagination_class = CustomPagination 
    renderer_classes = [CustomRenderer]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Review.objects.all()
    
    def perform_create(self, serializer):
        
        try:
            course_identity = self.kwargs["pk"]
            course = get_object_or_404(Course, id=course_identity)
            serializer.save(course=course, user=self.request.user)
        except IntegrityError:
            raise validators.ValidationError(
                                            {
                                            "detail": "This user has already created a review about this course"
                                            }
                                            )
        else:
            course.reviews += 1
            average = Review.objects.filter(course=course).aggregate(Avg("rating"))
            course.average_rating = average["rating__avg"]
            course.save()
            
            
class ReviewListView(AutoPrefetchViewSetMixin, generics.ListAPIView):
    serializer_class = ReviewSerializer 
    pagination_class = CustomPagination 
    renderer_classes = [CustomRenderer]
    queryset = Review.objects.all()
    permission_classes = [custom_permissions.IsCreatorOrReadOnly]
    
    def get_queryset(self):
        pk = self.kwargs["pk"]
        return super().get_queryset().filter(user__is_active=True, course__id=pk)
    
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer 
    renderer_classes = [CustomRenderer]
    permission_classes = [custom_permissions.IsCreatorOrReadOnly]
    
    def get_object(self):
        pk = self.kwargs["pk"]
        obj = get_object_or_404(Review, id=pk)
        self.check_object_permissions(self.request, obj)
        return obj 
    
    def perform_update(self, serializer):
        pass
    
    
    