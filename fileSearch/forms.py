from django import forms
from .models import smiles

class smilesForm(forms.ModelForm):

    class Meta:
        model = smiles
        fields = ('input',)