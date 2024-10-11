from distutils.command.register import register

from django.contrib import admin
from posts.models import post
# Register your models here.
admin.site.register(post)