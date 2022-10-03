from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return render(request,'recipes/home.html',context ={ 'name':'Luiz Otavio'})
# Create your views here.
def contato(request):
    return HttpResponse('zecatatu')
def sobre(request):
    return HttpResponse('zecao')