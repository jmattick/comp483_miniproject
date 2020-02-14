# COMP483 Mini Project 

# Tools needed:

- fastq-dump
- kallisto

# Retrieving Data:

1. Store list of SRR accession numbers in 'acc_list.txt'
2. Run 'get_fastq.py' to output paired-end fastq files in directory named 'data'
    ```
    python3 get_fastq.py
    ```
3. Store genome accesion number in 'genome_acc.txt'
4. Run 'get_genome_fasta.py' to retrieve all CDS sequences into a file named 'genome.fa'. Use '-e' or '--email' to set email address.
    ```
    python3 get_genome_fasta.py -e name@email.com
    ```
# Kallisto

1. Run 'build_kallisto_index.py' to create an index of the genome in the 'idx' directory
    ```
    python3 build_kallisto_index.py
    ```



