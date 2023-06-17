from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.cart_detail , name='cart_detail'),
    path('add/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('change/<int:id><str:flavor>', views.ChangeQuantity, name='ChangeQuantity'),
    path('delete/<int:id><str:flavor>', views.delete, name='delete'),
    
    
    #path('remove/<int:product_id>', views.cart_remove, name='cart_remove'),

]