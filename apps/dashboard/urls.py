from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.account, name='account'),
    path('account/admin/', views.account_admin, name='account-admin'),
    path('account/customer/', views.account_customer, name='account-customer'),
    path('modify-customer', views.editar_usuario, name='editar-usuario'),
    path('account/admin/search-customer/<str:pk>/', views.buscar, name='search-customer'),
    path('account/admin/delete-customer/<str:pk>/', views.delete, name='delete-customer'),
    path('account/customer/eliminar_causa/<int:pk>/', views.eliminar_causa, name='eliminar-causa'),
    path('account/admin/eliminar_causa/<int:pk>/', views.eliminar_causa_admin, name='eliminar-causa'),
    path('account/admin/editar_causa/<int:pk>/', views.editar_causa, name='editar-causa'),
    path('account/admin/agregar_caso/', views.agregar_caso, name='agregar_caso'),
    path('account/admin/eliminar_contrato/<int:pk>/', views.eliminar_contrato, name='eliminar-contrato'),
    path('account/admin/editar_contrato/<int:pk>/', views.editar_contrato, name='editar-contrato'),
    path('account/admin/casos/', views.listar_casos, name='listar_casos'),
    path('account/admin/contrato/crear/<int:caso_id>/', views.crear_contrato, name='crear_contrato'),
    path('account/customer/pagar-contrato/<int:contrato_id>/', views.pagar_contrato, name='pagar_contrato'),
]
