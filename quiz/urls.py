from django.urls import path
from . import views

app_name = "quiz"
urlpatterns = [
    path("", views.index, name="index"),
    path("team_quiz", views.team_quiz, name="team_quiz"),
    path("player_quiz", views.player_quiz, name="player_quiz")    
]