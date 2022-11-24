from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import Upload
from django.contrib import messages
from django.http import  HttpResponse
from django.http import FileResponse, Http404
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def upload(request):
    if request.user.email == 'dehra-ongc@ongc.co.in':
        if request.method == 'POST':
            form = UploadForm(request.POST, request.FILES)
            files = request.FILES.getlist('pdf')

            if form.is_valid():
                for f in files:
                    file_instance = Upload(pdf=f)
                    file_instance.save()
                    messages.success(request, 'PDF are uploaded succesfully!')
            else:
                messages.error(request, 'Upload only PDFs')
        else:
            form = UploadForm()

        context = {'form': form}
        return render(request, 'ocrFile/upload.html', context)
    
    else:
        return redirect("http://10.205.223.29:9000/ocrfiles/")



def pdfView(request, ocrfilepath):
    # testing
    # ocrfilepath = r'C:\Jimmy\aa.pdf'

    with open(ocrfilepath, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
        print(ocrfilepath)
        return response



def viewer(request, ocrfilepath):
    print(ocrfilepath)
    context = {'ocrfilepath': ocrfilepath}
    #print(ocrfilepath)
    return redirect(pdfView,ocrfilepath)
    return render(request, 'ocrFile/pdf-view.html', context)

