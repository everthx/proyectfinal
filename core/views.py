from django.shortcuts import render, HttpResponse


# Create your views here.

#def home(request):
#   return render( request, "core/home.html")

def bolsa(request):
    return render( request, "core/bolsa-de-trabajo.html")

def directorio(request):
    return render( request, "core/directorio.html")