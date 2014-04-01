"""
Created on 05/lug/2013

@author: Marco Pompili
"""

from django.conf import settings
from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _

from django.contrib import admin
from django.contrib.flatpages.models import FlatPage

from .models import CKPage


CKEDITOR_VERSION = "4.3.2"


class CKPageAdmin(admin.ModelAdmin):
    """
        Admin interface with CKEditor support.
    """
    list_display = ('title', 'url', 'menu_weight')

    fieldsets = (
        (None, {'fields': ('title', 'url', 'menu_weight', 'content', 'sites')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )

    formfield_overrides = {
        models.TextField: {
            'widget': forms.Textarea(attrs={'class': 'ckeditor '})
        }
    }

    class Media:
        css = {
            'all': ('/static/django_ckpages/css/style.css',)
        }
        js = ('http://cdnjs.cloudflare.com/ajax/libs/ckeditor/' + CKEDITOR_VERSION + '/ckeditor.js',
              settings.CK_CONFIGURATION,)


admin.site.unregister(FlatPage)
admin.site.register(CKPage, CKPageAdmin)