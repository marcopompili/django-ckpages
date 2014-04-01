"""
Created on 05/lug/2013

@author: Marco Pompili
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.flatpages.models import FlatPage


class CKPage(FlatPage):
    menu_weight = models.IntegerField(_(u"Menu weight"), blank=True, null=True,
                                      help_text=_(u"Set the page order in a menu or list."))