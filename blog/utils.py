from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import PostForm
from blog.models import Post
from django.urls import reverse


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, pip):
        obj = get_object_or_404(self.model, pk=pip)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    form_model = None
    model = None
    template = None

    def get(self, request, pip):
        obj = self.model.objects.get(pk=pip)
        bound_form = self.form_model(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, pip):
        obj = get_object_or_404(self.model, pk=pip)
        bound_form = self.form_model(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})


class ObjectDeleteMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, pip):
        post = self.model.objects.get(pk=pip)
        return render(request, self.template, context={'post': post})

    def post(self, request, pip):
        post = self.model.objects.filter(pk=pip)
        post.delete()
        return redirect('posts_list_url')
