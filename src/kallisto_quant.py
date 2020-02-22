#!/usr/bin/python3

import os #import os
import sys #import sys

params = sys.argv #input parameters

fastq_dir = None
idx = None
output = None

for i in range(len(params)-1): #loop through parameters
    if params[i] == '-f' or params[i] == '--fastq_dir': #if parameter is fastq directory
        fastq_dir = params[i + 1] #set email
    if params[i] == '-g' or params[i] == '--genome_acc': #if parameter is genome accession number
        idx = params[i+1]
    if params[i] == '-o' or params[i] == '--output': #if parameter is output path
        output = params[i+1]

if fastq_dir == None or idx == None or output == None:
    print('Error: Invalid input parameters. \nSet fastq directory with -f or --fastq_dir.\nSet path to directory containing genome index with -g or --genome_acc.\nSet path to result output directory with -o or --output.')
else:

    for file in os.listdir(str(fastq_dir)): #loop through files in data directory
        if file.endswith('_1.fastq'): #if file is first read in pair
            base = file.split('_1.fastq')[0] #get basename of file
            r1 = str(fastq_dir) + str(base) + '_1.fastq' #path to read 1
            r2 = str(fastq_dir) + str(base) + '_2.fastq' #path to read 2
            os.system('kallisto quant -i ' + str(idx) + 'genome.idx -b 30 -o ' + str(output) + str(base) + ' ' + str(r1) + ' ' + str(r2)) #call kallisto quant on both paired reads        


        
