from django.shortcuts import render
from django.views import generic
from django.db.models import Count
from .models import Post


class About(generic.TemplateView):
    """About page render view"""
    template_name = 'blog/about.html'


class PostList(generic.ListView):
    """Main post feed view"""
    model = Post
    ordering = ['-created_on']
    paginate_by = 2
    queryset = Post.objects.annotate(number_of_comments=Count('comment'))


class PostDetail(generic.DetailView):
    """Main post detail view"""
    model = Post


class PostCreate(generic.CreateView):
    """View for creating post"""
    model = Post
    fields = ['title', 'excerpt', 'content', 'image']
