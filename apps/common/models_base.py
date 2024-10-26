from django.db import models

# Create your models here.

import json
from django.core import serializers
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    class Meta:
        abstract = True

    def to_json(self):
        return json.loads( serializers.serialize('json', [ self, ]) )[0]
