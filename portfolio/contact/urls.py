from django.urls import path
from .views import contact_details

urlpatterns = [
    path("submit/",contact_details,name="contact_details")
]
