from __future__ import print_function
from rdkit import Chem

def handleUploadFile(f):    
    with open('static/media/molecule.txt','w+') as destination:
        for chunk in f.chunks():
           destination.write(chunk)
            # rdkit  
    with open('static/media/molecule.txt','r') as des2:          
        stringWithMolData=des2.read()
        m = Chem.MolFromMolBlock(stringWithMolData)
        smiles = Chem.MolToSmiles(m)
        # print(smiles)
    
    return smiles
    # else:
        # return 'File type Error!'
    