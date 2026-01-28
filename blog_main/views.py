from django.http import HttpResponse
from django.shortcuts import render

from assignment.models import About
from blogs.models import Category, Blogs


def home(request):
    categories = Category.objects.all()
    featured_posts = Blogs.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blogs.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    #fetch about us

    try:
        about  = About.objects.get()
    except About.DoesNotExist:
        about = None
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }

    return render(request, 'home.html', context)


def register(request):
    return render(request, 'register.html')
