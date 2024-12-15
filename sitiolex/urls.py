from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lex/account/', include('apps.account.urls')),
    path('contact/', include('apps.contact.urls')),
    path('lex/dashboard/', include('apps.dashboard.urls')),
    path('lex/home/', include('apps.home.urls')),
    path('lex/nosotros/', include('apps.nosotros.urls')),
    path('lex/services/', include('apps.services.urls')),
    path('lex/ubicacion/', include('apps.ubicacion.urls')),
    path('', include('apps.home.urls')), 
]

