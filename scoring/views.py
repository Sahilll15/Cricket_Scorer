from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.csrf import csrf_protect

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

def make_match(request):
    return render(request,'scoring/make_match.html') 

def match_toss(request):
    return render(request,'scoring/matchtoss.html')

def score(request):
    return render(request,'scoring/score.html')
    # return HttpResponse("You are at the score page")

def scoring(request):
    return render(request,'scoring/Scoring.html')


def home(request):
    return HttpResponse("You are at the home page")




    