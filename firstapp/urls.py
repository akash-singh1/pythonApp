from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('ajax/validate_name/', views.validate_name, name='validate_name'),
]