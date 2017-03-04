# mod9.15 1_do.py

from modeller import *

log.verbose()
env = environ()

#-- Prepare the input files

which = 'pdb_95'
#which = 'pdball'

#-- Read in the sequence database
sdb = sequence_db(env)
sdb.read(seq_database_file=which+'.pir', seq_database_format='PIR',
         chains_list='ALL', minmax_db_seq_len=(30, 4000), clean_sequences=True)

#-- Write the sequence database in binary form
sdb.write(seq_database_file=which+'.bin', seq_database_format='BINARY',
          chains_list='ALL')

#-- Now, read in the binary database
sdb.read(seq_database_file=which+'.bin', seq_database_format='BINARY',
         chains_list='ALL')

#-- Read in the target sequence/alignment
aln = alignment(env)
aln.append(file='SpmXandFriends.pir', alignment_format='PIR', align_codes='ALL')


#-- Convert the input sequence/alignment into
#   profile format
prf = aln.to_profile()

#-- Scan sequence database to pick up homologous sequences
prf.build(sdb, matrix_offset=-450, rr_file='${LIB}/blosum62.sim.mat',
          gap_penalties_1d=(-500, -50), n_prof_iterations=5,
          check_profile=True, max_aln_evalue=0.01, gaps_in_target=True)

#-- Write out the profile in text format
prf.write(file='template_candidates.prf', profile_format='TEXT')

#-- Convert the profile back to alignment format
aln = prf.to_alignment()

#-- Write out the alignment file
aln.write(file='template_candidates.ali', alignment_format='PIR')

