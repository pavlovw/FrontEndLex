from django.urls import path
from . import views

urlpatterns = [
    path('ubicacion/', views.ubicacion, name='ubicacion'),

]
