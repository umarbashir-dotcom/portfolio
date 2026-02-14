from django.urls import path
from .views import index,studies,projects



urlpatterns = [
    path('',index, name='index'),
    path('studies/',studies, name="studies"),
    path('projects/',projects, name="projects")

]

