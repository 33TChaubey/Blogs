from django.http import HttpResponse
from django.shortcuts import render, redirect
from assignment.models import About
from blogs.models import Category, Blogs
from .forms import RegisterForm


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
    if request.method == 'POST':
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('register')
    else:
        forms = RegisterForm()

    context = {
        'forms': forms,
    }
    return render(request, 'register.html', context)



