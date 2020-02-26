#!/usr/bin/python3

from Bio import Entrez #import Entrez
from Bio import SeqIO #import SeqIO
import sys #import sys to use parameters

params = sys.argv #get list of parameters

email = None #initialize email
genome_acc = None #initialize genome accession number
idx_path = None #initialize output path
log_file = None #initialize path to log file

for i in range(len(params)-1): #loop through parameters
    if params[i] == '-e' or params[i] == '--email': #if parameter is email
        email = params[i + 1] #set email
    if params[i] == '-g' or params[i] == '--genome_acc': #if parameter is genome accession number
        genome_acc = params[i+1]
    if params[i] == '-o' or params[i] == '--output': #if parameter is output path
        idx_path = params[i+1]
    if params[i] == '-l' or params[i] == '--log': #if parameter is output path
        log_file = params[i+1]

if log_file == None:
    log_file = 'miniProject.log'

#make sure that parameters are set

if email == None or genome_acc == None or idx_path == None:
    print('Error: Invalid input parameters. \nSet email address with -e or --email.')
else:
    Entrez.email = email #set Entrez email
    handle = Entrez.efetch(db='nucleotide', id=genome_acc, rettype='gbwithparts', retmode='txt') #fetch genbank record with features using genome acc number
    record = SeqIO.read(handle,'gb') #read handle into SeqIO object

    with open(str(idx_path) +'genome.fa','w') as z: #open fasta output file 
        num_CDS = 0 #initialize number of CDS features to 0
        for feature in record.features: #loop through all features in record
            if feature.type == "CDS": #if feature is CDS feature
                z.write('>' + str(feature.qualifiers['protein_id'][0]) + '\n') #set protein_id as fasta name
                z.write(str(feature.location.extract(record).seq) + '\n') #write sequence to file
                num_CDS += 1 #increment CDS count

    with open(log_file,'a') as z: #open miniProject.log file
        z.write('The HCMV genome (' + str(genome_acc) + ') has ' + str(num_CDS) + ' CDS.\n') #ouput number of cds features to log
