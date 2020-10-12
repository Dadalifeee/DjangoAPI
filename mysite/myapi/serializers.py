from rest_framework import serializers

from .models import Patient, Medecin, Adressepostale, Archive, Centre, Consultation, Fichier, Groupe, Horaire, Langue, \
    Logs, Parametre, Pays, Rendezvous, Specialite, Ville, Tokbox, Fileattente


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class MedecinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medecin
        fields = "__all__"

class AdresseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adressepostale
        fields = "__all__"

class ArchiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Archive
        fields = "__all__"

class CentreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Centre
        fields = "__all__"

class FileattenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fileattente
        fields = "__all__"

class ConsultationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Consultation
        fields = "__all__"

class HoraireSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horaire
        fields = "__all__"

class LangueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Langue
        fields = "__all__"


class FichierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fichier
        fields = "__all__"

class GroupeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Groupe
        fields = "__all__"

class LogsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Logs
        fields = "__all__"

class ParametreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parametre
        fields = "__all__"

class PaysSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pays
        fields = "__all__"


class RendezvousSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rendezvous
        fields = "__all__"

class SpecialiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Specialite
        fields = "__all__"

class VilleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ville
        fields = "__all__"

class TokboxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tokbox
        fields = "__all__"
