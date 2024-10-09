from django.db import models
from django.contrib.auth.models import User
from apps.common.models import Products
from django_quill.fields import QuillField

# Create your models here.

class TypeChoices(models.TextChoices):
    PRODUCT_ASSISTANCE = 'PRODUCT_ASSISTANCE', 'Product Assistance'
    PLATFORM = 'PLATFORM', 'Platform'
    SUGGESTED_FEATURE = 'SUGGESTED_FEATURE', 'Suggested Feature'

class PlatformChoices(models.TextChoices):
    PURCHASES = 'PURCHASES', 'Purchases'
    AUTHENTICATION = 'AUTHENTICATION', 'Authentication'

class StateChoices(models.TextChoices):
    OPEN = 'OPEN', 'Open'
    ANSWERED = 'ANSWERED', 'Answered'
    CLOSED = 'CLOSED', 'Closed'

class PriorityChoices(models.TextChoices):
    LOW = 'LOW', 'Low'
    HIGH = 'HIGH', 'High'

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    guest_email = models.EmailField(null=True, blank=True)
    type = models.CharField(max_length=100, choices=TypeChoices.choices, default=TypeChoices.PRODUCT_ASSISTANCE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    platform = models.CharField(max_length=100, choices=PlatformChoices.choices, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = QuillField()
    states = models.CharField(max_length=50, choices=StateChoices.choices, default=StateChoices.OPEN)
    priority = models.CharField(max_length=50, choices=PriorityChoices.choices, default=PriorityChoices.LOW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = QuillField()
    created_at = models.DateTimeField(auto_now_add=True)