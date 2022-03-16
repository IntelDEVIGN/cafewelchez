from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from menu.views import indice

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('menu.urls')),
    path('login/', auth_views.LoginView.as_view(), name='iniciar'),
    path('logout/', auth_views.LogoutView.as_view(), name='salir'),
    path('', indice, name='home'),
]
