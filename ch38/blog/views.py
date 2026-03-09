from django.shortcuts import render
from .form import PostForm
from .models import Post


# Create your views here.

def home(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'blog/home.html', {'form': form})

def about(request):
    return render(request, 'blog/about.html')

def profile(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'blog/profile.html', {'post': post})