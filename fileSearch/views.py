from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from .forms import smilesForm,uploadFileForm,uploadImageForm
from django.shortcuts import redirect
from .smilesSearch import smiles2cas
from .handleUploadFile import handleUploadFile
from .models import *
import json
# Create your views here.

def smilesSearch(request):
    if request.method == 'POST':
        form = smilesForm(request.POST)
        if form.is_valid():
            smiles = form.cleaned_data['smiles']
            cas = smiles2cas(smiles)                      
            return render(request,'fileSearch/result.html',{'cas':cas})
    else:
        form = smilesForm()
    return render(request,'fileSearch/smilesSearch.html',{'form':form})
    
def ketcher(request):
    if request.method == 'POST':
        smiles = request.POST.get('smiles')
        cas = smiles2cas(smiles) 
        return render(request, 'fileSearch/result.html',{'cas':cas})
    else:
        return render(request,'fileSearch/ketcher.html')   
    
def imageSearch(request):
    if request.method == 'POST':
        # form = uploadImageForm(request.FILES)       
        image = handleUploadFile(request.FILES('file'))
            # smiles = image2smiles(image)
            # cas = smiles2cas(smiles)
        cas = 'test'
        return render(request,'fileSearch/result.html',{'cas':cas})
    else:
        form = uploadImageForm()
    return render(request, 'fileSearch/imageSearch.html', {'form': form})
    # return render(request, 'fileSearch/ketcher.html') 
    
def fileSearch(request):
    if request.method == 'POST':
        form = uploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            smiles = handleUploadFile(request.FILES['file'])
            cas = smiles2cas(smiles)
            return render(request,'fileSearch/result.html',{'cas':cas})
    else:
        form = uploadFileForm()
    return render(request, 'fileSearch/fileSearch.html', {'form': form})