from django import forms
from ejemplo.models import Familiar, Automovil, Mascota

class BuscarFamiliar(forms.Form):
    nombre = forms.CharField(max_length=100)

class BuscarAutomoviles(forms.Form):
    propietario = forms.CharField(max_length=100)

class BuscarMascotas(forms.Form):
    nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']

class AutomovilForm(forms.ModelForm):
  class Meta:
    model = Automovil
    fields = ['propietario', 'marca', 'color', 'patente']

class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = ['nombre', 'propietario', 'raza', 'edad']
