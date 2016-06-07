from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class smiles(models.Model):
#     input = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.input
        
class uploadImage(models.Model):
#     MOL = 'MOL'
#     CDX = 'CDX'
#     SDF = 'SDF'
#     UPLOAD_FILE_TYPE = (
#         (MOL,'MDL Molfile'),
#         (CDX,'Cdx File'),
#         (SDF,'SDF')
#     )
#     uoload_file_type = models.CharField(max_length = 10, choices = UPLOAD_FILE_TYPE, default = CDX)
    upload_file = models.FileField(upload_to = 'uploads')
    
   