from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ("is_familiar", "is_learned", "student")

admin.site.register(Student, StudentAdmin)

