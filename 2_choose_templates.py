infile = 'template_candidates.prf'

def retrieve_best_matches(infile, similarity, max_evalue):
    matches = 0
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
                idx, code, type, _,_,_,_,first,last,_,seqid,evalue = line_chunks[:12]
                evalue = float(evalue)
                seqid = float(seqid)
                
                # copy line if e-value is below threshold
                if type=='X' and evalue<=max_evalue and seqid>=similarity:
                    fout.write(line)
                    matches+=1
                    
    print ('{} sequences with similarity > {} and e-value < {}'.format(matches, similarity, max_evalue))
    return


matches = retrieve_best_matches(infile, 10, 1e-9)
