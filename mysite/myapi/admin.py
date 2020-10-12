from django.contrib import admin
from .models import Patient, Medecin, Adressepostale, Archive, Centre, Consultation, Fichier, Fileattente, Groupe, \
    Horaire, Langue, Logs, MedecinCentre, MedecinLangue, MedecinPlanning, MedecinSpecialite, Parametre, Pays, \
    Rendezvous, Specialite, Tokbox, Ville

admin.site.register(Patient)
admin.site.register(Medecin)
admin.site.register(Adressepostale)
admin.site.register(Archive)
admin.site.register(Centre)
admin.site.register(Consultation)
admin.site.register(Fichier)
admin.site.register(Fileattente)
admin.site.register(Groupe)
admin.site.register(Horaire)
admin.site.register(Langue)
admin.site.register(Logs)
admin.site.register(MedecinCentre)
admin.site.register(MedecinLangue)
admin.site.register(MedecinPlanning)
admin.site.register(MedecinSpecialite)
admin.site.register(Parametre)
admin.site.register(Pays)
admin.site.register(Rendezvous)
admin.site.register(Specialite)
admin.site.register(Tokbox)
admin.site.register(Ville)
