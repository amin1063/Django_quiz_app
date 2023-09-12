from rest_framework import routers
from django.urls import include, path
from .views import *
from Quiz.views import PersonViewSet, SpeciesViewSet

router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'species', SpeciesViewSet)


urlpatterns = [
    path('', include(router.urls)),

]