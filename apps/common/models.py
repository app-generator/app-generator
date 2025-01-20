from django.db import models
from autoslug import AutoSlugField

from .models_base           import *
from .models_authentication import *
from .models_blog           import *
from .models_deploy         import *
from .models_generator      import *
from .models_pages          import *
from .models_products       import *
from .models_tasks          import *
from .models_tools          import *
from .models_util           import *
from .models_ticket         import *

# No Models defined here       #
# each app will defined models #

class EventType(models.TextChoices):
    GENERAL      = 'GENERAL', 'General'
    ERR_500      = 'ERR_500', 'ERR_500'
    ERR_404      = 'ERR_404', 'ERR_404'
    ERR_403      = 'ERR_403', 'ERR_403'
    ERR_400      = 'ERR_400', 'ERR_400'
    API          = 'API'    , 'API'
    CSV_PROCESS  = 'CSV_PROCESS', 'CSV Processing'
    DB_MIGRATOR  = 'DB_MIGRATOR', 'DB Migrator'
    DB_PROCESSOR = 'DB_PROCESSOR', 'DB Processor'

class Event(BaseModel):
    userId = models.IntegerField(default=-1)
    type = models.CharField(max_length=100, choices=EventType.choices, default=EventType.GENERAL)
    text = models.TextField(null=True, blank=True)
    status_code = models.CharField(max_length=10, null=True, blank=True)
    input = models.JSONField(null=True, blank=True)
    output = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.userId}, {self.type} -> {self.text}"

class FileInfo(models.Model):
    path = models.URLField()
    info = models.CharField(max_length=255)

    def __str__(self):
        return self.path