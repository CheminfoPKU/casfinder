from __future__ import print_function
from rdkit import Chem

def handleUploadFile(f):    
    # if type == 'SDF':
    #     mol = 
    # if type == 'MOL':
    mol = Chem.MolFromMolFile(f)
    smiles = Chem.MolToSmiles(mol)
    return smiles
    # else:
        # return 'File type Error!'
    