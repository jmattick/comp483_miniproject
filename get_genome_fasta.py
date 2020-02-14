#!/usr/bin/python3

from Bio import Entrez #import Entrez
from Bio import SeqIO #import SeqIO
import sys #import sys to use parameters

params = sys.argv #get list of parameters

email = '' #initialize email

for i in range(len(params)-1): #loop through parameters
    if params[i] == '-e' or params[i] == '--email': #if parameter is email
        email = params[i + 1] #set email
        break #end loop

#make sure that email set
while True:
    try: #if email is not empty break loop
        email != ''
        break
    except ValueError: #else raise ValueError
        print('no valid email address') #output error message

Entrez.email = email #set Entrez email

with open('genome_acc.txt','r') as f: #get genome accession number
    genome_acc = f.readline().strip() #store in variable

handle = Entrez.efetch(db='nucleotide', id=genome_acc, rettype='gbwithparts', retmode='txt') #fetch genbank record with features using genome acc number
record = SeqIO.read(handle,'gb') #read handle into SeqIO object

with open('idx/genome.fa','w') as z: #open fasta output file 
    num_CDS = 0 #initialize number of CDS features to 0
    for feature in record.features: #loop through all features in record
        if feature.type == "CDS": #if feature is CDS feature
            z.write('> ' + str(feature.qualifiers['protein_id'][0]) + '\n') #set protein_id as fasta name
            z.write(str(feature.location.extract(record).seq) + '\n') #write sequence to file
            num_CDS += 1 #increment CDS count

with open('miniProject.log','a') as z: #open miniProject.log file
    z.write('The HCMV genome (' + str(genome_acc) + ') has ' + str(num_CDS) + ' CDS.\n') #ouput number of cds features to log
