
from django.urls import path
from . import views
app_name = 'orders'
urlpatterns = [
    path('create/', views.order_create_view, name='create'),
    path('<int:pk>/', views.order_detail_view, name='detail'),
    path('', views.order_list_view, name='list'),
]