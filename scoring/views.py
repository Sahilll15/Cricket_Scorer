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



# Create your views here.
def signup(request):

    if request.method == 'POST':
        uname = request.POST.get('username')
        uemail = request.POST.get('email')
        upassword = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if upassword != confirm_password:
            return HttpResponse("The passwords in the two password fields do not match")
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
            # replace with your desired URL after successful login
            return redirect('score')
        else:
            # return render(request, 'login.html', {'error_message': 'Invalid username or password'})
            messages.error(request, "Invalid password or username")
            return redirect('login')
    return render(request, 'scoring/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# def match_toss(request):
#     return render(request,'scoring/matchtoss.html')
@login_required(login_url="/login/")
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
    return render(request, ['scoring/team_list.html', 'scoring/make_match.html', 'scoring/tournaments_list.html'], {'tournaments': tournaments})

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
        tournament = Tournament.objects.get(id=tournament_id)
        team1 = Team.objects.get(id=team1_id)
        team2 = Team.objects.get(id=team2_id)
        match_pin = request.POST['matchpin']
        match = Makematch.objects.create(
            tournament_name=tournament, team_1=team1, team_2=team2, match_pin=match_pin)
        # print(tournament,team1,team2)
        return redirect('match_detail', match_id=match.id)
    else:
        tournaments = Tournament.objects.all()
        teams = Team.objects.all()
        context = {'tournaments': tournaments, 'teams': teams}
        return render(request, 'scoring/make_match.html', context)


def match_detail(request, match_id):
    match = Makematch.objects.get(id=match_id)
    context = {'match': match}
    return render(request, 'scoring/matchtoss.html', context)


def scoring(request, match_id):
    match = Makematch.objects.get(id=match_id)

    team_a = match.team_1
    team_b = match.team_2

    team_a_batters = Batter.objects.filter(match=match, player__team=team_a)
    team_b_batters = Batter.objects.filter(match=match, player__team=team_b)
    team_a_bowlers = Batter.objects.filter(match=match, player__team=team_a)
    team_a_bowlers = Batter.objects.filter(match=match, player__team=team_b)

    tournaments = Tournament.objects.all()
    teams = Team.objects.all()

    context = {'tournaments': tournaments,
               'team_a': team_a,
               'team_b': team_b,
               'match': match,
               'team_a_batters': team_a_batters,
               'team_b_batters': team_b_batters,
               'team_a_bowlers': team_a_bowlers,
               'team_a_bowlers': team_a_bowlers

               }

    return render(request, 'scoring/Scoring.html', context)


def team_page(request):
    return render(request, 'scoring/team_page.html')


def add_player(request,):
   
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_player')
    else:
        form = PlayerForm()

    context = {'form': form}
    return render(request, 'scoring/add_player.html', context)
