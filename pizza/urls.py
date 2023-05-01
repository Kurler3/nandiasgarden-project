

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="pizza.home"),
    path('order', views.order, name="pizza.order"),
]