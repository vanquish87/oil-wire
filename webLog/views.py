from django.shortcuts import render, redirect
import pandas as pd
import matplotlib.pyplot as plt
import lasio
from .forms import UploadFileForm
import os


# Create your views here.

def viewDlis(request):
    print(request.POST)
    context = {}
    return render(request, 'webLog/dlis.html', context)

def createLas(request):
    # deleting existing files
    dir = 'C:\Jimmy\Codeholic\ongc-wire\static\data\science'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    # handling file via ORM
    form = UploadFileForm()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()

        # creating PNG files out of LAS uploads
        las_file = str(request.FILES['file'])
        las = lasio.read(f"C:\Jimmy\Codeholic\ongc-wire\static\data\science\{las_file}")
        well = las.df()

        for i in well.columns:
            well.plot(y=i)
            plt.savefig(f"C:\Jimmy\Codeholic\ongc-wire\static\data\science\{i}.png")

        return redirect('view-LAS')

    context = {'form': form}
    return render(request, 'webLog/create-las.html', context)


def viewLas(request):
    dir = 'C:\Jimmy\Codeholic\ongc-wire\static\data\science'
    files = os.listdir(dir)
    png_files = []
    for file in files:
        if file.endswith('.png'):
            png_files.append(file)

    context = {'png_files': png_files}
    return render(request, 'webLog/view-las.html', context)