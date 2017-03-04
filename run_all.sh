# 0. start with sequences and align the sequences to each other


# 1. get template candidates
#python 1_find_homologues.py > 1_get_homologues.log

# 2. obtain pdbs
#python 2_get_pdbs.py

# 3. narrow down template candidates based on evalue
# python 3_choose_templates.py

# 4. perform iterative structural alignment of templates
# python 4_multiple_structure_alignment_templates.py > 4_malign.log

# 5. view the aligned templates in VMD
# vmd -e 5_view_malign.tcl


#####
# pairwise block align templates against 2anx and spmx
# pairwise block align templates/2anx/spmx against targets


# 6. align the target sequence to the templates
# python 6_align_target_templates.py > 6_align_target_templates.log

# 7. manually select templates based on resolution and family tree closeness
# nano 8_build_model.py

# 8. build homology models
# python 8_build_model.py > 8_build_model.log

# 9. final structural alignment
# python 9_align_structures.py > 9_align_structures.log

# 10. view templates and models
# vmd -e 10_view_models.tcl
