from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, rut, email, username, nombre, telefono, password=None, **extra_fields):
        if not rut:
            raise ValueError('El RUT debe ser proporcionado')
        email = self.normalize_email(email)
        user = self.model(rut=rut, email=email, username=username, nombre=nombre, telefono=telefono, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rut, email, username, nombre, telefono, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(rut, email, username, nombre, telefono, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    rut = models.CharField(_('RUT'), max_length=12, unique=True, primary_key=True)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=50, unique=True)
    nombre = models.CharField(_('nombre'), max_length=100)
    telefono = models.CharField(_('teléfono'), max_length=8)
    birthdate = models.DateField('fecha de nacimiento', null=True, blank=True)
    is_active = models.BooleanField(_('activo'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rut', 'username', 'nombre', 'telefono']

    def __str__(self):
        return self.nombre


class Caso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    estado = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    abogado = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='casos_abogado')

    def __str__(self):
        return self.nombre

    
class Presupuesto(models.Model):
    descripcion = models.TextField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    estado = models.CharField(max_length=50)
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE, related_name='presupuestos')
    abogado = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='presupuestos_abogado')

    def __str__(self):
        return self.descripcion


class Contrato(models.Model):
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE, related_name='contratos')
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    modalidad_pago = models.CharField(max_length=255)
    fecha_firma = models.DateField()
    fecha_vencimiento = models.DateField(blank=True, null=True)
    abogado = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contratos_abogado')

    def __str__(self):
        return f"Contrato {self.id}"

