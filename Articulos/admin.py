from django.contrib import admin
from .models import Articulo

# Register your models here.

# Class to display on the Admin Page the Created and Updated fields as ReadOnly
class ArticulosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# Registers the clases to the Admin page
admin.site.register(Articulo, ArticulosAdmin)

