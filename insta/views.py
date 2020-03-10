from django.shortcuts import render, redirect

# Create your views here.

## index page
def index(request):

    return render(request, "index.html")


## home page
def home_page(request):

    return render(request, "home.html")

