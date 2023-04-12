
from inicio.models import Jugador
from django.shortcuts import render, redirect
from inicio.forms import CreacionJugadorFormulario, BuscarJugador






def crear_jugador(request):
    
    if request.method == "POST":
        formulario = CreacionJugadorFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            jugador = Jugador(nombre=datos_correctos['nombre'], edad=datos_correctos['edad'], fecha_nacimiento=datos_correctos['fecha_nacimiento'], posicion=datos_correctos['posicion'],  )
            jugador.save()

            return redirect('inicio:listar_jugadores')
    
    formulario = CreacionJugadorFormulario()
    return render(request, 'inicio/crear_jugador.html', {'formulario': formulario})

def lista_jugadores(request):
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar:
        jugadores = Jugador.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        jugadores = Jugador.objects.all()
    formulario_busqueda = BuscarJugador()
    return render(request, 'inicio/lista_jugadores.html', {'jugadores': jugadores, 'formulario': formulario_busqueda})


    