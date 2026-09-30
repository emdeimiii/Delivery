

from django.urls import path
from .views import get_by_id, get_catalog


app_name = 'catalogs'

urlpatterns = [
    path('', get_catalog, name='dish_list'),
    path('<int:id>', get_by_id )
    
]

