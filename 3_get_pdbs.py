import os
import requests
import subprocess

infile = 'template_candidates.prf.filtered'

# Retrieve the pdb codes of the template structures
pdb_codes = []
with open (infile) as fin:
    for line in fin:
        if line[0]!='#':
            line_chunks = line.split()
            if len(line_chunks)==13:
                pdb_code = line_chunks[1][0:4]
                chain = line_chunks[1][4]
                pdb_codes.append(pdb_code)
                pdb_code = None

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
    
