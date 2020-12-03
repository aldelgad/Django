from django.shortcuts import render
from factura.models import Factura, Linea_de_Factura

#Create your views here:

def factura(request, num):
    return render(request, 'factura.html', {
    'total': Factura.objects.get(pk=num),
    })

def facturas(request):
    total = 0

    for b in Linea_de_Factura.objects.all():
        a = b.prize()
        total = total + a

    return render(request, 'linea.html',{
    'fact_rest' : Factura.objects.order_by('num').all(),
    })
