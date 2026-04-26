# contact/views.py
from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages

def submit_contact_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if not name or not email or not message:
            messages.error(request, "Please fill all the fields!")
            return redirect("home:index")

        try:
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )

            messages.success(request, "Message sent successfully")

        except Exception:
            messages.error(request, "Something went wrong! Please try again.")

    return redirect("home:index")

