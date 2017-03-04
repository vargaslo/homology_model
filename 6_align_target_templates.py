# align2d/align using salign

# parameters to be input by the user
# 1.  gap_penalties_1d
# 2.  gap_penalties_2d
# 3.  input alignment file

from modeller import *
log.verbose()
env = environ()
env.io.atom_files_directory = ['pdb']

aln = alignment(env)

# templates
aln.append(file='templates_aligned.ali', align_codes='all')
templates_block = len(aln)

# target
aln.append(file='SpmXandFriends.pir', align_codes='all')

# align target sequence to template structures
#aln.align2d()
aln.salign(rr_file='$(LIB)/as1.sim.mat',  # Substitution matrix used
           output='',
#           max_gap_length=30,
           gap_function=True,              # If False then align2d not done
           align_block=templates_block,
           align_what='BLOCK',
           alignment_type='PAIRWISE',
           feature_weights=(1., 0., 0., 0., 0., 0.),
           gap_penalties_1d=(-100, 0),
           gap_penalties_2d=(3.5, 3.5, 3.5, 0.2, 4.0, 6.5, 2.0, 0.0, 0.0),
           # d.p. score matrix
           #output_weights_file='salign.mtx'
           similarity_flag=True)   # Ensuring that the dynamic programming
                                   # matrix is not scaled to a difference matrix

aln.write(file='target-templates.ali', alignment_format='PIR')
