from django import template

register = template.Library()

@register.simple_tag
def idx(a, b):
    return a*9 + b