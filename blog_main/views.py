
from django.shortcuts import render
from blogs.models import category, Blog

def home(request):
    categories = category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    unfeatured_post = Blog.objects.filter(is_featured=False, status='Published').order_by('-updated_at')
    print(unfeatured_post)
    context = {
        'categories': categories,
        'featured_post': featured_post,
        'unfeatured_post': unfeatured_post
    }
    return render(request, 'home.html', context)

