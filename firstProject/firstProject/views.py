from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello Django page")
    return render(request, "website/index.html")

def blogs(request):
    # return HttpResponse("Hello about page")
    return render(request, "website/blogs.html")

def contact(request):
    return HttpResponse("Hello contact page")