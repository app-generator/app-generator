from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from apps.common.models import Tag
User = settings.AUTH_USER_MODEL
# Create your models here.




class ChatThread(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

class ChatMessage(models.Model):
    thread = models.ForeignKey(ChatThread, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(blank=True, null=True)
    public = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        if self.pk and self.message:
            self.slug = f"{slugify(self.message)}-{self.pk}"
        super(ChatMessage, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return self.slug
    


class AnonymousChatIP(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    questions_asked = models.IntegerField(default=0)
    last_question_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ip_address
    