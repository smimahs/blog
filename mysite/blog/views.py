from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post

def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})


def post(request,slug):
    return render(None,'post.html', {'post':get_object_or_404(Post,slug=slug)})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})
# Create your views here.
