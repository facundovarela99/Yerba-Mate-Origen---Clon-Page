from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from .forms import CustomAuthenticationForm, CustomUserCreationForm, UserProfileForm
from django.urls import reverse_lazy
from .forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'usuarios/registro.html'
    next_page = reverse_lazy('usuarios:miCuenta')

    def form_valid(self, form: CustomUserCreationForm) -> HttpResponse:
        return super().form_valid(form)
        
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'usuarios/miCuenta.html'
    next_page = reverse_lazy('usuarios:miCuenta')
    
    def form_valid(self, form: AuthenticationForm) -> HttpResponse: #Cuando el formulario sea valido
        return super().form_valid(form)
    
class UpdateProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'usuarios/perfil.html'
    success_url = reverse_lazy('usuarios:perfil')

    def get_object(self):
        #Devuelve el usuario actual en lugar de esperar un pk
        return self.request.user