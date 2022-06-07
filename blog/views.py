# from django.shortcuts import render
from django.views import generic
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post


class About(generic.TemplateView):
    """About page render view"""
    template_name = 'blog/about.html'


class PostList(generic.ListView):
    """Main post feed view"""
    model = Post
    ordering = ['-created_on']
    paginate_by = 5
    queryset = Post.objects.annotate(number_of_comments=Count('comment'))


class PostDetail(generic.DetailView):
    """Main post detail view"""
    model = Post


class PostCreate(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """View for creating post"""
    model = Post
    fields = ['title', 'excerpt', 'content', 'image']
    success_message = 'You post was submitted successfully!'
    success_url = '/post/{id}'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
