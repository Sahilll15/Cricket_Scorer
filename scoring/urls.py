from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import TeamList,MakeMatchList
urlpatterns = [
    # path('',views.home,name="home"),

    path('', views.login_view, name="login"),
    path('scoring/<int:match_id>/', views.scoring, name="scoring"),
    path('signup/', views.signup, name="signup"),
    path('score/', views.score, name="score"),
    path('logout/', views.logout_view, name="logout"),
    path('makematch/', views.make_match, name="make_match"),
    path('makematch/<int:match_id>/', views.match_detail, name='match_detail'),
    # path('matchtoss/',views.match_detail,name="match_detail"),
    path('makematch/<int:match_id>/scoring/', views.scoring, name="scoring"),
    # path('makematch/<int:match_id>/slug:slug>/',views.scoring,name="score"),
    path('scoring/', views.scoring, name="scoring"),
    path('entermatch/', views.entermatch, name="entermatch"),
    path('tournament_create/', views.tournament_create, name="tournament_create"),
    path('tournament_list/', views.tournament_list, name="tournament_list"),
    path('tournament_details/<int:pk>',
         views.tournament_detail, name="tournament_detail"),
    path('create_teams/', views.team_create, name="team_create"),
    path('list_teams/', views.team_list, name="team_list"),
    path('edit_team/<int:team_id>/', views.edit_player, name='edit_player'),
    path('edit_team/', views.edit_team, name="edit_team"),
    path('edit_player/<int:team_id>', views.edit_player, name='edit_player'),

    path('team_page/', views.team_page, name="team_page"),
    path('add_player/', views.add_player, name="add_player"),

    path('makematch/<int:match_id>/scoring/add_score/',
         views.add_score, name='add_score'),
    path('edit_player_names/<int:team_id>/', views.edit_player_names, name='edit_player_names'),
    path('logout/', LogoutView.as_view(), name='logout'),

   
   #API urls
    path('teams/',TeamList.as_view(),name='team_Api'),
    path('matches_api/',MakeMatchList.as_view(),name='Match_Api'),


    path('matches/',views.match_list, name='match_list'),

]
