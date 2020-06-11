from django.shortcuts import render
from .models import Post


def main_page(request):
    posts = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts})


def post_detail(request, pip):
    post = Post.objects.get(pk=pip)
    return render(request, 'blog/post_detail.html', context={'post': post})


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', context={'posts': posts})
