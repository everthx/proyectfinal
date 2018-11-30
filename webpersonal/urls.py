"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views #Importing the vews from our core APP
from Articulos import views as articulos_views 
from Trabajos import views as trabajos_views
#from Trabajos.views import PostListView

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', articulos_views.home, name = "home"),
    path('directorio/', core_views.directorio, name="directorio"),
    path('bolsa/', trabajos_views.bolsa, name="bolsa-de-trabajo"),
    #path('bolsa/', PostListView.as_view(), name="bolsa-de-trabajo"),
]


if settings.DEBUG:  # Displays media content from Dev site
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,  document_root= settings.MEDIA_ROOT)