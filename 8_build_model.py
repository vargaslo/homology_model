import os
import shutil
from modeller import *
from modeller.automodel import *
#from modeller import soap_protein_od

env = environ()

aln_file = 'target-templates.ali'

# create directory if it doesnt exist and cd into it
path='models'
os.makedirs(path, exist_ok=True)
shutil.copyfile(aln_file, os.path.join(path, aln_file))
os.chdir(path)

# directories for input atom files
env.io.atom_files_directory = ['../pdb']

# which chains to use as templates
pdb_chain = []
pdb_chain.append(('2o7a', 'A'))
pdb_chain.append(('spmx', 'A'))
pdb_chain.append(('2anv', 'A'))
pdb_chain.append(('3hdf', 'A'))
knowns = [i[0]+i[1] for i in pdb_chain]

# generate models
model_codes = ['SpmX-Pb', 'SpmXL-Pb', 'SpmXL-Po']
out = {}
for var, code in zip(range(len(model_codes)), model_codes):
    out[var] = automodel(env, alnfile=aln_file,
              sequence=code,
              knowns=knowns,
              assess_methods=(assess.DOPE,
                              #soap_protein_od.Scorer(),
                              assess.GA341))

    out[var].starting_model = 1
    out[var].ending_model = 2
    out[var].make()

    out[var].rename_segments(segment_ids=('M'), renumber_residues=(89))


#for i,m in out.items():
#    m.rename_segments(segment_ids=('M'), renumber_residues=(89))
#    m.write(''.format(k))
