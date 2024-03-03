from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='esta_no_grupo')
def esta_no_grupo(user, group_name):
    return user.groups.filter(name=group_name).exists()
