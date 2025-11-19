from django.shortcuts import render

# rendering index page
def index(request):
    return render(request, "home/index.html")

# rendering studies page
def studies(request):
    return render(request, "home/studies.html")

# rendering projects page
def projects(request):
    return render(request, "home/projects.html")