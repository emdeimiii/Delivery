from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('', views.cart_detail_view, name='detail'),
    path('add/<int:dish_id>/', views.add_to_cart_view, name='add'),
]