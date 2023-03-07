from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.csrf import csrf_protect
from .models import Tournament,Team,Match

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

from django.shortcuts import render
from .models import Tournament, Team, Match

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
