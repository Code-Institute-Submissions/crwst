from django import forms
from .models import Blog, Comment
from django.contrib.auth.models import User
from django.db import models


class CommentForm(forms.Form):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
             related_name="comments")
    comment_text = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return f"{self.comment_text} by {self.author}"


class SearchForm(forms.Form):
    title = forms.CharField(max_length=20)


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        blogs = Blog.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'
