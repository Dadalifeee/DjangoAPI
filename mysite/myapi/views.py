from django.shortcuts import render

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


from .serializers import *
from .models import *


class PatientViewSet(generics.ListCreateAPIView):
    filterset_fields  = ['snom', 'sprenom', 'smail','nidpatient']
    filter_backends = [DjangoFilterBackend]
    queryset = Patient.objects.all().order_by('nidpatient')
    serializer_class = PatientSerializer

class PatientViewSetid(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('nidpatient')
    serializer_class = PatientSerializer

class MedecinViewSet(generics.ListCreateAPIView):
    filterset_fields  = ['snom', 'sprenom', 'smail','nidmedecin']
    filter_backends = [DjangoFilterBackend]
    queryset = Medecin.objects.all().order_by('nidmedecin')
    serializer_class = MedecinSerializer

class MedecinViewSetid(viewsets.ModelViewSet):
    queryset = Medecin.objects.all().order_by('nidmedecin')
    serializer_class = MedecinSerializer

class AdresseViewSetid(viewsets.ModelViewSet):
    queryset = Adressepostale.objects.all()
    serializer_class = AdresseSerializer

class ArchiveViewSetid(viewsets.ModelViewSet):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer

class CentreViewSetid(viewsets.ModelViewSet):
    queryset = Centre.objects.all()
    serializer_class = CentreSerializer


class ConsultationViewSetid(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer


class FichierViewSetid(viewsets.ModelViewSet):
    queryset = Fichier.objects.all()
    serializer_class = FichierSerializer


class FileattenteViewSetid(viewsets.ModelViewSet):
    queryset = Fileattente.objects.all()
    serializer_class = FileattenteSerializer


class GroupeViewSetid(viewsets.ModelViewSet):
    queryset = Groupe.objects.all()
    serializer_class = GroupeSerializer


class HoraireViewSetid(viewsets.ModelViewSet):
    queryset = Horaire.objects.all()
    serializer_class = HoraireSerializer


class LangueViewSetid(viewsets.ModelViewSet):
    queryset = Langue.objects.all()
    serializer_class = LangueSerializer

class LogsViewSetid(viewsets.ModelViewSet):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer

class ParametreViewSetid(viewsets.ModelViewSet):
    queryset = Parametre.objects.all()
    serializer_class = ParametreSerializer


class PaysViewSetid(viewsets.ModelViewSet):
    queryset = Pays.objects.all()
    serializer_class = PaysSerializer


class RendezvousViewSetid(viewsets.ModelViewSet):
    queryset = Rendezvous.objects.all()
    serializer_class = RendezvousSerializer

class SpecialiteViewSetid(viewsets.ModelViewSet):
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer

class TokboxViewSetid(viewsets.ModelViewSet):
    queryset = Tokbox.objects.all()
    serializer_class = TokboxSerializer

class VilleViewSetid(viewsets.ModelViewSet):
    queryset = Ville.objects.all()
    serializer_class = VilleSerializer
