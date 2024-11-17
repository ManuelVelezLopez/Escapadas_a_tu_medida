from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('reservar/<int:propiedad_id>/', views.crear_reserva, name='crear_reserva'),
    path('buscar/', views.buscar_alojamientos, name='buscar_alojamientos'),
    path('gestionPropiedad/create', views.crear_propiedad, name='crear_propiedad'),
    path('gestionPropiedad/delete/<int:propiedad_id>/', views.eliminar_propiedad, name='eliminar_propiedad'),
    path('gestionPropiedad/update/<int:propiedad_id>/', views.actualizar_propiedad, name='editar_propiedad'),
    path('gestionPropiedad/show/<int:propiedad_id>/', views.mostrar_detalles_propiedad, name='mostrar_propiedad'),
    path('gestionPropiedad/', views.listar_propiedades_propietario, name='listar_propiedades_propietario'),
    path('historialReservas/', views.historial_reservas, name='historial_reservas'),
    path('agregarListaDeseos/<int:propiedad_id>/', views.agregar_propiedad_deseada, name='agregar_lista_deseos'),
    path('listaDeseos/', views.obtener_lista_deseos, name='lista_deseos'),
    path('eliminarListaDeseos/<int:propiedad_id>/', views.eliminar_de_lista_deseos, name='eliminar_lista_deseos'),
]
