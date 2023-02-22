from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
posts =[
       {
           "name": "post1" 
        },
        {
            "name": "post2"
        }
    
]

def home(request):
    context={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
