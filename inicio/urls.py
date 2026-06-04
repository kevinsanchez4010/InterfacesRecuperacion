from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact, name='contact'),
    path('404/', views.error_404, name='error_404'),
    path('shop/', views.shop, name='shop'),
]