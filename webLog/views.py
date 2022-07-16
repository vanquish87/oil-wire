from django.forms import FileField
from django.shortcuts import render, redirect
from numpy import absolute
import pandas as pd
import matplotlib.pyplot as plt
import lasio
from .forms import LogFileForm
import os
from .models import LogFile, LogColumn
from django.conf import settings

import base64
from io import BytesIO


# Create your views here.

def viewDlis(request):
    print(request.POST)
    context = {}
    return render(request, 'webLog/dlis.html', context)

def createLas(request):
    # deleting existing files
    file = LogFile.objects.all()
    file.delete()
    if os.path.isdir(settings.SCIENCE_DIR):
        for f in os.listdir(settings.SCIENCE_DIR):
            os.remove(os.path.join(settings.SCIENCE_DIR, f))

    # handling file via ORM
    form = LogFileForm()
    if request.method == 'POST':
        form = LogFileForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()

        # reading LAS file n saving its columns
        las_file = str(request.FILES['file'])

        las = lasio.read(os.path.join(settings.SCIENCE_DIR, las_file))
        well = las.df()

        for i in well.columns:
            try:
                logfile = LogFile.objects.get(file__contains=str(request.FILES['file']))
                column = LogColumn(logfile=logfile, name=str(i))
                column.save()
            except ValueError as e:
                raise e

        return redirect('view-LAS-image', well.columns[0])

    context = {'form': form}
    return render(request, 'webLog/create-las.html', context)


def viewLas(request, logcolumn_name):
    column = LogColumn.objects.get(name=logcolumn_name)
    logcolumns = LogColumn.objects.filter(logfile__id__contains=column.logfile_id)

    # creating PNG files out of LAS uploads
    logfile = LogFile.objects.get(id=column.logfile_id)

    # absolute path of FileField
    las_file = logfile.file.path

    las = lasio.read(las_file)
    well = las.df()
    well.plot(y=logcolumn_name)
    # import pdb; pdb.set_trace()
    # saving png in tmp file style
    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    png_file = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    context = {'png_file': png_file, 'logcolumns': logcolumns, 'column': column}

    return render(request, 'webLog/view-las.html', context)