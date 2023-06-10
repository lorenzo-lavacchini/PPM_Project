
from django.shortcuts import render, HttpResponse
# Create your views here.

recipes=[
    {
    'author':'Dom',
    'title':'meatball sub',
    'directions':'combine all ingredients',
    'date_posted':'May 19, 2022'
    },
    {
    'author':'Dom',
    'title':'turkey sub',
    'directions':'combine all ingredients',
    'date_posted':'May 16, 2022'
    },
    {
    'author':'Dom',
    'title':'ham and cheese sub',
    'directions':'combine all ingredients',
    'date_posted':'May 19, 2022'
    },
]
def home(request):
    context ={
        'recipes':recipes
    }
    return render(request, "recipes/home.html", context)

def about(request):
    return render(request, "recipes/about.html", {'title':'about us page'})