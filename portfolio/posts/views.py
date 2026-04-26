from django.shortcuts import render
from .models import Post

# Create your views here.
def get_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/posts.html', {'posts' : posts})