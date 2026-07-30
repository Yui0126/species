from django.db import models

# Create your models here.
class Scientific(models.Model):
    scientific_main = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date added')
    def __str__(self):
        return self.scientific_main

class ScientificSynonym(models.Model):
    scientific = models.ForeignKey(Scientific, on_delete=models.CASCADE)
    synonym = models.CharField(max_length=200)

class CommonEn(models.Model):
    scientific = models.ForeignKey(
        Scientific,
        on_delete=models.CASCADE,
        related_name="english_names"
    )
    commonen = models.CharField(max_length=200)
    def __str__(self):
        return self.commonen
    
class CommonJp(models.Model):
    scientific = models.ForeignKey(
        Scientific,
        on_delete=models.CASCADE,
        related_name="japanese_names"
    )
    commonjp = models.CharField(max_length=200)
    def __str__(self):
        return self.commonjp