from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'text', 'title']

        # widgets = {
            # 'title': forms.TextInput(atters={'class':'form-control'}),
            # 'text': forms.TextInput(atters={'class': 'form-control'}),
            # 'author': forms.TextInput(atters={'class': 'form-control'})
        # }
    # def clean_data(self):
