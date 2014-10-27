__author__ = 'Marco Pompili'

from django.conf import settings
from django import forms

CKEDITOR_VERSION = '4.3.2'


class CkTextWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        return super(CkTextWidget, self).render(name, value, {'class': 'ckeditor'})

    class Media:
        css = {
            'all': ('/static/django_ckpages/css/style.css',)
        }
        js = ('http://cdnjs.cloudflare.com/ajax/libs/ckeditor/' + CKEDITOR_VERSION + '/ckeditor.js',
              settings.CK_CONFIGURATION,)