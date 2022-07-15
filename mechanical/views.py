from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def equipmentLog(request):
    context = {}
    return render(request, 'mechanical/equipment-log.html', context)


def electricalLog(request):
    context = {}
    return render(request, 'mechanical/electric-log.html', context)