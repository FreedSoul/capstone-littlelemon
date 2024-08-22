#update URLConf by including URL patterns of restaurant app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
