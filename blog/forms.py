from django import forms
from django.contrib.auth.models import User
from django.db import models


class CommentForm(forms.Form):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name="comments")
    comment_text = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return f"{self.comment_text} by {self.author.username}"


class SearchForm(forms.Form):
    title = forms.CharField(max_length=20)
