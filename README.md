# COMP483 Mini Project 

# Description

This pipeline is designed to process paired-end Human cytomegalovirus RNAseq data from SRA using only accession numbers and user-provided sample information as input. 

# Software / Tools needed:

- Linux/Unix
- Python3
- Biopython
- fastq-dump
- kallisto
- R
- bowtie2
- SPAdes

# Run Pipeline:

1. Create a tab-delimited file containing sample information in the order of the following example and include the headers "sample, condition, name". The first column should contain the SRA accession numbers for each sample. The second column should describe the condition being compared. The final column should include the name or description of the sample.
	```
	sample	condition	name
	SRR5660030	2dpi	Donor 1 (2dpi)
	SRR5660033	6dpi	Donor 1 (6dpi)
	SRR5660044	2dpi	Donor 3 (2dpi)
	SRR5660045	6dpi	Donor 3 (6dpi)
	```

2. Run 'main_pipeline.py' to run through the entire pipeline.
	
	Parameters:

	- ``-s`` or ``--sample_info``: path to tab-delimited file created in step 1
	- ``-g`` or ``--genome``: genome accession number
	- ``-o`` or ``--output_directory``: directory for output files
	- ``-e`` or ``--email``: email address for use with Entrez
	- ``-t`` or ``--testrun``: include to run pipeline on test dataset

	Example of running pipeline on entire dataset:
	```
	python3 main_pipeline.py -s sample_info.txt -g EF999921 -o pipeline_results/ -e name@email.com
	```

	Example of running pipeline on test dataset (results output to testrun_output directory):
	```
	python3 main_pipeline.py -t -e name@email.com
	```

---

# Information on running each step separately:
	
# Retrieving Data:

1. Store list of SRR accession numbers in 'acc_list.txt' file.
2. Run 'get_fastq.py' to output paired-end fastq files into specified directory.
	
	Parameters: 

	- ``-a`` or ``--acc_list``: path to input file containing list of accession numbers
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
	- ``-l`` or ``--log_file``: log output file	

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
# Sleuth Differential Expression Analysis:

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
	Rscript sleuth_de.R samples.txt sleuth_results.txt file.log
	```
# Filter Host Reads using Bowtie2:

1. Run 'build_bowtie2_index.py' to build bowtie2 index. 

	Parameters:
	
	- ``-g`` or ``--genome_fasta``: path to genome fasta file
	- ``-o`` or ``--output_name``: output path and index name

	Example:
	```
	python3 build_bowtie2_index.py -g idx/genome.fa -o idx/EF999921
	```
2. Run 'mapped_reads_bowtie2.py' to get fastq files for reads that map to the genome. 

	Parameters:
	
	- ``-g`` or ``--genome_directory``: path to genome directory including index name
	- ``-f`` or ``--fastq_directory``: path to fastq directory
	- ``-o`` or ``--output``: path to output filtered fastq files

	Example:
	```
	python3 mapped_reads_bowtie2.py -f data/ -g idx/EF999921 -o filtered_data/
	```

# Assemble Genome using SPAdes:

1. Run 'spades_assembly.py' on filtered fastq files from bowtie2 output. 

	Parameters:
	
	- ``-f`` or ``--fastq_dir``: path to directory containing filtered reads
	- ``o`` or ``--output``: path to output directory

	Example:
	```
	python3 spades_assembly.py -f filtered_data/ -o spades_assembly 
	```

2. Run 'contig_manipulation.py' to output a concatenated fasta file of all contigs in assembly over 1000bp.

	Parameters:

	- ``-a`` or ``--assembly``: path to SPAdes assembly directory

	Example:
	```
	python3 contig_manipulation.py -a spades_assembly/
	```

# Blast Contig

1. Run 'blast_contig.py' to blast concatenated contig to Herpesviridae nt database.

	Parameters: 
	
	- ``-a`` or ``-assembly``: directory containing concatenated contig file

	Example:
	```
	python3 blast_contig.py -a spades_assembly/
	```

