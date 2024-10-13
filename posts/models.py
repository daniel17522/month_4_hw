

from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rate =models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='posts')

class Category(models.Model):
    text = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='categories')

