from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('mi-cuenta/', views.CustomRegisterView.as_view(), name='mi-cuenta'),
    path('mi-cuenta/', views.CustomLoginView.as_view(), name='mi-cuenta'),

]