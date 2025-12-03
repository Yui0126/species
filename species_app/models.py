from django.db import models

# Create your models here.

class Species(models.Model):
    scientific = models.CharField(max_length=255, unique=True, null=False, blank=False)
    main_common_jp = models.CharField(max_length=255, null=True, blank=True)
    main_common_en = models.CharField(max_length=255, null=True, blank=True)

    itis_tsn = models.IntegerField(null=True, blank=True)
    cites_id = models.IntegerField(null=True, blank=True)
    iucn_id = models.IntegerField(null=True, blank=True)

    class_name = models.CharField(max_length=255, null=True, blank=True)
    order = models.CharField(max_length=255, null=True, blank=True)
    suborder = models.CharField(max_length=255, null=True, blank=True)
    family = models.CharField(max_length=255, null=True, blank=True)
    subfamily = models.CharField(max_length=255, null=True, blank=True)
    genus = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.scientific or "Unnamed species"
    
        
class Synonym(models.Model):

    class NameType(models.TextChoices):
        SCIENTIFIC = 'scientific', 'Scientific name'
        COMMON_JP = 'common_jp', 'Common name (Japanese)'
        COMMON_EN = 'common_en', 'Common name (English)'
        OTHERS = 'others', 'Others'

    species = models.ForeignKey(
        'Species',
        on_delete=models.CASCADE,
        related_name='names'
    )

    name = models.CharField(max_length=255, null=False, blank=False)

    type = models.CharField(
        max_length=20,
        choices=NameType.choices,
        default=NameType.SCIENTIFIC,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['species', 'type', 'name'],
                name='unique_species_name_type'
            )
        ]

    def __str__(self):
        return f"{self.name} ({self.type})"

class SpeciesImage(models.Model):
    species = models.ForeignKey(
        'Species',
        on_delete=models.CASCADE,
        related_name='images'
    )

    image_url = models.URLField()

    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Image for {self.species.scientific}: {self.image_url}"