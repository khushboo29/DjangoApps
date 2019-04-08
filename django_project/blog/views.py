from django.shortcuts import render
from blog.models import Post
from django.contrib.auth.models import User

#from django.http import HttpResponse

def home(request):
    #return HttpResponse("<h1>Blog Home </h1>")
    context = {
        'posts': Post.objects.all()
    }
    return render(request,"blog/home.html",context)

def about(request):
    #return HttpResponse("<h1>Blog About</h1>")
    return render(request,"blog/about.html",{'title':'About'})
