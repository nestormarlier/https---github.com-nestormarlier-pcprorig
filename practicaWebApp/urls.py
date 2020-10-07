from django.urls import path
from .views import *

urlpatterns = [
    path('xfuncion/primera/', miPrimera, name="Primera"),
    path('xfuncion/segunda/', miSegundaPag, name="Segunda"),
    path('xfuncion/tercera/', miTerceraPag, name="Tercera"),
    path('xfuncion/cuarta/', miCuartaPag, name="Cuarta"),
    path('xfuncion/quinta/', miQuintaPag, name="Quinta"),
    path('xfuncion/sexta/', miSextaPag, name="Sexta"),

    path('xclase/primera/', CategoriaListView.as_view(), name="PrimeraClase"),
    path('xclase/segunda/', FamiliaListView.as_view(), name="SegundaClase"),
    path('xclase/tercera/', ParadaListView.as_view(), name="TerceraClase"),
    path('xclase/cuarta/', Ficha_TecnicaListView.as_view(), name="CuartaClase"),
    path('xclase/quinta/', ImpresoraListView.as_view(), name="QuintaClase"),
    
    path('datatables/categorias', CategoriaDataTableListView.as_view(), name="Datatable"),
]