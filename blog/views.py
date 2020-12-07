from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': "test",
        'title': 'Post 1',
        'content' : 'First post Content',
        'date_posted':'Dec 7, 2020'
    },
    {
        'author': "test2",
        'title': 'Post 2',
        'content' : 'Second post Content',
        'date_posted':'Dec 6, 2020'
    },
]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')
