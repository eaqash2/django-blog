from django.shortcuts import render
from django.views.generic import ListView
from post.models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

from django.views.generic import DetailView
from post.models import Post

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    all_posts = Post.objects.all()

