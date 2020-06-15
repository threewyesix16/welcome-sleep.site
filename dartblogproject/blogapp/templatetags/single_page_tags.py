from django import template

from blogapp.models import Post, Tag

register = template.Library()


@register.inclusion_tag('blogapp/popular_posts_tpl.html')
def show_popular_posts(count=3):
    posts = Post.objects.order_by('-views')[:count]
    return {'posts': posts}


@register.inclusion_tag('blogapp/tags_cloud_tpl.html')
def show_tags_cloud():
    tags = Tag.objects.order_by('?')
    return {"tags": tags}