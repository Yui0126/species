from rest_framework import serializers
from .models import Species, Synonym

class SynonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synonym
        fields = "__all__"


class SpeciesSerializer(serializers.ModelSerializer):
    # Optional: automatically show related synonyms for each species
    synonyms = SynonymSerializer(many=True, read_only=True)

    class Meta:
        model = Species
        fields = "__all__"
