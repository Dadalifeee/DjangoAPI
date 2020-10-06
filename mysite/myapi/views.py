from django.shortcuts import render

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


from .serializers import HeroSerializer, PatientSerializer, MedecinSerializer
from .models import Hero, Patient, Medecin


class HeroViewSet(generics.ListCreateAPIView):
    filterset_fields  = ['name', 'alias']
    filter_backends = [DjangoFilterBackend]
    queryset = Hero.objects.all().order_by('id')
    serializer_class = HeroSerializer

class PatientViewSet(generics.ListCreateAPIView):
    filterset_fields  = ['nom', 'prenom', 'email', 'password', 'id']
    filter_backends = [DjangoFilterBackend]
    queryset = Patient.objects.all().order_by('id')
    serializer_class = PatientSerializer

class PatientViewSetid(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('id')
    serializer_class = PatientSerializer

class MedecinViewSet(generics.ListCreateAPIView):
    filterset_fields  = ['nom', 'prenom', 'email', 'password','id']
    filter_backends = [DjangoFilterBackend]
    queryset = Medecin.objects.all().order_by('id')
    serializer_class = MedecinSerializer

class MedecinViewSetid(viewsets.ModelViewSet):
    queryset = Medecin.objects.all().order_by('id')
    serializer_class = MedecinSerializer