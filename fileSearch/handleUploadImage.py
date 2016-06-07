import os
from rdkit import Chem

def handleUploadImage(file_name):    
    # image to mol
    command_cd = '/home/ubuntu/myspaces/env1/mysite/casfinder/media_cdn/uploads'
    command_turn = './imago_console '+ file_name +' -o output.mol'
    os.system(command_cd)
    os.system(command_turn)
    
    # mol to smiles
    m = Chem.MolFromMolFile('/home/ubuntu/myspaces/env1/mysite/casfinder/media_cdn/uploads/output.mol')
    smiles = Chem.MolToSmiles(m)
    return smiles