from django.http import HttpResponse
from django.shortcuts import render, redirect
from assignment.models import About
from blogs.models import Category, Blogs
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


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

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

def logout(request):
    return render(request, 'logout.html')



