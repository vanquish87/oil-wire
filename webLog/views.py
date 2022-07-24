from django.shortcuts import render, redirect
import matplotlib.pyplot as plt
import lasio
from .forms import LogFileForm
from .models import Frame, LogFile, LogColumn
from .utils import delete_files, read_LAS
from django.contrib import messages
from dlisio import dlis

import os
from django.conf import settings

import base64
from io import BytesIO


# Create your views here.
def createLas(request):
    # deleting existing files
    delete_files()
    # handling file via ORM
    form = LogFileForm()
    if request.method == 'POST':
        form = LogFileForm(request.POST, request.FILES)
        if form.is_valid and request.FILES['file'].name.endswith(('.LAS', '.las')):
            form.save()
            # reading LAS file n saving its columns
            well = read_LAS(request)
            return redirect('view-LAS-image', well.columns[0])
        else:
            messages.error(request, 'No LAS file found')

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
    # saving png in tmp file style
    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    png_file = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    context = {'png_file': png_file, 'logcolumns': logcolumns, 'column': column}

    return render(request, 'webLog/view-las.html', context)


def createDlis(request):
    # deleting existing files
    delete_files()
    # handling file via ORM
    form = LogFileForm()
    if request.method == 'POST':
        form = LogFileForm(request.POST, request.FILES)
        if form.is_valid and request.FILES['file'].name.endswith(('.DLIS', '.dlis')):
            form.save()
            # reading DLIS Files
            dlis_file = str(request.FILES['file'])
            # import pdb; pdb.set_trace()
            with dlis.load(os.path.join(settings.SCIENCE_DIR, dlis_file)) as (f, *tail):
                for i in f.frames:
                    try:
                        logfile = LogFile.objects.get(file__contains=str(request.FILES['file']))
                        frame = Frame(logfile=logfile, name=str(i))
                        frame.save()
                        # get all the frames
                        frames = Frame.objects.get(logfile=logfile).all()
                        # import pdb; pdb.set_trace()


                    except ValueError as e:
                        raise e
                    # frame1 = f.object('FRAME' , '800T')

        else:
            messages.error(request, 'No DLIS file found')

    context = {'form': form}
    return render(request, 'webLog/dlis.html', context)