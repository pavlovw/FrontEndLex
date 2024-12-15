from django import forms
from apps.account.models import CustomUser, Caso, Contrato

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['rut', 'nombre', 'email']


class CasoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(is_staff=False),
        to_field_name='rut',
        label='Cliente'
    )
    abogado = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(is_staff=True),
        to_field_name='rut',
        label='Abogado'
    )

    class Meta:
        model = Caso
        fields = ['nombre', 'cliente', 'abogado', 'estado', 'fecha_inicio', 'fecha_fin']

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['costo', 'modalidad_pago', 'fecha_firma', 'fecha_vencimiento']
