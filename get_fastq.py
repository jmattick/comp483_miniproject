#!/usr/bin/python3

import os #import os

SRR = [] #list to store SRR numbers

with open('acc_list.txt', 'r') as f: #open file containing accession numbers
    for line in f:
        SRR.append(line.strip()) #add each accession number to SRR list

for acc in SRR: #loop through acc numbers
    os.system('fastq-dump -O data/ -I --split-files ' + str(acc)) #call fastq-dump command to output fastq files in data folder
