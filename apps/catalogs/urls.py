

from django.urls import path
from .views import get_by_id, get_catalog


urlpatterns = [
    path('', get_catalog),
    path('<int:id>', get_by_id )
]

