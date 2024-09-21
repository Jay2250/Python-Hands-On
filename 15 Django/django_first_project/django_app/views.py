from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse("Hii I am HA.VI.BA ")
    return render(request,'home.html')

def about(request):
    # return HttpResponse("I am a web developer and designer")  #new Screen
    return render(request,'about.html') 