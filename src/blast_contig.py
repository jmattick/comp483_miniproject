#!/usr/bin/python3

import os
import sys

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO

params = sys.argv

assembly = None
log = 'miniProject.log'

for i in range(len(params)-1): #loop through parameters
    if params[i] == '-a' or params[i] == '--assembly':
        assembly = params[i + 1]
    if params[i] == '-l' or params[i] == '--log':
        log = params[i + 1]


if assembly == None:
    print('Error: Invalid input parameters. \nSet assembly directory with -a or --assembly.')
else:
    with open(str(assembly) + 'concatenated_contig.fasta','r') as f:
        contig = list(SeqIO.parse(f, 'fasta'))
    result_handle=NCBIWWW.qblast("blastn","nr",contig[0].seq, entrez_query = "Herpesviridae", hitlist_size = 10) #call blast
    blast_records = list(NCBIXML.parse(result_handle))

    with open(log, 'a') as z:
        z.write('seq_title\talign_len\tnumber_HSPs\ttopHSP_ident\ttopHSP_gaps\ttopHSP_bits\ttopHSP_expect\n')
        for alignment in blast_records[0].alignments:
            z.write(str(alignment.title) + '\t' + str(alignment.length) + '\t' + str(len(alignment.hsps))) 
            hsp = alignment.hsps[0]
            z.write('\t' + str(hsp.identities) + '\t' + str(hsp.gaps) + '\t' + str(hsp.bits) + '\t' + str(hsp.expect) + '\n')


