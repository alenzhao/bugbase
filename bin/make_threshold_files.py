#!/usr/bin/env python
# Use precalculated files to generate trait presence or absence for each OTU in a range of thresholds (0-100%)
# Output table will yield the threshold file for the trait
# 
# USAGE FROM TERMINAL:
# # make_threshold_files.py -i precalculated_file.txt -o output_file.txt
# 


import sys
import os
from os.path import splitext
import argparse
import csv
import gzip
import collections

def get_opts():
	p = argparse.ArgumentParser()
	p.add_argument("-i", "--input",
		type=str,
		default=None,
		help="Input file (required].")
	p.add_argument("-o", "--output",
		type=str,
        default=None,
        help="Output file [required].")
	args = p.parse_args()
	return args

def check_args(args):
	if  args['input'] is None:
		raise ValueError('\n\nPlease include an input file.')
	if args['output'] is None:
		raise ValueError('\n\nPlease include an output file.')
			
def create_OTU_dict(input_file):
	#define thresholds to use
	thresholds = [0.0,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2,3.4,3.6,3.8,4.0,4.2,4.4,4.6,4.8,5.0,6.0,7.0,8.0,9.0,10.0,15.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0,65.0,70.0,75.0,80.0,85.0,90.0,95.0,100.0]
	otu_dict = {}
	lines = input_file.readlines()[1:]
	for line in lines:
		values = line.strip().split("\t")
		OTU_ID = values[0] 	# OTU_IDs are the first column
		Counts = values[1:]	# Counts for each gene/category are in columns 2 to the end of the file	
		otu_dict[OTU_ID] = {}
		for threshold in thresholds:
			Hits = 0
			otu_dict[OTU_ID].has_key(threshold)
			for count in Counts:
				if float(count)>0: # If the OTU has 1 or more copies of the gene/category, add a 1 to the counter (Hits)
					Hits+=1	
			# Count the number of 1s
			Category_Length = len(Counts)	# Count the total number of genes/categories being looked at for a given trait
			Percent_Coverage = (float(Hits) / float(Category_Length)) * 100		# Determine the percent of the category covered
			if Percent_Coverage >= float(threshold):
				otu_dict[OTU_ID][threshold] = 1	# Add the OTU_ID as a key in the dictionary with a binary (yes/no) value depending on threshold set
			else:
				otu_dict[OTU_ID][threshold] = 0
				
	return otu_dict
	
def write_header(args, output_file):
	output_file.write("OTU_ID	0.0	0.01	0.02	0.03	0.04	0.05	0.06	0.07	0.08	0.09	0.1	0.2	0.3	0.4	0.5	0.6	0.7	0.8	0.9	1.0	1.2	1.4	1.6	1.8	2.0	2.2	2.4	2.6	2.8	3.0	3.2	3.4	3.6	3.8	4.0	4.2	4.4	4.6	4.8	5.0	6.0	7.0	8.0	9.0	10.0	15.0	20.0	25.0	30.0	35.0	40.0	45.0	50.0	55.0	60.0	65.0	70.0	75.0	80.0	85.0	90.0	95.0	100.0")	
		
def write_outputs(otu_dict, output_file):
	# In a new line, write the OTU_ID and the binary (yes/no) coverage for each trait
	otuIDs = set()
	thresholds = [0.0,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2,3.4,3.6,3.8,4.0,4.2,4.4,4.6,4.8,5.0,6.0,7.0,8.0,9.0,10.0,15.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0,65.0,70.0,75.0,80.0,85.0,90.0,95.0,100.0]
	for OTU_ID in otu_dict.keys(): # for each key in the dictionary
		otuIDs.add(OTU_ID)	# Add each id to a set of otu ids (this will keep only unique otus)
	for id in otuIDs:
		output_file.write('\n' + str(id)+ '\t')	# Write the id in the output file
		for threshold_value in thresholds:
			output_file.write(str(otu_dict[id][threshold_value]) + '\t')	# Get the threshold value at that id and write to output

 	
def main(args):
	input_file = open(args['input'], 'r')	
	output_file = open(args['output'], 'w') # Open the outputfile
	otu_dict = create_OTU_dict(input_file) 
	write_header(args, output_file)	# and write the output file
	write_outputs(otu_dict, output_file)
	
	output_file.close # Close the outputfile
      
if __name__ == '__main__':
	args = get_opts()
	args = vars(args)
	check_args(args)
	main(args)
