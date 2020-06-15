from django.urls import path, include

from .views import *


urlpatterns = [
    path(route='', view=HomePage.as_view(), name='home'),
    path(route='category/<str:slug>/', view=CategoryPage.as_view(), name='category'),
    path(route='post/<str:slug>/', view=PostPage.as_view(), name='post'),
    path(route='post/<str:slug>/comment_create/', view=comment_create, name='comment_create'),
    path(route='tag/<str:slug>/', view=TagPage.as_view(), name='tag'),
    path(route='search/', view=SearchPage.as_view(), name='search'),
]