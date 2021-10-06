from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    allequipo = Equipo.objects.all()
    return render(request, 'index.html', {'allequipo':allequipo})