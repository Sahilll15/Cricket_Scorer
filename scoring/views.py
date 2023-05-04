from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import get_object_or_404
from django.shortcuts import render, get_object_or_404, redirect
import requests
from .models import Makematch
\
import random
from .models import Makematch, Tournament, Team
from django.http import JsonResponse
from .forms import PlayerForm
from .models import Team
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import TournamentForms, TeamForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .models import Makematch,Team
from .serializers import *


#RestAPi

class TeamList(generics.ListAPIView):
    queryset= Team.objects.all()
    serializer_class=TeamSerializer

class MakeMatchList(generics.ListAPIView):
    queryset=Makematch.objects.all().filter()
    serializer_class=MatchSerializer
  
    def get_queryset(self):
        return Makematch.objects.filter(winner__isnull=False)


#USE THE API
def match_list(request):
    api_url='http://localhost:8000/matches_api/'
    response=requests.get(api_url)
    matches=response.json()
    return render(request, 'scoring/matches.html', {'matches': matches})
# Create your views here.


def signup(request):

    if request.method == 'POST':
        uname = request.POST.get('username')
        uemail = request.POST.get('email')
        upassword = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if upassword != confirm_password:
           messages.error(request, 'Check the password and confirm password ')
        else:

            my_user = User.objects.create_user(
                username=uname, email=uemail, password=upassword)
            my_user.save()
            messages.success(request, 'Signup successful! Please login.')
            # return HttpResponse("User has been Created succesfully!")
            return redirect('login')
            # print(uname,uemail,upassword,confirm_password)

    return render(request, 'scoring/signup.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
           
            return redirect('score')
        else:
           
            messages.error(request, "Invalid password or username")
            return redirect('login')
    return render(request, 'scoring/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# def match_toss(request):
#     return render(request,'scoring/matchtoss.html')
@login_required
def score(request):
    return render(request, 'scoring/score.html')
    # return HttpResponse("You are at the score page")


# start scoring button

def entermatch(request):
    tournaments = Tournament.objects.all()
    teams = Team.objects.all()
    context = {'tournaments': tournaments, 'teams': teams}

    return render(request, 'scoring/entermatch.html', context)


def list_match(request):
    tournaments = Tournament.objects.all()
    teams = Team.objects.all()

    context = {
        'tournaments': tournaments,
        'teams': teams,  # will be updated via AJAX based on selected tournament
    }
    return render(request, 'scoring/make_match.html', context)


def tournament_list(request):
    tournaments = Tournament.objects.all()

    return render(request, 'scoring/tournaments_list.html', {'tournaments': tournaments})

# ['scoring/team_list.html',,'scoring/tournament_form.html','scoring/tournament_list.html']


def tournament_create(request):
    if request.method == 'POST':
        form = TournamentForms(request.POST)
        if form.is_valid():
            tournament = form.save(commit=False)
            # selected_teams = request.POST.getlist('teams')
            tournament.save()
            form.save_m2m()
            
            messages.success(request, 'Tournament created SuccessFully!!')
            return redirect('tournament_create')
    else:
        form = TournamentForms()
        teams = Team.objects.all()
        tournaments = Tournament.objects.all()
        return render(request, 'scoring/tournament_form.html', {'form': form, 'title': 'Create Tournament', 'teams': teams, 'tournaments': tournaments})


def tournament_detail(request, pk):
    tournament = Tournament.objects.get(pk=pk)
    teams = tournament.teams.all()
    return render(request, 'scoring/tournament_details.html', {'tournament': tournament, 'teams': teams})


def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'scoring/team_form.html', {'form': form})


def team_list(request):
    teams = Team.objects.all()
    return render(request, ['scoring/team_list.html', 'scoring/make_match.html'], {'teams': teams})



def make_match(request):
    if request.method == 'POST':
        tournament_id = request.POST['tournament']
        team1_id = request.POST['team1']
        team2_id = request.POST['team2']
        overs=request.POST['Overs']
        tournament = Tournament.objects.get(id=tournament_id)
        team1 = Team.objects.get(id=team1_id)
        team2 = Team.objects.get(id=team2_id)
        
        # match_pin = request.POST['matchpin']
        if team1_id != team2_id :
            match = Makematch.objects.create(
                tournament_name=tournament, team_1=team1, team_2=team2,overs=overs)
            request.session['clear_storage'] = True
            return redirect('match_detail', match_id=match.id)
        else:
            # Handle the case where team1 and team2 are the same
            error_msg = "Error: Please select two different teams"
            tournaments = Tournament.objects.all()
            teams = Team.objects.all()
            context = {'tournaments': tournaments,
                       'teams': teams, 'error_msg': error_msg}
            return render(request, 'scoring/make_match.html', context)
    else:
        tournaments = Tournament.objects.all()
        teams = Team.objects.all()
        request.session['clear_storage'] = True
        context = {'tournaments': tournaments, 'teams': teams}
        return render(request, 'scoring/make_match.html', context)


def match_detail(request, match_id):
    match = Makematch.objects.get(id=match_id)

    context = {'match': match}

    return render(request, 'scoring/matchtoss.html', context)


def scoring(request, match_id):
    request.session['clear_storage'] = True
    match = get_object_or_404(Makematch, id=match_id)
    tournaments = Tournament.objects.all()

    team_a = match.team_1
    team_b = match.team_2
    overs=match.overs
    # team_a_batters = Batter.objects.filter(match=match, player__team=team_a)
    team_a_batters = Player.objects.filter(team=team_a)
    team_b_batters = Player.objects.filter(team=team_b)
    team_a_bowlers = Player.objects.filter(team=team_a, role='Bowler')
    team_b_bowlers = Player.objects.filter(team=team_b,role='Bowler')

    tournaments = match.tournament_name
    teams = Team.objects.all()

    context = {'tournaments': tournaments,
               'team_a': team_a,
               'team_b': team_b,
               'match': match,
               'team_a_batters': team_a_batters,
               'team_b_batters': team_b_batters,
               'team_a_bowlers': team_a_bowlers,
               'team_b_bowlers': team_b_bowlers,
               'tournaments': tournaments,
               'overs':overs
               }

    return render(request, 'scoring/Scoring.html', context)


def team_page(request):
    return render(request, 'scoring/team_page.html')


def add_player(request,):

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Player Added SuccessFully!!')
            return redirect('add_player')
    else:
        form = PlayerForm()

    context = {'form': form}
    return render(request, 'scoring/add_player.html', context)


def add_score(request, match_id):
    if request.method == 'POST':
        team_a_runs = request.POST.get('team_a_runs')
        team_b_runs = request.POST.get('team_b_runs')

        match = get_object_or_404(Makematch, id=match_id)

        if match.team_a_score == 0 and match.team_b_score == 0:
            # update the scores for the match
            match.team_a_score += int(team_a_runs)
            match.team_b_score += int(team_b_runs)

            # determine the winner if both teams have batted once
            if match.team_a_score > 0 and match.team_b_score > 0:
                if match.team_a_score > match.team_b_score:
                    match.winner = match.team_1
                elif match.team_b_score > match.team_a_score:
                    match.winner = match.team_2
                else:
                    match.winner = "Tie"

            match.save()

            # add success message to session
            messages.success(request, 'Score successfully')
            print(request.session['messages'])  # add this line to check messages

        return redirect('scoring:match_detail', match_id=match.id)

    # if the request is not a POST, redirect to home page
    match = get_object_or_404(Makematch, id=match_id)
    return render(request, 'scoring/scoring.html', {'match': match, 'messages': messages.get_messages(request)})



def test(request, match_id):
    request.session['clear_storage'] = True
    match = get_object_or_404(Makematch, id=match_id)
    tournaments = Tournament.objects.all()

    team_a = match.team_1
    team_b = match.team_2

    # team_a_batters = Batter.objects.filter(match=match, player__team=team_a)
    team_a_batters = Player.objects.filter(team=team_a)
    team_b_batters = Player.objects.filter(team=team_b)
    team_a_bowlers = Player.objects.filter(team=team_a)
    team_b_bowlers = Player.objects.filter(team=team_b)

    tournaments = match.tournament_name
    teams = Team.objects.all()

    context = {'tournaments': tournaments,
               'team_a': team_a,
               'team_b': team_b,
               'match': match,
               'team_a_batters': team_a_batters,
               'team_b_batters': team_b_batters,
               'team_a_bowlers': team_a_bowlers,
               'team_b_bowlers': team_b_bowlers,
               'tournaments': tournaments,

               }

    return render(request, 'scoring/test.html', context)


def edit_team(request):
    teams = Team.objects.all()
    return render(request, 'scoring/edit_team.html', {'teams': teams})




def edit_player(request,team_id):
    team = get_object_or_404(Team, pk=team_id)
    players=Player.objects.filter(team_id=team_id)
    return render(request, 'scoring/edit_player.html', {'players': players,'team':team})




def edit_player_names(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    players = Player.objects.filter(team=team)
    if request.method == 'POST':
        for player in players:
            new_name = request.POST.get('player_name_{}'.format(player.id))
            player.name = new_name
            player.save()
        return redirect('edit_player', team_id=team_id)
    else:
        return render(request, 'scoring/edit_player.html', {'players': players, 'team': team})