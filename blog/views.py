from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Blog, Comment

# Create your views here.


class HomePageView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blog'


class BlogCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Blog
    template_name = 'blog_add.html'
    fields = ['title', 'summary', 'body', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class BlogEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'blog_edit.html'
    fields = ['title', 'summary', 'body', 'image', 'author']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment.html'
    fields = ['comment']
    context_object_name = 'comment'

    def form_valid(self, form):
        id = self.kwargs['pk']
        form.instance.blog = Blog.objects.get(pk=id)
        form.instance.author = self.request.user
        return super().form_valid(form)
