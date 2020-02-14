#!/usr/bin/python3

import os #import os

SRR = [] #list to store SRR numbers

with open('acc_list.txt', 'r') as f: #open file containing accession numbers
    for line in f:
        SRR.append(line.strip()) #add each accession number to SRR list

base_url = 'https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos2/sra-pub-run-11/' #base url to retrieve sra files

commands = [] #list to store full wget commands

for acc in SRR: #loop through acc numbers
    commands.append('wget -P data/ ' + base_url + str(acc) + '/' + str(acc) + '.1') #gets sra files and stores in data folder

for command in commands:
    os.system(command) #call bash command to retrieve each file
