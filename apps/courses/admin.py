from django.contrib import admin
from .models import Course, Lesson, Curriculum, Topic

# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Curriculum)
admin.site.register(Topic)
