from django.urls import path
from .views import submit_contact_form


app_name = 'contact'
urlpatterns = [
    path("submit/",submit_contact_form,name="submit_contact_form")
]
