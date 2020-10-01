from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name


class Patient(models.Model):
    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=60)
    telephone = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    date = models.DateField()
    def __str__(self):
        return self.nom

class Medecin(models.Model):
    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=60)
    telephone = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    date = models.DateField()
    specialite = models.CharField(max_length=60)
    langue = models.CharField(max_length=60)
    centre = models.CharField(max_length=60)
    def __str__(self):
        return self.nom

