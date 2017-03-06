import os
import requests
import subprocess

infile = 'template_candidates.ali'

# Retrieve the pdb codes of the template structures
pdb_codes = []
type_line = None
with open (infile) as fin:
    for i, line in enumerate(fin):
        if '>P1;' in line:
            type_line = i + 1
            pdb_code = line[4:8]
            chain = line[8]
        if i==type_line and 'structure' in line:
            pdb_codes.append(pdb_code)
            pdb_code = None
            chain = None

# Create output directory to hold PDB files if not exist
dirpath = 'pdb'
os.makedirs(dirpath, exist_ok=True)

# Download the files
for pdb_code in list(set(pdb_codes)):

    pdb_code_uppercase = pdb_code.upper()
    url = 'https://files.rcsb.org/download/{}.pdb.gz'.format(pdb_code_uppercase)

    r = requests.get(url, stream=True)

    filename = os.path.join(dirpath, '{}.pdb.gz'.format(pdb_code))
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)

    # unzip the *.pdb.gz file
    cmd = 'gunzip {}'.format(filename)
    subprocess.call(cmd.split())
    
