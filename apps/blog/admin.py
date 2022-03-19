from django.contrib import admin
from .models import PostCategory, PostTag, Post

admin.site.register(PostCategory)
admin.site.register(PostTag)
admin.site.register(Post)
