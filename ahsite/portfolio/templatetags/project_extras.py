from django import template

register = template.Library()

@register.filter(name='strip')
def strip(value):
    return value.replace(' ', '')