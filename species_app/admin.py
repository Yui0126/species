from django.contrib import admin
from .models import Species, Synonym, SpeciesImage

# Register your models here.


class SynonymInline(admin.TabularInline):
    model = Synonym
    extra = 1

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ("id", "scientific", "main_common_en", "main_common_jp")
    search_fields = ("scientific", "main_common_en", "main_common_jp")
    list_filter = ("class_name", "order", "family")
    inlines = [SynonymInline]

@admin.register(Synonym)
class SynonymAdmin(admin.ModelAdmin):
    list_display = ("id", "species", "name")
    search_fields = ("name",)


admin.register(SpeciesImage)
