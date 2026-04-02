from django.contrib import admin
from inicio.models import DepartamentosMedicos
# Register your models here.

admin.site.register(DepartamentosMedicos)

@admin.register(DepartamentosMedicos)
class DepartamentosMedicosaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "nro_departamento", "nro_medicos")
    
    list_display_links = ("nombre",)
    
    search_fields = ("nro_departamento", )
    
    list_filter = ("fecha", )
    
    ordering = ("nro_departamento", )
    
    readonly_fields = ("fecha", )
    
    