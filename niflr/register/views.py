from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .forms import UserForm, UserProfileForm
from .models import UserProfil, User

# Create your views here.
session = { 'user_id': None }

def home(request):
    if not request.user.is_authenticated():
        return render(request, 'register/home.html') #### on giving userid session
    else:
        user = request.user
        return render(request, 'register/home.html', { 'user':user, 'user_id': session['user_id'] } )


def myaccount(request):
    user= request.user
    u = UserProfil.objects.get(username=request.user.username)
    return render(request, 'register/account.html', {'user_id': session['user_id'], 'user': user, 'u':u })

def logout_user(request):
    if not request.user.is_authenticated():
        return render(request, 'register/login.html')
    else:
	logout(request)
        return render(request, 'register/home.html')






def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                session['user_id'] = user
                return render(request, 'register/home.html', {'user_id':session['user_id'],'user':user })
            else:
                return render(request, 'register/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'register/login.html', {'error_message': 'Invalid login' })
    return render(request, 'register/login.html' )



def register(request):
    form = UserForm(request.POST or None)
    form2= UserProfileForm(request.POST or None)
    if form.is_valid() and form2.is_valid():                   ################
        user = form.save(commit=False)
        userprofile = form2.save(commit=False)
        userprofile.user = request.user
        userprofile.username = form.cleaned_data['username']
        userprofile.password = form.cleaned_data['password']
        userprofile.email = form.cleaned_data['email']
        userprofile.mobile_number = form2.cleaned_data['mobile_number']
        userprofile.firstname = form2.cleaned_data['firstname']
        userprofile.lastname = form2.cleaned_data['lastname']
	userprofile.birthdate =  form2.cleaned_data.get('birthdate')
        userprofile.set_password(userprofile.password)
        
        userprofile.save()
        user = authenticate(username=userprofile.username, password=userprofile.password )
        
        if user is not None:
            if user.is_active:
                login(request, user)
		#session['user_id'] = user
                return render(request, 'register/home.html', { 'user_id':session['user_id']})
    context = {
        "form": form,
        "form2": form2,
    }
    return render(request, 'register/register.html', context)



        

