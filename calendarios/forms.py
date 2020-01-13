from django import forms
from .models import Reservas

from datetime import timedelta

class AddClientForm(forms.Form): # If let blank, they are REQUIRED by default
    casa = forms.ChoiceField(label='Casa', choices=[('', 'Seleccione una casa'), (1, 'Barro Roga'), (2, 'Ysypo Roga'), (3, 'Hierro Roga')], widget=forms.Select(attrs={'class':'form-control'}))
    nombre = forms.CharField(label='Nombre', max_length=150, strip=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del cliente'}))
    email = forms.EmailField(required=False, label='Email', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email del cliente'}))
    cantidad_personas = forms.IntegerField(label='Cantidad de personas', min_value=1, max_value=10, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cantidad de personas'}))
    fecha_inicio = forms.DateField(label='Fecha de inicio', widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    fecha_fin = forms.DateField(label='Fecha de fin', widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    cantidad_dias = forms.IntegerField(label='Cantidad de dias', min_value=0, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cantidad de dias'}))
    notas = forms.CharField(required=False, label='Notas', widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Notas'}))

    # TODO: For some reason this doesnt work AGAIN
    # TODO: Make sure nobody selects the 'Seleccione una casa' option (A.K.A. find a way to validate it)
    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        casa = cleaned_data.get('casa')
        cantidad_dias = cleaned_data.get('cantidad_dias')

        if fecha_fin and fecha_inicio and cantidad_dias:
            if not ((fecha_fin - fecha_inicio) >= timedelta(days=0)):
                raise forms.ValidationError("ERROR: La fecha final es antes de la fecha inicial.")
            if Reservas.objects.filter(fecha_inicio__gte=fecha_inicio).filter(fecha_fin__lte=fecha_fin).filter(casa=casa):
                raise forms.ValidationError("ERROR: Esta fecha ya fue reservada para esta casa.")
            if not ((fecha_fin - fecha_inicio) == timedelta(days=cantidad_dias)):
                raise forms.ValidationError('ERROR: La cantidad de dias introducida no coincide con las fechas.')
            if casa == '':
                self.add_error('casa', 'ERROR: La casa seleccionada no es válida.')

        return cleaned_data