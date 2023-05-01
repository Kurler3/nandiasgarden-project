

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="pizza.home"),
    path('order', views.order, name="pizza.order"),
    path('pizzas', views.pizzas, name="pizza.pizzas"),
    path('order/<int:pk>', views.edit_order, name='pizza.edit_order'),
]