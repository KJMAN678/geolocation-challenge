from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("clicked", views.clicked, name="clicked"),
    path("save-location", views.save_location, name="save_location"),
]
