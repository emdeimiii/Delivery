from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def my_view(request):
    return JsonResponse({'message':'Helllo'})

def get_by_id(request, id: int):
    return JsonResponse({'data': id})

def hello(request, name: str):
    return HttpResponse({f'<h1>hello, {name}</h1>'})

def get_catalog(request):
    return render(request, 'catalogs/catlist.html' )