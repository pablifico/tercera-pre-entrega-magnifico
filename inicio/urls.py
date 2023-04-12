from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.mi_vista, name='inicio'),

    path('crear-jugador/', views.crear_jugador, name='crear_jugador'),
    path('jugadores/', views.lista_jugadores, name='listar_jugadores'),

]
