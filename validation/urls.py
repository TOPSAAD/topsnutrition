from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.validate , name='validate'),
    path('saveInfos/', views.saveInfos , name='saveInfos'),
    path('thankyou', views.thankyou, name='thankyou'),
]