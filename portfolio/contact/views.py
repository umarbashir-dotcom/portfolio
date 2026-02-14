# contact/views.py
from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages

def contact_details(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message_text = request.POST.get('message')

        if name and email and message_text:
            ContactMessage.objects.create(
                name=name,
                subject = subject,
                email=email,
                message=message_text
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('index')  # redirect to homepage or wherever
        # else:
        #     messages.error(request, "Please fill all the fields!")

    # If GET request, optionally redirect or render a form
    return redirect('index')
