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


    



]
