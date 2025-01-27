from django.db import models

from .models_base import *

# Create your models here.

class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    mailchimp = models.BooleanField(default=False)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"mail={self.email}, is_subscribed={self.mailchimp}"

class Prompt(models.Model):
    user_id = models.IntegerField(null=True, blank=True, default=-1)
    question = models.TextField()
    response = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"user={self.user_id}, question={self.question}"

class ProjectTypeChoices(models.TextChoices):
    CUSTOM_SOFTWARE_DEVELOPMENT = 'CUSTOM_SOFTWARE_DEVELOPMENT', 'Custom Development'
    SERVICE_OPTIMIZATION = 'TOOLS_RESEARCH', 'DevTools & Research'
    CLOUDE_DEPLOYMENT = 'DEPLOYMENT', 'Deployment (Digital Ocean, AWS, Azure)'

class BudgetRangeChoices(models.TextChoices):
    UNDER_5k = 'UNDER_5k', 'Under $5,000'
    F5K_T10k = 'F5K_T10k', '$5,000 - $10,000'
    OVER_10k = 'OVER_10k', 'Over $10,000'

class CustomDevelopment(BaseModel):
    project_type = models.CharField(max_length=255, choices=ProjectTypeChoices.choices)
    budget_range = models.CharField(max_length=100, choices=BudgetRangeChoices.choices)
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"email={self.email}, project_type={self.project_type}, budget_range={self.budget_range}"    