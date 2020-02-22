#!/usr/bin/python3

import os  #import os
import sys #import sys

params = sys.argv #input parameters

genome_dir = None #initialize path to genome.fastq

for i in range(len(params)-1): #loop through parameters
    if params[i] == '-g' or params[i] == '--genome_dir': #if parameter is genome directory 
        genome_dir = params[i+1]

if genome_dir == None:
    print('Error: Invalid input parameters. \nSet path to directory containing genome fasta file with -g or --genome_dir.')
else:
    os.system('kallisto index -i ' + str(genome_dir) + '/genome.idx ' + str(genome_dir) + 'genome.fa') #run command to build index from genome.fa


