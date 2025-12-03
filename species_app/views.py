from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Species, Synonym
from .serializers import SpeciesSerializer, SynonymSerializer
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the species index.")


class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer


class SynonymViewSet(viewsets.ModelViewSet):
    queryset = Synonym.objects.all()
    serializer_class = SynonymSerializer