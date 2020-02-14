#!/usr/bin/python3

import os #import os

for file in os.listdir('data'): #loop through files in data directory
    if file.endswith('_1.fastq'): #if file is first read in pair
        base = file.split('_1.fastq')[0] #get basename of file
        r1 = 'data/' + str(base) + '_1.fastq' #path to read 1
        r2 = 'data/' + str(base) + '_2.fastq' #path to read 2
        os.system('kallisto quant -i idx/genome.idx -o results/' + str(base) + ' ' + str(r1) + ' ' + str(r2)) #call kallisto quant on both paired reads        


        
