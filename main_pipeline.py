#!/usr/bin/python3

import os #import os
import sys #import sys

params = sys.argv #get parameters

genome = None #initialize genome inxex name
output = None #initializes output directory
samples = None #initializes list containing sample info 
email = None #initializes email
testrun = False #initialize testrun boolean


for i in range(len(params)-1):
    if params[i] == '-g' or params[i] == '--genome':
        genome = params[i+1]
    if params[i] == '-o' or params[i] == '--output_directory':
        output = params[i+1]
    if params[i] == '-s' or params[i] == '--sample_info':
        samples = params[i+1]
    if params[i] == '-e' or params[i] == '--email':
        email = params[i+1]
    if params[i] == '-t' or params[i] == '--testrun':
        testrun = True

#set variables for test run
if testrun == True:
    genome = 'EF999921'
    output = 'testrun_output'
    samples = 'testrun/sample_info.txt'



if genome == None or output == None or samples == None or email == None:
    print('Error: Invalid input parameters. \nSet genome accession number  with -g or --genome.\nSet output path  with -o or --output_directory.\nSet path to sample information file  with -s or --sample_info.\nSet email with -e or --email.')
else:
    #make necesarry directories
    if not os.path.exists(output): #if output directory does not exist
        os.makedirs(output) #make it
    if not os.path.exists(str(output) + 'data/'): #data folder for fastqs
        os.makedirs(str(output) + 'data/')
    if not os.path.exists(str(output) + 'idx/'): #idx folder for genome
        os.makedirs(str(output) + 'idx/')
    if not os.path.exists(str(output) + 'results/'): #store kallisto quant results
        os.makedirs(str(output) + 'results/')
    if not os.path.exists(str(output) + 'filtered_data/'): #data folder for filtered fastqs
        os.makedirs(str(output) + 'filtered_data/')
    if not os.path.exists(str(output) + 'spades_assembly/'): #data folder for filtered fastqs
        os.makedirs(str(output) + 'spades_assembly/')

    #initalize log file
    log = str(output) + 'miniProject.log'
    with open(log, 'w') as z: #will override existing
        z.write('')

    #get sample information
    sample_info = []
    with open(samples, 'r') as f:
        for line in f:
            sample_info.append(line.strip().split('\t'))
    #output files for downstream analysis
    with open(str(output) + 'acc_list.txt', 'w') as z:
        for i in range(1, len(sample_info)):
            z.write(str(sample_info[i][0]) + '\n')
    with open(str(output) + 'sleuth_sample_info.txt', 'w') as z:
        for i in range(0, len(sample_info)):
            z.write(str(sample_info[i][0]) + '\t' + str(sample_info[i][1]) + '\n')
    #get fastq files
    if testrun == False:
        os.system('python3 src/get_fastq.py -a ' + str(output) + ' acc_list.txt -o ' + str(output) + 'data/')

    #get genome fasta
    os.system('python3 src/get_genome_fasta.py -e ' + str(email) + ' -g ' + str(genome) + ' -o ' + str(output) + 'idx/ -l' + str(log))
    
    #build kalliston index
    os.system('python3 src/build_kallisto_index.py -g ' + str(output) + 'idx/')

    #quantify transcripts
    if testrun:
        os.system('python3 src/kallisto_quant.py -f testrun/data/ -g ' + str(output) + 'idx/ -o ' + str(output) + 'results/')
    else:
        os.system('python3 src/kallisto_quant.py -f ' + str(output) + 'data/ -g ' + str(output) + 'idx/ -o ' + str(output) + 'results/')
    
    #Sleuth analysis
    os.system('Rscript src/sleuth_de.R ' + str(output) + 'sleuth_sample_info.txt ' + str(output) + 'sleuth_results.txt ' + str(log))

    #build bowtie2 index
    os.system('python3 src/build_bowtie2_index.py -g ' + str(output) + 'idx/genome.fa -o ' + str(output) + 'idx/' + str(genome))

    #map reads to genome
    os.system('python3 src/mapped_reads_bowtie2.py -f ' + str(output) + 'data/ -g ' + str(output) + 'idx/' + str(genome) + ' -o ' + str(output) + 'filtered_data/') 
    #log the number of reads filtered to file
    def count_reads(path, filtered):
        for file in os.listdir(str(path)): #loop through files in data directory
        if file.endswith('_1.fastq'): #if file is first read in pair
            base = file.split('_1.fastq')[0] #get basename of file
            file2 = str(filtered) + str(base) + '.1.fastq'
            original = 0 #initialize count of reads
            with open(file,'r') as f:
                for line in f:
                    original += 1

            filtered = 0 #initialize count of filtered reads
            with open(file2, 'r') as f:
                for line in f:
                    filtered += 1
            #find name of sample
            for item in sample_info:
                if item[0] == base:
                    name = item[2]
                    break

            #output results
            with open(log, 'a') as z:
                z.write(str(name) + ' had ' + str(original/4) + ' read pairs before Bowtie2 filtering and ' + str(filtered/4) + ' read pairs after.')

    count_reads(str(output) + 'data/', str(output) + 'filtered_data')

    #spades assembly
    os.system('python3 src/spades_assembly.py -f ' + str(output) + 'filtered_data/ -o ' + str(output) + 'spades_assembly/' )

    #generate large contig
    os.system('python3 src/contig_manipulation.py -a ' + str(output) + 'spades_assembly/ -l ' + str(log))

    #blast large contig
    os.system('python3 src_blast_contig.py -a spades_assembly/ -l ' + str(log))





