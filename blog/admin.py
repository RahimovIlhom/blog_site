from django.contrib import admin
from .models import Blog, Comment

# Register your models here.


class CommentTabular(admin.TabularInline):
    model = Comment
    extra = 0


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    inlines = [CommentTabular]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
