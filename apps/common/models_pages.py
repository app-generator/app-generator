from django.db import models

from .models_base import *

# Create your models here.


class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    mailchimp = models.BooleanField(default=False)
    subscribed_at = models.DateTimeField(auto_now_add=True)


class Prompt(models.Model):
    user_id = models.CharField(max_length=10)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)