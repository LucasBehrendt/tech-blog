from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Count
from .models import Post


def about(request):
    """About page render view"""
    return render(request, 'blog/about.html')


class PostList(ListView):
    """Main post feed view"""
    model = Post
    ordering = ['-created_on']
    paginate_by = 2
    queryset = Post.objects.annotate(number_of_comments=Count('comment'))
