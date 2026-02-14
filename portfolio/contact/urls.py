from django.urls import path
from .views import contact_details


app_name = 'contact'
urlpatterns = [
    path("submit/",contact_details,name="contact_details")
]
