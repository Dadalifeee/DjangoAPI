from rest_framework import serializers

from .models import Hero, Patient, Medecin


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'nom', 'prenom', 'email', 'date')

class MedecinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medecin
        fields = ('id', 'nom', 'prenom', 'email', 'date', 'specialite', 'langue', 'centre')