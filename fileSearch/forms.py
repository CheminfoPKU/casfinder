from django.forms import ModelForm
from django import forms


class smilesForm(forms.Form):
    smiles = forms.CharField(label = 'INPUT SMILES  ',)
    # class Meta:
    #     model = smiles
    #     fields = ('input',)
    
class uploadFileForm(forms.Form):
    MOL = 'MOL'
    CDX = 'CDX'
    SDF = 'SDF'
    UPLOAD_FILE_TYPE = (
        (MOL,'MDL Molfile'),
        (CDX,'Cdx File'),
        (SDF,'SD File')
    )
    file = forms.FileField()
    upload_file_type = forms.ChoiceField(label = 'File Type:', choices = UPLOAD_FILE_TYPE) 
    