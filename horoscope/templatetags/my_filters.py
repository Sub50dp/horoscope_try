from django import template

register = template.Library()

@register.filter(name="get_key")
def get_key(value, key):
    return value[key]
