from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'med', views.MedecinViewSetid)
router.register(r'pat', views.PatientViewSetid)
router.register(r'adresse', views.AdresseViewSetid)
router.register(r'archive', views.ArchiveViewSetid)
router.register(r'centre', views.CentreViewSetid)
router.register(r'consultation', views.ConsultationViewSetid)
router.register(r'fichier', views.FichierViewSetid)
router.register(r'fileattente', views.FileattenteViewSetid)
router.register(r'groupe', views.GroupeViewSetid)
router.register(r'horaire', views.HoraireViewSetid)
router.register(r'langue', views.LangueViewSetid)
router.register(r'logs', views.LogsViewSetid)
router.register(r'parametre', views.ParametreViewSetid)
router.register(r'pays', views.PaysViewSetid)
router.register(r'rendezvous', views.RendezvousViewSetid)
router.register(r'specialite', views.SpecialiteViewSetid)
router.register(r'tokbox', views.TokboxViewSetid)
router.register(r'ville', views.VilleViewSetid)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('patient/', views.PatientViewSet.as_view()),
    path('medecin/', views.MedecinViewSet.as_view()),

]