from distutils.command.register import register

from django.contrib import admin
from posts.models import Post
# Register your models here.
admin.site.register(Post)