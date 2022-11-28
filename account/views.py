from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def loginUser(request):
    if request.method == 'POST':
        # request.method is a dictionary of all the data in POST
        username = request.POST['username'].lower()
        password = request.POST['password']

        # to check if user exist in database
        try:
            user = User.objects.get(username=username)
        except:
            pass
            # for flashing messages
            # messages.error(request, 'Email doesnt exist')

        # this check password against username in database
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # sets session for user
            login(request, user)
            messages.info(request, 'You are logged in!')
            # if next in the url value so redirect there else to account page
            return redirect(request.GET['next'] if 'next' in request.GET else 'index')
        else:
            messages.error(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'account/login.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')