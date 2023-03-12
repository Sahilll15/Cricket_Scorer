from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Tournament,Team
from .forms import TournamentForms,TeamForms

# from django.views.decorators.csrf import csrf_protect
# from .models import Tournament,Team,Match

# Create your views here.
def signup(request):
    
    if request.method=='POST':
        uname=request.POST.get('username')
        uemail=request.POST.get('email')
        upassword=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        

        if upassword!=confirm_password:
            return HttpResponse("The passwords in the two password fields do not match")
        else:

            my_user=User.objects.create_user(username=uname,email=uemail,password=upassword)
            my_user.save()
            # return HttpResponse("User has been Created succesfully!")
            return redirect('login')
            # print(uname,uemail,upassword,confirm_password)

    
    return render(request,'scoring/signup.html')




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('score')  # replace with your desired URL after successful login
        else:
            # return render(request, 'login.html', {'error_message': 'Invalid username or password'})
            return HttpResponse("Invalid password or username")
    return render(request, 'scoring/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


    

def match_toss(request):
    return render(request,'scoring/matchtoss.html')

def score(request):
    return render(request,'scoring/score.html')
    # return HttpResponse("You are at the score page")

def scoring(request):
    return render(request,'scoring/Scoring.html')


def home(request):
    return HttpResponse("You are at the home page")


# start scoring button
def entermatch(request):
    return render(request,'scoring/entermatch.html')


def make_match(request):
    tournaments = Tournament.objects.all()

    if request.method == 'POST':
        tournament_id = request.POST.get('tournament')
        team1_id = request.POST.get('team1')
        team2_id = request.POST.get('team2')
        pin = request.POST.get('pin')
        team1 = Team.objects.get(id=team1_id)
        team2 = Team.objects.get(id=team2_id)
        match = Match(team1=team1, team2=team2, pin=pin)
        match.save()
        # redirect to a success page or show a success message

    context = {
        'tournaments': tournaments,
        'teams': None, # will be updated via AJAX based on selected tournament
    }
    return render(request,'scoring/make_match.html',context) 


def tournament_list(request):
    tournaments = Tournament.objects.all()
    return render(request, 'scoring/tournament_list.html', {'tournaments': tournaments})



def tournament_create(request):
    if request.method == 'POST':
        form = TournamentForms(request.POST)
        if form.is_valid():
            tournament = form.save(commit=False)
            selected_teams = request.POST.getlist('teams')
            tournament.save()
            form.save_m2m()
            for team_id in selected_teams:
                team = Team.objects.get(id=team_id)
                tournament.teams.add(team)
            return redirect('tournament_details', pk=tournament.pk)
    else:
        form = TournamentForms()
        teams = Team.objects.all()
        return render(request, 'scoring/tournament_form.html', {'form': form, 'title': 'Create Tournament', 'teams': teams})

def tournament_detail(request, pk):
    tournament = Tournament.objects.get(pk=pk)
    teams = tournament.teams.all()
    return render(request, 'scoring/tournament_details.html', {'tournament': tournament, 'teams': teams})


def tournament_update(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    if request.method == 'POST':
        form = TournamentForms(request.POST, instance=tournament)
        if form.is_valid():
            tournament = form.save(commit=False)
            selected_teams = request.POST.getlist('teams')
            tournament.save()
            form.save_m2m()
            tournament.teams.clear()
            for team_id in selected_teams:
                team = Team.objects.get(id=team_id)
                tournament.teams.add(team)
            return redirect('tournament_details', pk=tournament.pk)
    else:
        form = TournamentForms(instance=tournament)
        teams = Team.objects.all()
        selected_teams = tournament.teams.all()
        return render(request, 'scoring/tournament_form.html', {'form': form, 'title': 'Update Tournament', 'teams': teams, 'selected_teams': selected_teams})


def create_team(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    if request.method == 'POST':
        form = TeamForms(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.tournament = tournament
            team.save()
            return redirect('tournament_details', pk=tournament_id)
    else:
        form = TeamForms()
    return render(request, 'scoring/team_form.html', {'form': form, 'tournament': tournament})

def edit_team(request, tournament_id, team_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        form = TeamForms(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('tournament_details', pk=tournament_id)
    else:
        form = TeamForms(instance=team)
    return render(request, 'scoring/team_form.html', {'form': form, 'tournament': tournament})
