from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# -------------------------------------
class ResourceEquipo(resources.ModelResource):
    class Meta:
        model = Equipo

class AdminEquipo(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre_equipo']
    list_display = ['pk_equipo', 'codigo', 'nombre_equipo', 'descripcion', 'precio']
    resource_class = ResourceEquipo

admin.site.register(Equipo, AdminEquipo)



class ResourceEmpleado(resources.ModelResource):
    class Meta:
        model = empleado

class AdminEmpleado(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['dpi']
    list_display = ['pk_cliente', 'nombre', 'apellido', 'dpi', 'telefono']
    resource_class = ResourceEquipo

admin.site.register(empleado, AdminEmpleado)