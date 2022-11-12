from django import forms
from .models import Citas
from .models import Especialidad

def crear_cita(request):
    citas = Citas.objects.filter(usuario=request.user, fecha_completada__isnull=True)

class CitasForm(forms.ModelForm):
    class Meta:
        model = Citas
        fields = ['titulo', 'descripcion','important']
        
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el titulo de la cita'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe la descripcion de la cita'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check'}),
            #'especialidad': forms.Select(attrs={'option':'gato'}),
            
        }

class AreasForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['Nombre_Especialidad']
        
        widgets = {
            'Nombre_Especialidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Esccribe la especialidad'})
            
            
        }