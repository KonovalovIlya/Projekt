from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_media.forms import UploadFileForm, DocumentForm, MultiFileForm
from app_media.models import File


def upload_file(request):
    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=file.name, status=200)
    else:
        upload_file_form = UploadFileForm()
    return render(request, 'media/upload_file.html', context={'form': upload_file_form})


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form = DocumentForm
    return render(request, 'media/file_form_upload.html', {'form': form})


def upload_files(request):
    if request.method == 'POST':
        upload_file_form = MultiFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            files = request.FILES.getlist('file_field')
            for f in files:
                instance = File(file=f)
                instance.save()
            return redirect('/')
    else:
        upload_file_form = MultiFileForm()
    return render(request, 'media/upload_files.html', context={'form': upload_file_form})