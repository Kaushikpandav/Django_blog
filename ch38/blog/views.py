from django.shortcuts import render
from .form import PostForm
from .models import Post
from django.contrib import messages


# Create your views here.

def home(request):

    messages.add_message(request, messages.SUCCESS,'This is a success message')
    messages.add_message(request, messages.INFO,'This is an info message')
    messages.add_message(request, messages.WARNING,'This is a warning message')
    messages.add_message(request, messages.ERROR,'This is an error message')

    messages.success(request, 'This is a success message')
    messages.info(request, 'This is an info message')
    messages.warning(request, 'This is a warning message')
    messages.error(request, 'This is an error message')

    # to print aor display
    print(messages.get_level(request))
    print(messages.set_level(request, messages.DEBUG))

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