from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("start/<str:difficulty>/", views.start_game, name="start"),
    path("play/", views.play, name="play"),
]