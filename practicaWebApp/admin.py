from django.contrib import admin
from .models import Familia, Ficha_tecnica, Categoria, Operario, Impresora, Parada, Cambio_Mecanico, Setup, Produccion, \
    Parte_Impresion

# Register your models here.

class CambioMecanicoAdmin(admin.ModelAdmin):
    fields = ['create', 'parada', 'fecha_fin']
    readonly_fields = ['create']

class SetupAdmin(admin.ModelAdmin):
    fields = ['create', 'parada', 'fecha_fin']
    readonly_fields = ['create']

class ProduccionAdmin(admin.ModelAdmin):
    fields = ['create', 'parada', 'fecha_fin']
    readonly_fields = ['create']

admin.site.register(Familia)

admin.site.register(Ficha_tecnica)

mis_modelos = Categoria, Operario
admin.site.register(Cambio_Mecanico, CambioMecanicoAdmin)
admin.site.register(Parada)
admin.site.register(mis_modelos)
admin.site.register(Impresora)
admin.site.register(Produccion, ProduccionAdmin)
admin.site.register(Parte_Impresion)
admin.site.register(Setup, SetupAdmin)