from django.db import models

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

'''class equipment(models.Model):
    name = models.fields.CharField(max_length=100)
    nbr = models.fields.IntegerField()
    description = models.CharField(max_length=1000)
    eligibility = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

class fournisseur(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'

class fournisseur(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)

class type_connexion(models.Model):
    name = models.fields.CharField(max_length=100)

class network(models.Model):
    name_company = models.fields.CharField(max_length=100)
    connection = models.fields.CharField(max_length=100)
    connection_help = models.CharField(max_length=100)

    description = models.CharField(max_length=1000)
'''
