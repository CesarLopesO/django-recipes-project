from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return render(request,'recipes/home.html',context ={ 'name':'tilesburguer'})
# Create your views here.
