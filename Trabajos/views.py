from django.shortcuts import render
from .models import Trabajo

# Create your views here.

def bolsa(request):
    trabajos = Trabajo.objects.all()
    return render( request, "trabajos/bolsa-de-trabajo.html", { 'trabajos': trabajos})