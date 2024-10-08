#update URLConf by including URL patterns of restaurant app
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter() 
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path("menu/",views.MenuItemView.as_view()),
    path("menu/<int:pk>",views.SingleMenuItemView.as_view()),
    path("booking/",include(router.urls)),
]
