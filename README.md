# COMP483 Mini Project 

# Software / Tools needed:

- Linux/Unix
- Python3
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
# Kallisto Transcript Quantification:

1. Run 'build_kallisto_index.py' to create an index of the genome in the 'idx' directory.
    ```
    python3 build_kallisto_index.py
    ```
2. Run 'kallisto_quant.py' to quantify genes using fastq files in data directory and genome index in idx directory. Results will be output to 'results' directory.
    ```
    python3 kallisto_quant.py
    ```
# Sleuth Differential Analysis:

1. Create 'samples.txt' tab delimited file containing sample names, conditions, and paths to kallisto output. Example:

    ```
    sample	condition	path
    SRR1	cond1	results/SRR1
    SRR2	cond2	results/SRR2
    SRR3	cond1	results/SRR3
    SRR4	cond2	results/SRR4
    ```

2. Run 'sleuth_de.R' to identify differentially expressed transcripts. Sleuth results with be output to sleuth_results.txt.
    ```
    Rscript sleuth_de.R
    ```

