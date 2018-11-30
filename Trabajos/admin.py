from django.contrib import admin
from .models import Trabajo

# Register your models here.

# Class to display on the Admin Page the Created and Updated fields as ReadOnly
class TrabajosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# Registers the clases to the Admin page
admin.site.register(Trabajo, TrabajosAdmin)