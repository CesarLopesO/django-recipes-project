from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return render(request,'home.html')
# Create your views here.
def contato(request):
    return HttpResponse('zecatatu')
def sobre(request):
    return HttpResponse('zecao')