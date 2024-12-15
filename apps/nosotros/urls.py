from django.urls import path
from . import views

urlpatterns = [
    path('nosotros', views.nosotros, name='nosotros'),
]
