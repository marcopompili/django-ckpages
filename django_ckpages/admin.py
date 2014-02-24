'''
Created on 05/lug/2013

@author: Marco Pompili
'''

from django.conf import settings
from django.db import models
from django import forms

from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
#from django.contrib.flatpages.admin import FlatPageAdmin

class CKPageAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            'widget' : forms.Textarea(attrs = { 'class' : 'ckeditor '})
        }
    }
    
    class Media:
        css = {
            'all' : ('/static/django_ckpages/css/style.css',)
        }
        js = ('http://cdnjs.cloudflare.com/ajax/libs/ckeditor/4.3.2/ckeditor.js',
              settings.CK_CONFIGURATION,)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CKPageAdmin)