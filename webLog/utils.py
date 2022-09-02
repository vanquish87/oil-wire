from .models import LogFile, LogColumn
from .forms import LogFileForm
import os
from django.conf import settings
import lasio


# deleting existing files
def delete_files():
    file = LogFile.objects.all()
    file.delete()
    if os.path.isdir(settings.SCIENCE_DIR):
        for f in os.listdir(settings.SCIENCE_DIR):
            os.remove(os.path.join(settings.SCIENCE_DIR, f))


# reading LAS file n saving its columns
def read_LAS(request):
    las_file = str(request.FILES['file'])
    #print(las_file)
    las = lasio.read(os.path.join(settings.SCIENCE_DIR, las_file))
   
    well = las.df()
   

    for i in well.columns:
    
        try:
            
            logfile = LogFile.objects.get(file__contains=str(request.FILES['file']))
          
            column = LogColumn(logfile=logfile, name=str(i))
           
            column.save()
       
        except ValueError as e:
            raise e
    
    return well


