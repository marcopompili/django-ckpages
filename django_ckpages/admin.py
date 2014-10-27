"""
Created on 05/lug/2013

@author: Marco Pompili
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib import admin
from django.contrib.flatpages.models import FlatPage

from .models import CKPage
from .widgets import CkTextWidget


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
            'widget': CkTextWidget
        }
    }


admin.site.unregister(FlatPage)
admin.site.register(CKPage, CKPageAdmin)