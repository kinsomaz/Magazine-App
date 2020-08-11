from django import template


register = template.Library()

@register.filter
def shrink(value):
    return value[:300]

@register.filter
def capitalize(value):
    return value.capitalize()