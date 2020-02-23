#!/usr/bin/python3

import os #import os
import sys #import sys

params = sys.argv #get parameters

genome = None
output = None

for i in range(len(params)-1):
    if params[i] == '-g' or params[i] == '--genome_fasta':
        genome = params[i+1]
    if params[i] == '-o' or params[i] == '--output_name':
        output = params[i+1]

if genome == None or output == None:
    print('Error: Invalid input parameters. \nSet path to genome fasta with -g or --genome_fasta.\nSet output file name  with -o or --output_name.')
else:
    os.system('bowtie2-build ' + str(genome) + ' ' + str(output))
