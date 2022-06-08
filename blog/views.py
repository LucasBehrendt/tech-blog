from django.shortcuts import redirect
from django.views import generic
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
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
        try:
            form.instance.author = self.request.user
            return super().form_valid(form)
        except Exception:
            messages.warning(
                self.request, 'Please choose a valid image format!')
            return redirect('create_post')


class PostUpdate(LoginRequiredMixin,
                 UserPassesTestMixin,
                 SuccessMessageMixin,
                 generic.UpdateView):
    """View for updating post"""
    model = Post
    fields = ['title', 'excerpt', 'content', 'image']
    template_name = 'blog/update_post.html'
    success_message = 'You post was updated successfully!'
    success_url = '/post/{id}'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
