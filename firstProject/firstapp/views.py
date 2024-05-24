from django.shortcuts import render
from .models import ChaiVariety

# Create your views here.
def topics(request):
    return render(request, "firstapp/topics.html")

def chais(request):
    all_chai = ChaiVariety.objects.all()
    return render(request, "firstapp/chais.html", { "chais": all_chai })



