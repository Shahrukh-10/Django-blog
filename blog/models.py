from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Content = models.TextField()
    Author = models.CharField(max_length=25)
    slug = models.CharField(max_length=130)
    ts = models.DateTimeField(blank=True,auto_now_add=True)

    def __str__(self):
        return self.Title


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment
