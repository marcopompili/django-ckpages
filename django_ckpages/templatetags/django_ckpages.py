__author__ = 'Marco Pompili'


from django import template
from django.conf import settings


register = template.Library()

@register.inclusion_tag('ck_configuration.html')
def ck_configuration():
    return {
        'ck_configuration': settings.CK_CONFIGURATION
    }