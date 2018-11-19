from django.template import Library
from django.utils.formats import localize

register = Library()

@register.simple_tag
def multiply(quantity, price, *args, **kwargs):
    return localize(quantity * price)