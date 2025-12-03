from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpeciesViewSet, SynonymViewSet

# from . import views



router = DefaultRouter()
router.register(r"species", SpeciesViewSet)
router.register(r"synonyms", SynonymViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]


# urlpatterns = [
#     path("", views.index, name="index"),
# ]