from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    genre = models.CharField(choices=Genre.choices, max_length=5)
    name = models.CharField(max_length=100)
    biography = models.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(null=True, blank=True, default=0,
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = 'RC'
        CLOTHING = 'CL'
        POSTERS = 'PS'
        MISCELLANEOUS = 'MS'

    type = models.CharField(choices=Type.choices, max_length=5)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    sold = models.BooleanField(default=False)
    year = models.IntegerField(blank=True, null=True)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)