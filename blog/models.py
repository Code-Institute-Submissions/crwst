from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    blog_title = models.CharField(max_length=20)
    blog = models.TextField()

    def __str__(self):
        return f"Blog: {self.blog_title}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
             related_name="comments")
    comment_text = models.TextField()
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by: {self.author}"
