
import os, json  
from apps.common.models import Event, EventType

'''
class Event(BaseModel):
    userId = models.IntegerField(default=-1)
    type = models.CharField(max_length=100, choices=EventType.choices, default=EventType.GENERAL)
    text = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.userId}, {self.type} -> {self.text}"
'''

def event_create(aRequest, aType, aText):
    
    userId = -1
    text   = str( aText )[:510] 

    if aRequest.user.is_authenticated:
        userId = aRequest.user.id

    event = Event(userId=userId, type=aType, text=text)
    event.save()

    return event

def event_404(aRequest, aText):

    return event_create(aRequest, EventType.ERR_404, aText)

def event_500(aRequest, aText):

    return event_create(aRequest, EventType.ERR_500, aText)

def event_403(aRequest, aText):

    return event_create(aRequest, EventType.ERR_403, aText)
