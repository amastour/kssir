from django.db import models
import random
import string
from django.conf import settings

# Create your models here.

from .utils import *

SHORTCODE_MAX = getattr(settings,"SHORTCODE_MAX",15)

class KssirURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main  = super(KssirURLManager,self).all(*args,**kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=100):
        qs = KssirURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items,int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            print (q.shortcode)
            new_codes +=1
        return "New codes  made: {i}".format(i=new_codes)

class KssirURL(models.Model):
    url         = models.URLField(max_length=220,)
    shortcode   = models.URLField(max_length=SHORTCODE_MAX,unique=True,blank=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    active      = models.BooleanField(default=True)
    #empty_datetime = models.DateTimeField(auto_now=False,auto_now_add=False) 

    objects = KssirURLManager()
    #some_ramdom = KssirURLManager()

    def save(self, *args, **kwargs):
        print "generating"
        if self.shortcode  is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(KssirURL,self).save(*args,**kwargs)
    
    def __str__(self):
        return str(self.url)
    
    def __unicode__(self):
        return str(self.url)
    
    