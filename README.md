# COMP483 Mini Project 

# Software / Tools needed:

- Linux/Unix
- Python3
- Biopython
- fastq-dump
- kallisto

# Retrieving Data:

1. Store list of SRR accession numbers in 'acc_list.txt' file.
2. Run 'get_fastq.py' to output paired-end fastq files into specified directory.
	
	Parameters: 

	- ``a`` or ``--acc_list``: path to input file containing list of accession numbers
	- ``-o`` or ``--output``: path to output directory

	Example:
	```
	 python3 get_fastq.py -a acc_list.txt -o data/
	```
3. Run 'get_genome_fasta.py' to retrieve all CDS sequences into a file named 'genome.fa'.

	Parameters:

	- ``-e`` or ``--email``: email address for Entrez
	- ``-g`` or ``--genome_acc``: genome accession number
	- ``-o`` or ``--output``: output directory for fasta file    

	Example:
	```
	python3 get_genome_fasta.py -e name@email.com -g EF999921 -o idx/
	```
# Kallisto Transcript Quantification:

1. Run 'build_kallisto_index.py' to create an index of the genome

	Parameters:

	- ``-g`` or ``--genome_dir``: path to directory containing genome fasta file

	Example:
	```
	python3 build_kallisto_index.py -g idx/
	```
2. Run 'kallisto_quant.py' to quantify genes using fastq files and genome index.

	Parameters:

	- ``-f`` or ``--fastq_dir``: path to directory containing fastq files
	- ``-g`` or ``--genome_dir``: path to directory containing genome index
	- ``-o`` or ``--output``: path to results output directory 

	Example:
	```
	python3 kallisto_quant.py -f data/ -g idx/ -o results/
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

2. Run 'sleuth_de.R' to identify differentially expressed transcripts. Provide path to sample matrix and output file.

	Example:
	```
	Rscript sleuth_de.R samples.txt sleuth_results.txt
	```

