from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return render(request,'recipes/pages/home.html',context ={})
# Create your views here.
