from django.db import models


class Adressepostale(models.Model):
    nidadressepostale = models.BigAutoField(db_column='nIDAdressepostale', primary_key=True)  # Field name made lowercase.
    nnumerorue = models.IntegerField(db_column='nNumeroRue')  # Field name made lowercase.
    slibellerue = models.CharField(db_column='sLibelleRue', max_length=300)  # Field name made lowercase.
    nidville = models.ForeignKey('Ville', models.DO_NOTHING, db_column='nIDVille')  # Field name made lowercase.
    slongitude = models.CharField(db_column='sLongitude', max_length=50, blank=True, null=True)  # Field name made lowercase.
    slatitude = models.CharField(db_column='sLatitude', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sextension = models.CharField(db_column='sExtension', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adressepostale'


class Archive(models.Model):
    nidarchive = models.BigAutoField(db_column='nIDArchive', primary_key=True)  # Field name made lowercase.
    ntypedarchive = models.CharField(db_column='nTypedarchive', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dtempsconsultation = models.CharField(db_column='dTempsConsultation', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'archive'


class Centre(models.Model):
    nidcentre = models.BigAutoField(db_column='nIDCentre', primary_key=True)  # Field name made lowercase.
    nidadressepostale = models.BigIntegerField(db_column='nIDAdressepostale', blank=True, null=True)  # Field name made lowercase.
    nidgroupe = models.BigIntegerField(db_column='nIDGroupe', blank=True, null=True)  # Field name made lowercase.
    snomcentre = models.CharField(db_column='sNomCentre', max_length=80, blank=True, null=True)  # Field name made lowercase.
    stelephone = models.CharField(db_column='sTelephone', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'centre'


class Consultation(models.Model):
    nidconsultation = models.BigAutoField(db_column='nIDConsultation', primary_key=True)  # Field name made lowercase.
    nidmedecin = models.ForeignKey('Medecin', models.DO_NOTHING, db_column='nIDMedecin')  # Field name made lowercase.
    nidpatient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='nIDPatient')  # Field name made lowercase.
    netatconsultation = models.IntegerField(db_column='nEtatConsultation')  # Field name made lowercase.
    dconsultation = models.DateField(db_column='dConsultation', blank=True, null=True)  # Field name made lowercase.
    hfinconsultation = models.TimeField(db_column='hFinConsultation', blank=True, null=True)  # Field name made lowercase.
    surlroom = models.CharField(db_column='sURLRoom', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bconsultationpartel = models.IntegerField(db_column='bConsultationParTel')  # Field name made lowercase.
    hdebutconsultation = models.TimeField(db_column='hDebutConsultation', blank=True, null=True)  # Field name made lowercase.
    smotif = models.CharField(db_column='sMotif', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssymptome = models.CharField(db_column='sSymptome', max_length=50, blank=True, null=True)  # Field name made lowercase.
    scompterendu = models.CharField(db_column='sCompteRendu', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    nnombrepatient = models.IntegerField(db_column='nNombrePatient', blank=True, null=True)  # Field name made lowercase.
    stypeacte = models.CharField(db_column='sTypeActe', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'consultation'


class Fichier(models.Model):
    nidfichier = models.BigAutoField(db_column='nIDFichier', primary_key=True)  # Field name made lowercase.
    snomfichier = models.CharField(db_column='sNomFichier', max_length=80)  # Field name made lowercase.
    buffichierobjet = models.TextField(db_column='bufFichierObjet')  # Field name made lowercase.
    nidconsultation = models.BigIntegerField(db_column='nIDConsultation')  # Field name made lowercase.
    bprovenance = models.IntegerField(db_column='bProvenance')  # Field name made lowercase.
    nidproprietaire = models.CharField(db_column='nIDProprietaire', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fichier'


class Fileattente(models.Model):
    nidfileattente = models.BigAutoField(db_column='nIDFileAttente', primary_key=True)  # Field name made lowercase.
    nidpatient = models.BigIntegerField(db_column='nIDPatient')  # Field name made lowercase.
    nidmedecin = models.BigIntegerField(db_column='nIDMedecin', blank=True, null=True)  # Field name made lowercase.
    scodeticket = models.CharField(db_column='sCodeTicket', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nnbrpatient = models.IntegerField(db_column='nNbrPatient', blank=True, null=True)  # Field name made lowercase.
    smotifconsultation = models.CharField(db_column='sMotifConsultation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ntag = models.IntegerField(db_column='nTag', blank=True, null=True)  # Field name made lowercase.
    sobservation = models.TextField(db_column='sObservation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fileattente'


class Groupe(models.Model):
    nidgroupe = models.BigIntegerField(db_column='nIDGroupe', primary_key=True)  # Field name made lowercase.
    snomgroupe = models.CharField(db_column='sNomGroupe', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'groupe'


class Horaire(models.Model):
    nidplanning = models.ForeignKey('MedecinPlanning', models.DO_NOTHING, db_column='nIDPlanning', blank=True, null=True)  # Field name made lowercase.
    shoraire = models.CharField(db_column='sHoraire', max_length=50)  # Field name made lowercase.
    spause = models.CharField(db_column='sPause', max_length=50, blank=True, null=True)  # Field name made lowercase.
    njour = models.IntegerField(db_column='nJour', blank=True, null=True)  # Field name made lowercase.
    slibellejour = models.CharField(db_column='sLibelleJour', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'horaire'


class Langue(models.Model):
    nidlangue = models.BigAutoField(db_column='nIDLangue', primary_key=True)  # Field name made lowercase.
    slangue = models.CharField(db_column='sLangue', max_length=50)  # Field name made lowercase.
    scodeisolangue = models.CharField(db_column='sCodeISOLangue', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'langue'


class Logs(models.Model):
    nidlogs = models.BigAutoField(db_column='nIDlogs', primary_key=True)  # Field name made lowercase.
    snomapplication = models.CharField(db_column='sNomApplication', max_length=80)  # Field name made lowercase.
    snomprocedure = models.CharField(db_column='sNomProcedure', max_length=100)  # Field name made lowercase.
    smessageerreur = models.TextField(db_column='sMessageErreur')  # Field name made lowercase.
    sniveau = models.CharField(db_column='sNiveau', max_length=15)  # Field name made lowercase.
    sutilisateur = models.CharField(db_column='sUtilisateur', max_length=100)  # Field name made lowercase.
    dhcreation = models.DateTimeField(db_column='dhCreation')  # Field name made lowercase.
    sstatututilisateur = models.IntegerField(db_column='sStatutUtilisateur')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logs'


class Medecin(models.Model):
    nidmedecin = models.BigAutoField(db_column='nIDMedecin', primary_key=True)  # Field name made lowercase.
    snom = models.CharField(db_column='sNom', max_length=200)  # Field name made lowercase.
    sprenom = models.CharField(db_column='sPrenom', max_length=200)  # Field name made lowercase.
    bdisponible = models.IntegerField(db_column='bDisponible')  # Field name made lowercase.
    smail = models.CharField(db_column='sMail', max_length=200)  # Field name made lowercase.
    stelephone = models.CharField(db_column='sTelephone', max_length=20)  # Field name made lowercase.
    bufmdp = models.TextField(db_column='bufMDP', blank=True, null=True)  # Field name made lowercase.
    ngenre = models.IntegerField(db_column='nGenre')  # Field name made lowercase.
    bufphoto = models.TextField(db_column='bufPhoto', blank=True, null=True)  # Field name made lowercase.
    stokenconnexion = models.CharField(db_column='sTokenConnexion', max_length=80)  # Field name made lowercase.
    srpps = models.BigIntegerField(db_column='sRPPS')  # Field name made lowercase.
    sinformations = models.CharField(db_column='sInformations', max_length=500, blank=True, null=True)  # Field name made lowercase.
    dhdemande = models.DateTimeField(db_column='dhDemande')  # Field name made lowercase.
    dhvalidation = models.DateTimeField(db_column='dhValidation', blank=True, null=True)  # Field name made lowercase.
    dhdernieremodification = models.DateTimeField(db_column='dhDerniereModification', blank=True, null=True)  # Field name made lowercase.
    nidadressepostale = models.BigIntegerField(db_column='nIDAdressepostale')  # Field name made lowercase.
    ndureeconsultationmoyenne = models.IntegerField(db_column='nDureeConsultationMoyenne', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medecin'


class MedecinCentre(models.Model):
    nidcentre = models.ForeignKey(Centre, models.DO_NOTHING, db_column='nIDCentre')  # Field name made lowercase.
    nidmedecin = models.ForeignKey(Medecin, models.DO_NOTHING, db_column='nIDMedecin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medecin_centre'


class MedecinLangue(models.Model):
    nidlangue = models.ForeignKey(Langue, models.DO_NOTHING, db_column='nIDLangue')  # Field name made lowercase.
    nidmedecin = models.ForeignKey(Medecin, models.DO_NOTHING, db_column='nIDMedecin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medecin_langue'


class MedecinPlanning(models.Model):
    nidplanning = models.BigAutoField(db_column='nIDPlanning', primary_key=True)  # Field name made lowercase.
    nidmedecin = models.ForeignKey(Medecin, models.DO_NOTHING, db_column='nIDMedecin')  # Field name made lowercase.
    nidcentre = models.ForeignKey(Centre, models.DO_NOTHING, db_column='nIDCentre')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medecin_planning'


class MedecinSpecialite(models.Model):
    nidmedecin = models.ForeignKey(Medecin, models.DO_NOTHING, db_column='nIDMedecin')  # Field name made lowercase.
    nidspecialite = models.ForeignKey('Specialite', models.DO_NOTHING, db_column='nIDSpecialite')  # Field name made lowercase.
    sjour = models.CharField(db_column='sJour', max_length=50, blank=True, null=True)  # Field name made lowercase.
    scodervbcouleur = models.CharField(db_column='sCodeRVBCouleur', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medecin_specialite'


class Parametre(models.Model):
    nidparametre = models.BigAutoField(db_column='nIDParametre', primary_key=True)  # Field name made lowercase.
    suuid = models.CharField(db_column='sUUID', max_length=128)  # Field name made lowercase.
    stypeparam = models.CharField(db_column='sTypeParam', max_length=80)  # Field name made lowercase.
    scodeparam = models.CharField(db_column='sCodeParam', max_length=50)  # Field name made lowercase.
    scontenu = models.CharField(db_column='sContenu', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parametre'


class Patient(models.Model):
    nidpatient = models.BigAutoField(db_column='nIDPatient', primary_key=True)  # Field name made lowercase.
    snom = models.CharField(db_column='sNom', max_length=200)  # Field name made lowercase.
    sprenom = models.CharField(db_column='sPrenom', max_length=200)  # Field name made lowercase.
    smail = models.CharField(db_column='sMail', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bufmotdepasse = models.TextField(db_column='bufMotDePasse', blank=True, null=True)  # Field name made lowercase.
    stelephone = models.CharField(db_column='sTelephone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nnumsecusocial = models.BigIntegerField(db_column='nNumSecuSocial', blank=True, null=True)  # Field name made lowercase.
    ngenre = models.IntegerField(db_column='nGenre')  # Field name made lowercase.
    dnaissance = models.DateField(db_column='dNaissance', blank=True, null=True)  # Field name made lowercase.
    nidadressepostale = models.BigIntegerField(db_column='nIDAdressepostale', blank=True, null=True)  # Field name made lowercase.
    noriginecreation = models.IntegerField(db_column='nOrigineCreation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient'


class Pays(models.Model):
    nidpays = models.BigAutoField(db_column='nIDPays', primary_key=True)  # Field name made lowercase.
    snompays = models.CharField(db_column='sNomPays', max_length=50)  # Field name made lowercase.
    scodepays = models.CharField(db_column='sCodePays', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nidlangue = models.BigIntegerField(db_column='nIDLangue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pays'


class Rendezvous(models.Model):
    nidrendezvous = models.BigAutoField(db_column='nIDrendezVous', primary_key=True)  # Field name made lowercase.
    nidpatient = models.BigIntegerField(db_column='nIDPatient')  # Field name made lowercase.
    nidmedecin = models.BigIntegerField(db_column='nIDMedecin')  # Field name made lowercase.
    drendezvous = models.DateField(db_column='dRendezVous')  # Field name made lowercase.
    hrendezvous = models.TimeField(db_column='hRendezVous')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rendezvous'


class Specialite(models.Model):
    nidspecialite = models.BigAutoField(db_column='nIDSpecialite', primary_key=True)  # Field name made lowercase.
    snom = models.CharField(db_column='sNom', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'specialite'


class Tokbox(models.Model):
    stoken = models.TextField(blank=True, null=True)
    blibre = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tokbox'


class Ville(models.Model):
    nidville = models.BigAutoField(db_column='nIDVille', primary_key=True)  # Field name made lowercase.
    snomville = models.CharField(db_column='sNomVille', max_length=60)  # Field name made lowercase.
    ncodepostal = models.IntegerField(db_column='nCodePostal')  # Field name made lowercase.
    nidpays = models.BigIntegerField(db_column='nIDPays', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ville'
