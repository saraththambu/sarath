from django.shortcuts import render
from django.http import HttpResponse
from.models import Products

# Create your views here.
def home(request):
    products = Products.objects.all()
    return render(request,'home.html',{'products':products})
    #return HttpResponse("<h1>HI Friends</h1>")
def index(request):
    return HttpResponse("<h1>hello good morning</h1>")
