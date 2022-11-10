from django.shortcuts import render
from .forms import UploadForm
from .models import Upload
from django.contrib import messages
from django.http import  HttpResponse
from django.http import FileResponse, Http404


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


# def pdfView(request, ocrfilepath):
#     try:
#         file_response = FileResponse(open(r'C:\Jimmy\Codeholic\ongc-wire\static\sebi-ra.pdf', 'rb'), content_type='application/pdf')
#         file_loc = r'C:\Jimmy\Codeholic\ongc-wire\static\sebi-ra.pdf'
#     except FileNotFoundError:
#         raise Http404()

#     context = {
#         'file_response': file_response,
#         'file_loc': file_loc
#         }
#     return render(request, 'ocrFile/pdf-view.html', context)


def pdfView(request, ocrfilepath):
    # testing
    # ocrfilepath = r'C:\Jimmy\Codeholic\ongc-wire\static\sebi-ra.pdf'

    with open(ocrfilepath, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
        return response


def viewer(request, ocrfilepath):
    context = {'ocrfilepath': ocrfilepath}
    return render(request, 'ocrFile/pdf-view.html', context)

