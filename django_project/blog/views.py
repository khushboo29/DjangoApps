from django.shortcuts import render
import datetime
#from django.http import HttpResponse

posts =[
    {
        'author' : 'Corey MS',
        'title' : 'Blog Post 1',
        'date_posted' : datetime.date.today(),
        'content' : 'First Post content'
    },
     {
        'author' : 'Jane MS',
        'title' : 'Blog Post 2',
        'date_posted' : datetime.date.today(),
        'content' : 'Second Post content'
    },
]


def home(request):
    #return HttpResponse("<h1>Blog Home </h1>")
    context = {
        'posts': posts
    }
    return render(request,"blog/home.html",context)

def about(request):
    #return HttpResponse("<h1>Blog About</h1>")
    return render(request,"blog/about.html",{'title':'About'})