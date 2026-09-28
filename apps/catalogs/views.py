from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse


from .models import Dish

# Create your views here.

def get_by_id(request, id):
   # dish = Dish.objects.filter(pk=id.first())
    dish = get_object_or_404(Dish, pk=id)
    return render(
        request,
        'catalogs/dish_detail.html',
        {
        'dish' : dish,
        } )


def get_catalog(request):
    dishes = Dish.objects.all()
    content = {
        'dishes' : dishes
    }
    return render(request, 'catalogs/catlist.html' )