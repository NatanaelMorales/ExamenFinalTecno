from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    allproduct = Equipo.objects.all()
    return render(request, 'index.html', {'allproduct':allproduct})