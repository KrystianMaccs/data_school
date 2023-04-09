from django.contrib import admin
from .models import Course, Review
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name",  "difficulty", "is_available")
    list_filter = ( "difficulty", "is_available", "is_certified")
    search_fields = ( "name",)
    
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "course")
    list_filter = ("user", "course")
    