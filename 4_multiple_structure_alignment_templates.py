from modeller import *
import modeller.salign

log.verbose()
env = environ()
env.io.atom_files_directory = ['pdb']

def get_pdbcode_chain(prffile):
    mylist = []
    with open(prffile, 'r') as fin:
        for line in fin:
            if line[0]!='#':
                line_chunks = line.split()
                pdb_code = line_chunks[1][0:4]
                chain = line_chunks[1][4]
                type = line_chunks[2]
                first = line_chunks[7]
                last = line_chunks[8]
                if type=='X':
                    mylist.append((pdb_code, chain, first, last))
    return mylist

pdb_chain = get_pdbcode_chain('template_candidates.prf.filtered')

# add in P22
pdb_chain.append(('2anx', 'A', 'FIRST', 'LAST'))
#m = model(env, file='2anx')
#aln.append_model(m, atom_files='2anx', align_codes='P22/1-146')

# add in SpmX
pdb_chain.append(('spmx', 'A', 'FIRST', 'LAST'))
#m = model(env, file='spmx')
#aln.append_model(m, atom_files='spmx', align_codes='SpmX')




aln = alignment(env)
for i in pdb_chain:
    pdb, chain, first, last = i

    # read in partial pdb --- just the chain
    m = model(env, file=pdb, model_segment=('FIRST:{}'.format(chain), 'LAST:{}'.format(chain)))

    try:
        # retrieve resids from residue indices
        residues = m.residue_range(int(first)-1, int(last)-1)
        resid_0, resid_1 = [residues[0].num, residues[-1].num]

        # read pdb segment
        start = '{}:{}'.format(resid_0, chain)
        stop  = '{}:{}'.format(resid_1, chain)
        m = model(env, file=pdb, model_segment=(start, stop))
    except:
        pass

    aln.append_model(m, atom_files=pdb, align_codes=pdb+chain)

# determine best structural alignment
modeller.salign.iterative_structural_align(aln)

# save the aligned pdbs
for i, mdl in enumerate(aln):
    pdb, chain, first, last = pdb_chain[i]
    mdl.write(pdb+'.malign.pdb')

# write the (structure-based) sequence alignments to file
aln.write(file='templates_aligned.ali', alignment_format='PIR')

# write the family tree to file
aln.compare_structures()  # calculates RMS etc between structures
aln.id_table(matrix_file='family.mat')
env.dendrogram(matrix_file='family.mat', cluster_cut=-1.0)
