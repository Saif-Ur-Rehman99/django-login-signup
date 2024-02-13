from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'name':'saif',
        'designation':'software engineer',
        'message':'hi I am saif',
        'date_posted':'August 27, 2023'
    },
    {
        'name':'sami',
        'designation':'aircraft engineer',
        'message':'hi I am sami',
        'date_posted':'August 28, 2023'
    }
]

def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse('<h1> Blog Home </h1>')

def about(request):
    return render(request, 'blog/about.html')