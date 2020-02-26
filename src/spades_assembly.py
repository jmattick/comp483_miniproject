#!/usr/bin/python3

import os #import os
import sys #import sys

params = sys.argv #input parameters

fastq_dir = None
output = None
log_file = None

for i in range(len(params)-1): #loop through parameters
    if params[i] == '-f' or params[i] == '--fastq_dir': #if parameter is fastq directory
        fastq_dir = params[i + 1] #set email
    if params[i] == '-o' or params[i] == '--output': #if parameter is output
        output = params[i+1]
    if params[i] == '-l' or params[i] == '--log': #if parameter is output path
        log_file = params[i+1]

if log_file == None:
    log_file = 'miniProject.log'

if fastq_dir == None or output == None:
    print('Error: Invalid input parameters. \nSet fastq directory with -f or --fastq_dir.\nSet path to result output directory with -o or --output.')
else:
    fastqs = ''
    pair = 0
    for file in os.listdir(str(fastq_dir)): #loop through files in data directory
        if file.endswith('.1.fastq'): #if file is first read in pair
            pair += 1
            base = file.split('.1.fastq')[0] #get basename of file
            r1 = str(fastq_dir) + str(base) + '.1.fastq' #path to read 1
            r2 = str(fastq_dir) + str(base) + '.2.fastq' #path to read 2
            fastqs = fastqs + ' --pe' + str(pair) + '-1 ' + str(r1) + ' --pe' + str(pair) + '-2 ' + str(r2) 
    
    spades_cmd = 'spades -k 55,77,99,127 -t 2 --only-assembler' + str(fastqs) + ' -o ' + str(output)
    with open(log_file,'a') as z:
        z.write('\n' + str(spades_cmd))
    os.system(spades_cmd)
