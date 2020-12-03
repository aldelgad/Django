from django.contrib import admin
from factura.models import Factura, Linea_de_Factura

# Register your models here.

class FacturaAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'year',
        'emission_date',
        'customer_name',
        'customer_address',
    )
admin.site.register(Factura)

class Linea_de_FacturaAdmin(admin.ModelAdmin):
    list_display = (
        'id_line'
        'product_name',
        'facture_line',
        'unit_prize',
        'total_unit',
        'total_prize',
    )
admin.site.register(Linea_de_Factura)
