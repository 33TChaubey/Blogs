from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from .models import Blogs, Category


# Create your views here.
def posts_by_category(request, category_id):
    #fetch the post that belongs to the category with the id
    posts = Blogs.objects.filter(status = 'Published',category=category_id)
    try:
        category = Category.objects.get(id=category_id)
    except:
        return redirect('home')

    context = {'posts': posts, 'category': category}
    return render(request, 'posts_by_category.html', context)