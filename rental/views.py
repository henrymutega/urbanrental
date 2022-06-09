from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Properties, Blog, About
import datetime as dt


def home(request):
    property = Properties.property_details()
    blog = Blog.blog_details()
    return render(request, 'index.html', {"property":property, "blog":blog})

def blog(request):
    blog = Blog.blog_details()
    return render(request, 'blog-grid.html', {"blog":blog})

def blogsingle(request, blog_id):
    blogsingle = Blog.objects.get(id=blog_id)
    return render(request, 'blogsingle.html', {"blogsingle":blogsingle})

def contact(request):
    return render(request, 'contact.html')

def property(request):
    property = Properties.property_details()
    return render(request, 'property-grid.html', {"property":property})

def about(request):
    about = About.about_details()
    return render(request, 'about.html', {"about": about})

def service(request):
    return render(request, 'service.html')