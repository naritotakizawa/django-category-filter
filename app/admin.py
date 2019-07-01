from django.contrib import admin
from .models import Post, ParentCategory, Category

admin.site.register(Post)
admin.site.register(ParentCategory)
admin.site.register(Category)
