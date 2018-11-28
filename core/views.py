from django.shortcuts import render, HttpResponse


#NavBar test

NavBar_1 = """
<ul>
    <li><a href="/">Home</a></li>
    <li><a href="/directorio">Directorio</a></li>
    <li><a href="/bolsa/">Bolsa de Trabajo</a></li>
</ul>

"""
# Create your views here.

def home(request):
    return render( request, "core/home.html")

def bolsa(request):
    return render( request, "core/bolsa-de-trabajo.html")

def directorio(request):
    return render( request, "core/directorio.html")