from django.urls import path
from . import views

# urls.py
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('handle-register/', views.handle_register, name='handle_register'),
    path('handle-login/', views.handle_login, name='handle_login'),
    # ... otras urls
]

