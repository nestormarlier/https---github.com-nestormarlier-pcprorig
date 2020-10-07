from django.http import HttpResponse
from django.shortcuts import render
from .models import Categoria, Familia, Parada, Ficha_tecnica, Impresora, Parte_Impresion
from django.views.generic.list import ListView

# Create your views here.


def miPrimera(request):
    data = {
        'title': 'Listado de categorías',
        'categorias': Categoria.objects.all()
    }
    return render(request, 'xFuncion/categorias/list.html', data)

def miSegundaPag(request):
    data = {
        'title': 'Listado de familias',
        'familias': Familia.objects.all()
    }
    return render(request, 'xFuncion/familia/list.html', data)

def miTerceraPag(request):
    data = {
        'title': 'Listado de paradas',
        'paradas': Parada.objects.all()
    }
    return render(request, 'xFuncion/paradas/list.html', data)

def miCuartaPag(request):
    data = {
        'title' : 'Fichas técnicas',
        'fichastecnicas' : Ficha_tecnica.objects.all()
    }
    return render(request,'xFuncion/fichastecnicas/list.html', data)

def miQuintaPag(request):
    data = {
        'title' : 'Listado de impresoras',
        'impresoras' : Impresora.objects.all()
    }
    return render(request,'xFuncion/impresoras/list.html', data)

def miSextaPag(request):
    data = {
        'title' : 'Listado de partes de impresión',
        'partes': Parte_Impresion.objects.all()
    }
    return render(request,'xFuncion/partes/list.html',data)

class Ficha_TecnicaListView(ListView):
    model = Ficha_tecnica
    template_name = "xClases/fichastecnicas/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Fichas técnicas'
        return context

class CategoriaListView(ListView):
    model = Categoria
    template_name = "xClases/categorias/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de categorías'
        #context['object_list'] = Familia.objects.all() Puedo pasar al contexto el objeto que quiero mostrar
        return context

class CategoriaDataTableListView(ListView):
    model = Categoria
    template_name = "datatables/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de categorías'
        #context['object_list'] = Familia.objects.all() Puedo pasar al contexto el objeto que quiero mostrar
        return context

class FamiliaListView(ListView):
    model = Familia
    template_name = "xClases/familia/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado familia'
        return context

class ParadaListView(ListView):
    model = Parada
    template_name = 'xClases/paradas/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de paradas'
        #context['object_list'] = Familia.objects.all() Puedo pasar al contexto el objeto que quiero mostrar
        return context

    def get_queryset(self):
        #return Parada.objects.filter(nombre__startswith='L')
        return Parada.objects.all()

class ImpresoraListView(ListView):
    model = Impresora
    template_name = "xClases/impresoras/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de impresoras' 
        return context
