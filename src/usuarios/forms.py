from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


def validar_nombre(nombre: str):
    if not nombre.isalpha():
        raise forms.ValidationError('Debe contener caracteres alfabeticos.')
    return nombre

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ['username', 'contrasenia']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2'] #campos pre-establecidos del UserCreationForm
        help_texts = {'username': ''}
    def __init__(self, *args, **kwargs: any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']