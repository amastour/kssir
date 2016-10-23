from django.db import models

# Create your models here.
from shoortner.models import KssirURL

class ClickEventManager(models.Manager):
    def create_event(self ,KssirInstance):
        if isinstance(KssirInstance,KssirURL):
            obj,created = self.get_or_create(url=KssirInstance)
            obj.count +=1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    url         = models.OneToOneField(KssirURL)
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    
    objects = ClickEventManager()
    
    def __str__(self):
        return "{}".format(self.count)
    def __unicode__(self):
        return "{}".format(self.count)