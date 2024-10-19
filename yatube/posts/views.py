from django.shortcuts import render
def index(request):
    return render(request, 'posts/index.html')
def about(request):
    return render(request, 'posts/about.html')
def posts(request):
    return render(request, 'posts/posts.html')
def register(request):
    return render(request, 'posts/register.html')
def login(request):
    return render(request, 'posts/login.html')
