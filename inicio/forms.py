from django import forms


class CreacionJugadorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(max_length=20)
    posicion = forms.CharField(max_length=20)

    
class BuscarJugador(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)