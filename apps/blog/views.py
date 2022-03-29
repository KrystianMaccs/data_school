from django.shortcuts import render
from rest_framework import generics
from apps.blog.models import Post, PostTag, PostCategory
from .serializers import PostSerializer, PostCategorySerializer, PostTagSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostSerializer

    
class PostCategoryList(generics.ListAPIView):
    serializer_class = PostCategorySerializer
    
class PostCategoryDetail(geneircs.RetrieveAPIView):
    queryset = PostCategory.objects.get()
    serializer_class = PostCategorySerializer
    
    
class PostTagList(generics.ListAPIView):
    queryset = PostTag.objects.all()
    serializer_class = PostTagSerializer
    
class PostTagDetail(generics.RetrieveAPIView):
    queryset = PostTag.objects.get()
    serializer_class = PostTagSerializer

class PostCreate(LoginRequiredMixin,generics.CreateAPIView):
    model = Post
    fields = ['title', 'content', 'category', 'tag']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

