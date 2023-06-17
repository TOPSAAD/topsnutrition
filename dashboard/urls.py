from django import views
from django.urls import path
from . import views
urlpatterns = [
   path('', views.isLogged , name="isLogged"),
   path('panel', views.dashboard, name="dashboard"),
   path('order/<str:id>', views.order_details, name="order_details")
]
