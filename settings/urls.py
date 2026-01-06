from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('details/<int:product_id>/', views.product_detail, name='details'),
    path('checkout/<int:product_id>/', views.checkout, name='checkout'),
]