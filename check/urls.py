from django.urls import path

from . import views

app_name = "check"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:scientific_id>", views.edit, name="edit"),
    path("<int:scientific_id>", views.update, name="update")
]