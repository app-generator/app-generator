
from django.db import models
from django.contrib.auth import get_user_model

from autoslug import AutoSlugField
from django_quill.fields import QuillField

from django.utils import crypto

class State(models.TextChoices):
    DRAFT = 'DRAFT', 'Draft'
    PENDING = 'PENDING', 'Pending'
    PUBLISHED = 'PUBLISHED', 'Published'


class FileType(models.TextChoices):
    VIDEO = 'video', 'video'
    PDF = 'pdf', 'pdf'
    IMAGE = 'image', 'image'
    OTHER = 'other', 'other'

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

def get_thumbnail_filename(instance, filename):
    ext = filename.split('.')[-1]
    return f"articles/thumbnail_{crypto.get_random_string(7)}.{ext}"

class File(models.Model):
    file = models.FileField(upload_to=get_thumbnail_filename, blank=True)
    url = models.URLField(blank=True)
    type = models.CharField(max_length=10, choices=FileType.choices, default=FileType.OTHER)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    
class Article(models.Model):
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    state = models.CharField(max_length=10, choices=State.choices, default=State.DRAFT)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    thumbnail = models.OneToOneField(File, related_name='+', on_delete=models.SET_NULL, null=True, blank=True)
    video = models.OneToOneField(File, related_name='+', on_delete=models.SET_NULL, null=True, blank=True)
    content = QuillField()
    tags = models.ManyToManyField(Tag, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
    

class Bookmark(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('article', 'user')
    
    def __str__(self):
        return self.article.title