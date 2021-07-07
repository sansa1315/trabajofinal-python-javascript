from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('login', views.login, name="login"),
    path('logoutUser', views.logoutUser, name="logout"),
    path('registro', views.registro, name="registro"),
    path('carrito', views.carrito, name="carrito"),
    path('productoCrud', views.productoCrud, name="productoCrud"),
    path('productoEdit/<str:pk>', views.productoEdit, name="productoEdit"),
    path('productoEdit', views.productoEdit, name="productoEdit"),
    path('productoFind/<str:catg>', views.productoFind, name="productoFind"),
    path('productoFind', views.productoFind, name="productoFind"),
    path('productoDetalle/<str:pk>', views.productoDetalle, name="productoDetalle"),
    path('carrito/<str:pk>', views.carrito, name="carrito"),
    path('acercaDe', views.acercaDe, name="acercaDe"),
    path('carritoDel/<str:pk>', views.carritoDel, name="carritoDel"),
    path('contacto', views.contacto, name="contacto"),

]