from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name="hello"),
    path('add/', views.add, name="add"),
]