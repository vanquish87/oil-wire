from django.shortcuts import render, redirect
import matplotlib.pyplot as plt
# RuntimeError: main thread is not in main loop with Matplotlib
import matplotlib
matplotlib.use('Agg')

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
    print(well.columns.values)

    print(logcolumn_name)
    print(las.curves[logcolumn_name].unit)
    
    
    #for expanding the chartsize
    f,ax=plt.subplots(nrows=1,ncols=6,figsize=(12,8))
    #ax[0].plot(well[logcolumn_name],logs.Depth,color='green')
  
    # Ist Solution

    #df = las.df()
    #df['DEPTH'] = df.index
    #df.plot(x=logcolumn_name, y='DEPTH', c='black', lw=0.5, legend=False, figsize=(7,10))

    #plt.fill_betweenx(df['DEPTH'], df[logcolumn_name], 0, facecolor='green')
    #plt.ylim(4500, 3500)
    #plt.xlim(0,150)
    #plt.title('Plot With a Single Colour Fill to Y-Axis')

    # 3rd solution
    df = las.df()
    df['DEPTH'] = df.index
   # print(df['DEPTH'])
    well=well.reset_index()
    plt.clf()
    #plt.plot(well[logcolumn_name], well.DEPT,lw=.5)
    #plt.plot(well[logcolumn_name], well.DEPT,lw=.5)
    
    plt.plot(df[logcolumn_name], df['DEPTH'],lw=.9)
    plt.fill_betweenx(df['DEPTH'], df[logcolumn_name], 0, facecolor='yellow')


    # Old Solution
    #well.plot(y=logcolumn_name)
    
    #for setting the x & y label
    plt.xlabel(logcolumn_name+" ("+las.curves[logcolumn_name].unit+")", size=20); plt.ylabel("Depth (m)", size=20)
    #plt.title("LAS chart for - " + logcolumn_name, size=20)
    
    plt.grid(True)
    
    
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
            with dlis.load(os.path.join(settings.SCIENCE_DIR, dlis_file)) as (f, *tail):
                # saving all frames
                for i in f.frames:
                    try:
                        logfile = LogFile.objects.get(file__contains=str(request.FILES['file']))
                        frame = Frame(logfile=logfile, name=str(i))
                        frame.save()
                    except ValueError as e:
                        raise e
                
                # get all the frames
                try:
                    frames = Frame.objects.all().filter(logfile=logfile)
                    for frame in frames:
                        # to get - 'FRAME' , '800T'
                        frame_name = str(frame).split('(', )
                        frame_num = frame_name[1].split(')')[0]

                        frame1 = f.object(frame_name[0].upper() , frame_num)
                        # getting curve names
                        curves = frame1.curves()
                        d = curves.dtype
                        for i in d.names:
                            try:
                                column = LogColumn(logfile=logfile, frame_id=frame.id, name=str(i))
                                column.save()
                            except ValueError as e:
                                raise e
                    
                    columns = LogColumn.objects.all().filter(logfile=logfile, frame_id=frames[0].id)
                    # import pdb; pdb.set_trace()
                    return redirect('view-DLIS-image', logfile.id, frames[0].id, columns[3].name )
                                
                except ValueError as e:
                    raise e
                
        else:
            messages.error(request, 'No DLIS file found')

    context = {'form': form}
    return render(request, 'webLog/dlis.html', context)


def viewDLIS(request, logfile_id, frame_id, logcolumn_name):
    column = LogColumn.objects.get(
        logfile_id=logfile_id, 
        frame_id=frame_id, 
        name=logcolumn_name
        )

    graphunit=""
    # creating PNG files out of DLIS uploads
    logfile = LogFile.objects.get(id=column.logfile_id)

    # absolute path of FileField
    dlis_file = logfile.file.path
    with dlis.load(dlis_file) as (f, *tail):
  
        for channel in f.channels:
           if logcolumn_name==channel.name:
            graphunit= channel.units
            
   
       
        # for template purpose frames are called
        frames = Frame.objects.all().filter(logfile=logfile)

        frame = Frame.objects.get(id=frame_id)
        # to get - 'FRAME' , '800T'
        frame_name = str(frame).split('(', )
        frame_num = frame_name[1].split(')')[0]

        frame1 = f.object(frame_name[0].upper() , frame_num)
        # getting curve names
        curves = frame1.curves()
        
        #xlabelg=f.object('CHANNEL', logcolumn_name)
        
        d = curves.dtype
        #print({d.names}.units)
        
        if 'TDEP' in d.names:
            depth = curves['TDEP'] * 0.00254
        elif 'DEPT' in d.names:
            depth = curves['DEPT'] * 0.00254
        
        # to display given column image
        out_image = curves[column.name]
        print(out_image)
        plt.clf()
        f,ax=plt.subplots(nrows=1,ncols=1,figsize=(12,8))
        plt.plot(out_image,depth)
        plt.xlabel(str(logcolumn_name)+" ("+graphunit+")", size=20); plt.ylabel("Depth (m)", size=20)
        #plt.title("LAS chart for - " + logcolumn_name, size=20)
        plt.fill_betweenx(depth,out_image, 0, facecolor='cyan')
        plt.grid(True)
        # plt.show()
        # import pdb; pdb.set_trace()

        # saving png in tmp file style
        tmpfile = BytesIO()
        plt.savefig(tmpfile, format='png')
        png_file = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

        context = {
            'png_file': png_file, 
            'column': column,
            'logfile': logfile,
            'frames': frames,
            }

    return render(request, 'webLog/view-dlis.html', context)