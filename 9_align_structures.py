import os
from modeller import *
import modeller.salign

log.verbose()
env = environ()
env.io.atom_files_directory = ['pdb', 'models']

pdb_chain = []
pdb_chain.append(('2o7a', 'A'))
pdb_chain.append(('spmx', 'A'))
pdb_chain.append(('2anv', 'A'))
pdb_chain.append(('3hdf', 'A'))

pdb_chain.append(('SpmX-Pb.B99990001', ''))
pdb_chain.append(('SpmXL-Pb.B99990002', ''))
pdb_chain.append(('SpmXL-Po.B99990009', ''))


aln = alignment(env)
for i in pdb_chain:
    pdb, chain = i
    m = model(env, file=pdb, model_segment=('FIRST:'+chain, 'LAST:'+chain))
    aln.append_model(m, atom_files=pdb, align_codes=pdb+chain)

# determine best structural alignment
modeller.salign.iterative_structural_align(aln)

# save the aligned pdbs
for i, mdl in enumerate(aln):
    pdb, chain = pdb_chain[i]
    outfile = os.path.join('models', pdb+'.final.pdb')
    mdl.write(outfile)
