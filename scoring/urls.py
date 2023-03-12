from django.urls import path
from . import views

urlpatterns =[
    # path('',views.home,name="home"),

    path('login/',views.login_view,name="login"),
    path('',views.signup,name="signup"),
    path('score/',views.score,name="score"),
    path('logout/',views.logout_view,name="logout"),
    path('makematch/',views.make_match,name="make_match"),
    path('matchtoss/',views.match_toss,name="matchtoss"),
    path('scoring/',views.scoring,name="scoring"),
    path('entermatch/',views.entermatch,name="entermatch"),
    path('tournament_create/',views.tournament_create,name="tournament_create"),
    path('tournament_list/',views.tournament_list,name="tournament_list"),
    path('tournament_details/<int:pk>',views.tournament_detail,name="tournament_detail"),
    path('create_teams/',views.team_create,name="team_create"),
    path('list_teams/',views.team_list,name="team_list"),

     


]

