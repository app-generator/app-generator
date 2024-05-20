from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class State(models.TextChoices):
    DRAFT = 'DRAFT', 'Draft'
    PENDING = 'PENDING', 'Pending'
    PUBLISHED = 'PUBLISHED', 'Published'


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

