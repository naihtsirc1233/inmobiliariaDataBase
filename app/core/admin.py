from django.contrib import admin
from core.models import *


# Register your models here.


class BuscadorFiltros(admin.ModelAdmin):
    List_display = ['name', 'telefono1']
    search_fields = ['name', 'telefono1']
    List_filter = ['name']


admin.site.register(Inmueble)
admin.site.register(Persons,BuscadorFiltros)
