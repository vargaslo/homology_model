infile = 'template_candidates.prf'

def retrieve_best_matches(infile, max_eval):
    matches = []
    outfile = infile + '.filtered'
    with open(infile, 'r') as fin:
      with open(outfile, 'w') as fout:
        for line in fin:

            # copy comment lines directly
            if line[0]=='#':
                fout.write(line)

            # parse non-comment lines
            if line[0]!='#':
                line_chunks = line.split()
                idx, code, type, _,_,_,_,first,last,_,seqid,eval = line_chunks[:12]
                eval = float(eval)
                
                # copy line if e-value is below threshold
                if type=='X' and eval<max_eval:
                    fout.write(line)
    return


matches = retrieve_best_matches(infile, 1e-5)
