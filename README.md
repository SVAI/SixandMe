#Ranking Mutations

##Objective:
* identify and rank mutations in NF2

##Introduction:
###Understanding VCF data
Samples: The genetic data provided comprised of genetic data from three different samples.
* OF_010116NF2_a : patient’s tumor sample 
* OF_112015SJIA_2: patient’s blood sample 
* NF2_XY_s: patient's sibling's blood sample

The data collected for these samples were stored in VCF files. The important columns to note are:
* SAMPLE : patient's tumor/ patient's blood/ sibling's blood
* CHROM	: the chromosome number. Human cells have 23 pairs of chromosomes (22 pairs of autosomes and one pair of sex chromosomes), giving a total of 46 per cell. 
* POS	: position on the chromosome
* REF	: the REF refers to the SNP of a reference genome (that of a Mormon lady's, which is used for quality control) 
A single-nucleotide polymorphism (SNP, pronounced snip) is a DNA sequence variation occurring when a single nucleotide adenine (A), thymine (T), cytosine (C), or guanine (G]) in the genome (or other shared sequence) differs between members of a species or paired chromosomes in an individual. For example, two sequenced DNA fragments from different individuals, AAGCCTA to AAGCTTA, contain a difference in a single nucleotide. In this case we say that there are two alleles: C and T. 
* ALT : the sample SNP is campared with reference to the REF SNP. If there were any differences, it would appear in the ALT column. 

For example:
CHROM POS ID    REF ALT   QUAL FILTER INFO
20     3   .     C   CTAG  .    PASS DP=100

The reference has a Cytosine at chromosome 20, position 3. The sample has CTAG at that same position, which indicates an insertion mutation since the reference base C is being replaced by C [the reference base] plus three insertion bases TAG.

To see how other mutations are represented in the VCF data, read https://samtools.github.io/hts-specs/VCFv4.3.pdf

##Method
1. Created a script(separate_files.py) that isolated the chromosome positions that were different from the references (i.e. did not have a GT of 0/0). This resulted in three smaller, more manageable files - 
* normal.csv 
* tumor.csv
* brother.csv
2. Created a script(diff.py) that compares normal.csv to tumor.csv.
