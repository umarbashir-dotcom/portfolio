from django.urls import path
from .views import get_posts

app_name = "posts"
urlpatterns = [
    path('',get_posts,name='get_posts')
]
