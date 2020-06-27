from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import View, ListView
from .utils import *
from .forms import PostForm


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'
    # def get(self, request, pip):
    #     # post = Post.objects.get(pk=pip)
    #     post = get_object_or_404(Post, pk=pip)
    #     return render(request, 'blog/post_detail.html', context={'post': post})


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update.html'


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html'
    # def get(self, request):
    #     form = PostForm()
    #     return render(request, 'blog/post_create.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = PostForm(request.POST)
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request, 'blog/post_create.html', context={'form': bound_form})


class PostDelete(ObjectDeleteMixin, View):
    model_form = PostForm
    template = 'blog/post_delete.html'
    model = Post

class PostListView(ListView):
    template_name = 'blog/posts_list.html'
    queryset = Post.objects.all()


def home_page(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', context={'posts': posts})


def main_page(request):
    posts = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts})
