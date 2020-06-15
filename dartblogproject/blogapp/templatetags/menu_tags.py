import random

from django import template
from django.db.models import Max

from blogapp.models import Category, Post

register = template.Library()


@register.simple_tag()
def get_random():
    max_id = Post.objects.all().aggregate(max_id=Max("id"))['max_id']
    pk = random.randint(1, max_id)
    return Post.objects.get(pk=pk)


@register.inclusion_tag('blogapp/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class, }

