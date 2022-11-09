from django.shortcuts import render
from .forms import UploadForm
from .models import Upload
from django.contrib import messages
from django.http import  HttpResponse


# Create your views here.
def upload(request):
    if request.method == 'POST':

        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
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


def pdfView(request, ocrfilepath):
    with open(ocrfilepath, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
        return response