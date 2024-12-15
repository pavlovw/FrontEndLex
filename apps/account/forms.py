from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from itertools import cycle
import datetime


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email', 'username', 'nombre', 'telefono', 'rut', 'birthdate', 'password1', 'password2']

    def clean_rut(self):
        rut = self.cleaned_data['rut'].strip().replace('.', '').replace('-', '')  # Limpiar formato
        if not self.validar_rut(rut):
            raise forms.ValidationError("El RUT no es válido.")
        return rut

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está en uso. Por favor, usa otro.")
        return email
    
    def clean_birthdate(self):
        birthdate = self.cleaned_data.get('birthdate')
        if birthdate:
            if isinstance(birthdate, datetime.date):  # Verifica si birthdate ya es datetime.date
                return birthdate  # Retorna birthdate si ya es un objeto date

            try:
                birthdate = datetime.datetime.strptime(birthdate, '%d/%m/%Y').date()
            except ValueError:
                raise forms.ValidationError("Formato de fecha incorrecto. Utiliza el formato DD/MM/YYYY.")
        return birthdate

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def validar_rut(self, rut):
        rut = rut.upper()
        rut = rut.replace("-", "")
        rut = rut.replace(".", "")
        rut = rut.replace(",", "")
        rut = rut.replace(" ", "")
        aux = rut[:-1]
        dv = rut[-1:]

        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(revertido, factors))
        res = (-s) % 11

        if str(res) == dv:
            return True
        elif dv == "K" and res == 10:
            return True
        else:
            return False

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', max_length=254)
