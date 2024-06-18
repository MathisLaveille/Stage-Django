from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Typologie(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'


class Place(models.Model):
    name = models.fields.CharField(max_length=100)
    place = models.CharField(max_length=100)
    population = models.fields.IntegerField()
    typologie = models.ForeignKey(Typologie, null=True, on_delete=models.SET_NULL)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'


class Brand(models.Model):
    marque = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)

    def __str__(self):
        return f'{self.marque}'


class Provider(models.Model):
    marque = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)

    def __str__(self):
        return f'{self.marque}'


class Type_connexion(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'


class Type_equipment(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'


class Network(models.Model):
    class Meta:
        ordering = ["rank"]

    place = models.ForeignKey(Place, null=True, on_delete=models.SET_NULL)
    type_connection = models.ForeignKey(Type_connexion, null=True, on_delete=models.SET_NULL)
    provider = models.ForeignKey(Provider, null=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)

    rank = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(9)
        ]
    )

    rescue = models.BooleanField(default=False)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f'Network for {self.place.name}'



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Platform(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'


class Software(models.Model):
    name = models.fields.CharField(max_length=100)
    version = models.CharField(max_length=100)
    administrator = models.CharField(max_length=100)
    platform = models.ForeignKey(Platform, null=True, on_delete=models.SET_NULL)
    place = models.ForeignKey(Place, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'

class Equipment(models.Model):
    name = models.fields.CharField(max_length=100)
    place = models.ForeignKey(Place, null=True, on_delete=models.SET_NULL)
    type_equipment = models.ForeignKey(Type_equipment, null=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0)
    eligible = models.BooleanField(default=False)
    description = models.CharField(max_length=1024 ,null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return f'{self.type_equipment}'


