from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.services, name='services'),
    path('complete/', views.services_complete, name='services_complete'),
    path('solicitar-servicio/', views.solicitar_servicio, name='solicitar_servicio'),
]

