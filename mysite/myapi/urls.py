from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
#router.register(r'heroes', views.HeroViewSet)
router.register(r'med', views.MedecinViewSetid)
router.register(r'pat', views.PatientViewSetid)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('patient/', views.PatientViewSet.as_view()),
    path('medecin/', views.MedecinViewSet.as_view()),
    path('heroes/', views.HeroViewSet.as_view()),

]