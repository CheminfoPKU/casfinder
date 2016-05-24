from django.shortcuts import render,get_object_or_404
from .forms import smilesForm
from django.shortcuts import redirect
from .smilesSearch import smiles2cas
from .models import *
# Create your views here.

def smilesSearch(request):
    if request.method == 'POST':
        form = smilesForm(request.POST)
        if form.is_valid():
            post = form.save()          
            return redirect('fileSearch.views.result', pk=post.pk )
    else:
        form = smilesForm()
    return render(request,'fileSearch/smilesSearch.html',{'form':form})

def result(request, pk):
    compound = get_object_or_404(smiles, pk=pk)
    cas = smiles2cas(compound.input)  
    return render(request, 'fileSearch/result.html',{'cas':cas})
    
def ketcher(request):
    return render(request, 'fileSearch/ketcher.html')
    
def imageSearch(request):
    return render(request, 'fileSearch/imageSearch.html')
    
def fileSearch(request):
    return render(request, 'fileSearch/fileSearch.html')