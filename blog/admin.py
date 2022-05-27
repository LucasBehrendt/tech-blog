from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post table on admin page"""
    list_filter = ('created_on',)
    list_display = ('author', 'title', 'excerpt', 'created_on')
    search_fields = ['title', 'excerpt', 'author__username']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment table on admin page"""
    list_filter = ('created_on',)
    list_display = ('author', 'body', 'post', 'created_on')
    search_fields = ['author__username', 'body']
