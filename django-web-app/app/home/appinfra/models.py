from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser

class Typologie(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    description = models.CharField(max_length=1000, verbose_name=_('description'))

    def __str__(self):
        return f'{self.name}'


class Place(models.Model):
    name = models.fields.CharField(max_length=100, verbose_name=_('name'))
    place = models.CharField(max_length=100, verbose_name=_('place'))
    population = models.fields.IntegerField(verbose_name=_('population'))
    typology = models.ForeignKey(Typologie, null=True, on_delete=models.SET_NULL, verbose_name=_('typology'))
    latitude = models.CharField(max_length=100, verbose_name=_('latitude'))
    longitude = models.CharField(max_length=100, verbose_name=_('longitude'))
    description = models.CharField(max_length=1000, verbose_name=_('description'))

    def __str__(self):
        return f'{self.name}'


class Brand(models.Model):
    brand = models.fields.CharField(max_length=100, verbose_name=_('brand'))
    description = models.fields.CharField(max_length=1000, verbose_name=_('description'))

    def __str__(self):
        return f'{self.brand}'


class Provider(models.Model):
    brand = models.fields.CharField(max_length=100, verbose_name=_('brand'))
    description = models.fields.CharField(max_length=1000, verbose_name=_('description'))

    def __str__(self):
        return f'{self.brand}'


class Type_connexion(models.Model):
    name = models.fields.CharField(max_length=100, verbose_name=_('name'))
    description = models.CharField(max_length=1000, verbose_name=_('description'))

    def __str__(self):
        return f'{self.name}'


class Type_equipment(models.Model):
    name = models.fields.CharField(max_length=100, verbose_name=_('name'))
    description = models.CharField(max_length=1000, verbose_name=_('description'))

    def __str__(self):
        return f'{self.name}'


class Network(models.Model):
    class Meta:
        ordering = ["rank"]

    place = models.ForeignKey(Place, null=True, on_delete=models.SET_NULL, verbose_name=_('place'))
    connection_type = models.ForeignKey(Type_connexion, null=True, on_delete=models.SET_NULL, verbose_name=_('connection_type'))
    provider = models.ForeignKey(Provider, null=True, on_delete=models.SET_NULL, verbose_name=_('provider'))
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL, verbose_name=_('brand'))

    rank = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(9)], verbose_name=_('rank'))

    rescue = models.BooleanField(default=False, verbose_name=_('rescue'))
    description = models.CharField(max_length=1000, verbose_name=_('description'))

    def __str__(self):
        return f'Network for {self.place.name}'

class Platform(models.Model):
    name = models.fields.CharField(max_length=100, verbose_name=_('name'))
    description = models.CharField(max_length=1000, verbose_name=_('description'))

    def __str__(self):
        return f'{self.name}'


class Software(models.Model):
    name = models.fields.CharField(max_length=100, verbose_name=_('name'))
    version = models.CharField(max_length=100, verbose_name=_('version'))
    administrator = models.CharField(max_length=100, verbose_name=_('administrator'))
    platform = models.ForeignKey(Platform, null=True, on_delete=models.SET_NULL, verbose_name=_('platform'))
    place = models.ForeignKey(Place, null=True, on_delete=models.SET_NULL, verbose_name=_('place'))
    description = models.CharField(max_length=1000, verbose_name=_('description'))

    def __str__(self):
        return f'{self.name}'

class Equipment(models.Model):
    name = models.fields.CharField(max_length=100, verbose_name=_('name'))
    place = models.ForeignKey(Place, null=True, on_delete=models.SET_NULL, verbose_name=_('place'))
    type_equipment = models.ForeignKey(Type_equipment, null=True, on_delete=models.SET_NULL, verbose_name=_('type_equipment'))
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_('brand'))
    quantity = models.IntegerField(default=0, verbose_name=_('quantity2'))
    eligible = models.BooleanField(default=False, verbose_name=_('eligible'))
    description = models.CharField(max_length=1024 ,null=True, blank=True, verbose_name=_('description'))
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children', verbose_name=_('parent'))

    def __str__(self):
        return f'{self.type_equipment}'

# Model pour la gestion des utilisateurs
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Administrateur'),
        ('USER', 'Utilisateur standard'),
        ('GUEST', 'Invité'),
    ]
    
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='USER',
        verbose_name=_('Rôle')
    )
    
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name=_('Numéro de téléphone')
    )
    
    date_modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Date de modification')
    )

    class Meta:
        verbose_name = _('Utilisateur')
        verbose_name_plural = _('Utilisateurs')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"