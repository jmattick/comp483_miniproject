#!/usr/bin/python3

import os #import os
import sys #import sys

params = sys.argv #get parameters

genome = None #initialize genome inxex name
output = None #initializes output directory
fastq_dir = None #initializes fastq directory

for i in range(len(params)-1):
    if params[i] == '-g' or params[i] == '--genome_index':
        genome = params[i+1]
    if params[i] == '-o' or params[i] == '--output_directory':
        output = params[i+1]
    if params[i] == '-f' or params[i] == '--fastq_directory':
        fastq_dir = params[i+1]

if genome == None or output == None or fastq_dir == None:
    print('Error: Invalid input parameters. \nSet path to genome index  with -g or --genome_fasta.\nSet output path  with -o or --output_name.\nSet path to fastq directory with -f or --fastq_directory.')
else:

    for file in os.listdir(str(fastq_dir)): #loop through files in data directory
        if file.endswith('_1.fastq'): #if file is first read in pair
            base = file.split('_1.fastq')[0] #get basename of file
            r1 = str(fastq_dir) + str(base) + '_1.fastq' #path to read 1
            r2 = str(fastq_dir) + str(base) + '_2.fastq' #path to read 2
            os.system('bowtie2 --threads 4 --quiet -x ' + str(genome) + ' -1 ' + str(r1) + ' -2 ' + str(r2) + ' --al-conc ' + str(output)  + str(base) + '.fastq')
        

