from django.urls import path

from . import views

urlpatterns = [
    path('<str:company>/', views.get_value_for, name='stock_value'),
]