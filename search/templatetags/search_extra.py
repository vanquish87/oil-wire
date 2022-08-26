from django import template

register = template.Library()

"""" This is used to because
by default in Django that you can't have a variable start with an underscore"""
@register.filter(name='get')
def get(d, k):
    return d.get(k, None)
    