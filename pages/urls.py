from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('product/<int:id>', views.product, name='product'),
    path('contact', views.contact, name='contact')
]
