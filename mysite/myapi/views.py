from django.shortcuts import render

from rest_framework import viewsets

from .serializers import HeroSerializer, PatientSerializer, MedecinSerializer
from .models import Hero, Patient, Medecin


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('id')
    serializer_class = HeroSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('id')
    serializer_class = PatientSerializer

class MedecinViewSet(viewsets.ModelViewSet):
    queryset = Medecin.objects.all().order_by('id')
    serializer_class = MedecinSerializer