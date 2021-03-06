from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post, Comment
from .forms import CommentForm


class About(generic.TemplateView):
    """View for rendering about page"""
    template_name = 'blog/about.html'


class PostList(generic.ListView):
    """
    Main post feed view, renders a list of all posts
    on the home page and paginates after five posts.
    """
    model = Post
    ordering = ['-created_on']
    paginate_by = 5


class PostDetail(generic.DetailView):
    """
    Main post detail view, renders a specific post,
    shows if the user has liked a post,
    renders and handles the comment form.
    """
    model = Post
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        post = self.get_object()
        if form.is_valid():
            form.instance.author = request.user
            form.instance.post = post
            form.save()
            messages.success(request, 'Comment created!')

            return redirect('post_detail', pk=post.id)
        else:
            messages.warning(
                request, 'Please write something in the comment field!')
            return redirect('post_detail', pk=post.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class

        post = self.get_object()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['liked'] = liked

        return context


class PostLike(generic.View):
    """
    View for handling likes on a post,
    adds or removes a user from the likes column on the post.
    """
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = self.request.user

        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)

        return redirect('post_detail', pk=post.id)


class PostCreate(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """
    View for creating posts, renders the form and defines the fields.
    Handles if a user uploads an invalid image format.
    """
    model = Post
    fields = ['title', 'excerpt', 'content', 'image']
    success_message = 'Your post was submitted successfully!'
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
    """
    View for updating posts, renders the form and defines the fields.
    Handles if a user uploads an invalid image format.
    Validates that the signed in user equals the request.user.
    """
    model = Post
    fields = ['title', 'excerpt', 'content', 'image']
    template_name = 'blog/update_post.html'
    success_message = 'Your post was updated successfully!'
    success_url = '/post/{id}'

    def form_valid(self, form):
        try:
            form.instance.author = self.request.user
            return super().form_valid(form)
        except Exception:
            messages.warning(
                self.request, 'Please choose a valid image format!')
            return redirect('update_post', pk=form.instance.pk)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDelete(LoginRequiredMixin,
                 UserPassesTestMixin,
                 generic.DeleteView):
    """
    View for deleting posts, validates that
    the signed in user equals the request.user.
    """
    model = Post
    success_message = 'Your post has been deleted!'
    success_url = '/'

    # Source: https://stackoverflow.com/questions/24822509/
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDelete, self).delete(request, *args, **kwargs)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class CommentDelete(LoginRequiredMixin, generic.View):
    """View for deleting comments"""
    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        post = comment.post.id
        comment.delete()
        messages.success(request, 'Your comment has been deleted!')

        return redirect('post_detail', pk=post)
