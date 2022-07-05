from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def equipmentLog(request):
    context = {}
    return render(request, 'mechanical/web-form.html', context)