from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'core/main_templates/index.html', { 'active_page': 'home' })

def dondeComprar(request):
    return render(request, 'core/main_templates/dondeComprar.html', { 'active_page': 'dondeComprar'})