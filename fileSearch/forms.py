from django.forms import ModelForm
from django import forms


class smilesForm(forms.Form):
    smiles = forms.CharField(label = 'INPUT SMILES  ',)
    
class uploadFileForm(forms.Form):
    MOL = 'MOL'
    CDX = 'CDX'
    # SDF = 'SDF'
    UPLOAD_FILE_TYPE = (
        (MOL,'MDL Molfile'),
        (CDX,'CDX File'),
        # (SDF,'SD File')
    )
    file = forms.FileField()
    upload_file_type = forms.ChoiceField(label = 'File Type:', choices = UPLOAD_FILE_TYPE) 
    
class uploadImageForm(forms.Form):    
    file = forms.FileField()
    
    