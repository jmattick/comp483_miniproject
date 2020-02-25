#!/usr/bin/python3

import os #import os
import sys #import sys
from Bio import SeqIO #import seqio

params = sys.argv #input parameters

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
    nnn = '' #initialize n separator
    for i in range(50): nnn+='N' #50 Ns
    with open(str(assembly) + 'contigs.fasta','r') as f: #open contigs.fasta (sorted from longest to shortest)
        contigs = list(SeqIO.parse(f, 'fasta')) #parse as list of Seq objects
    n = 0 #initialize number of contigs over 1000bp
    bp = 0 #initialize number of bps total
    megacontig = '>concatenated_contigs\n' #concatenated contig
    for c in contigs:
        if len(c) > 1000:
            n += 1 #add to num contigs
            bp += len(c) #add to num bp
            megacontig = megacontig + str(nnn) + c.seq #add to contig with separator
    

    with open(log,'a') as z:
        z.write('\nThere are ' + str(n) + ' contigs > 1000 bp in the assembly\n')
        z.write('There are ' + str(bp) + ' bp in the assembly.\n')
        
    with open(str(assembly) + 'concatenated_contig.fasta', 'w') as z:
        z.write(str(megacontig))
