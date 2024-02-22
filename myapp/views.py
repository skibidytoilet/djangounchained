from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'aboutus.html')

def contact(request):
    return render(request,'contact.html')

def home(request):
    return render(request,'home.html')

def gallery(request):
    return render(request,'gallery.html')

 # Create your views here.
