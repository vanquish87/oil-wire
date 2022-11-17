from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    context = {}
    return render(request, 'home.html', context)

@login_required(login_url='login')
def sas(request):
    context = {}
    return render(request, 'about-sas.html', context)