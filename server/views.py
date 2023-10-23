from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse


# Create your views here.


def homeView(request):
    return render(request, 'home.html', )

def signupView(request):
    context = {
            'form':UserCreationForm
    }
    if request.method == 'GET':
        return render(
            request, 
            './user/signup.html', 
            context
        )
    elif request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                )

                user.save()

                login(request, user)                     
                return redirect('taskapp:tasks')
            
            except Exception as e:
                context['error'] = 'We got an error, please tray again later'
                print(e)
                return render(
                    request, 
                    './user/signup.html', 
                    context
                )
        else:
            context['error'] = 'Woops... passwors did not match'
            return render(
                request, 
                './user/signup.html', 
                context
            )
    else: 
        context['error'] = 'Sorry we were unable to understand that'
        return render(
            request, 
            './user/signup.html', 
            context
        )


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    context = {
        'form':AuthenticationForm
    }

    if request.method == 'GET':
        return render(request, './user/login.html', context)
    elif request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            
            if user is None:
                context['error'] = 'Username or password is wrong'
                return render(request, './user/login.html', context)
            else:
                login(request, user)
                return redirect('taskapp:tasks')
        except Exception as e:
            context['error'] = 'something went wrong :s'
            print(e)
            return render(request, './user/login.html', context)
    else:
        context['error'] = 'Sorry we were unable to understand that'
        return render(request, './user/login.html', context)

