from django.shortcuts import render, redirect
from posts.models import Post

def index(request):
    data = Post.objects.prefetch_related("category").select_related("author")
    return render(request, 'index.html', {'data': data})