from django.conf.urls import url
from . import views



#para llamar a nuestra página para insertar tenemos que invocar la dirección /pelicula/nueva

# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.

urlpatterns = [
    #url('', views.lista_peliculas, name ='lista_peliculas'),
    url('alumno/nuevo/', views.alumno_nuevo, name='alumno_nuevo'),
    ]

