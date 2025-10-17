from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.CustomRegisterView.as_view(), name='registro'),
    path('mi-cuenta/', views.CustomLoginView.as_view(), name='mi-cuenta'),
    path('mi-cuenta/edit-account/', views.UpdateProfileView.as_view(), name='perfil'),
    path('mi-cuenta/menu/', views.mi_cuenta_menu, name='mi-cuenta-menu'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
]