#!/usr/bin/env python
# Parse prediction tables to make a new table based on desired thresholds
# Output table will yield a PICRUSt input table for all traits set at desired thresholds
# 
# USAGE FROM TERMINAL:
# Different threshold for each category:
# category_coverage.py -i prediction_table_1.txt -T .1  -i prediction_table_2 -T .3 -o output_file.txt
# 
# use the same threshold for all categories:
# category_coverage.py -i prediction_table.txt -t .1 -o output_file.txt

import sys
import os
from os.path import splitext
import argparse
import csv
import gzip

def get_opts():
	p = argparse.ArgumentParser()
	p.add_argument("-i", "--input",
		type=str,
		default=None,
		action="append",
		help="Input prediction file (required].")
	p.add_argument("-t", "--threshold_All",
		type=float,
		default=None,
		help="Threshold value used for all inputs. Enter a number ranging from 0-100.")
	p.add_argument("-T", "--threshold",
		type=float,
		default=None,
		action="append",
		help="Individual threshold value for one input. Enter a number ranging from 0-100.") 
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
	if (args['threshold_All']!=None) and (args['threshold'] != None):
		"\n\nWarning: both threshold_All and individual thresholds were specified. Default behavior uses threshold_all."
	if (args['threshold_All']==None) and (args['threshold'] == None):
		raise ValueError('\n\nPlease specify threshold_All (-t) or individual threshold values (-T).')
	if (args['threshold'] and (len(args['input']) != len(args['threshold']))):
		print args['input']
		print args['threshold']
		raise ValueError('\n\nNumber of input files and thresholds must be the same.')
		
def create_OTU_dict(input_file, threshold):

	OTU_dict = {}
	
	for line in list(input_file)[1:]:

		values = line.strip().split("\t")
		OTU_ID = values[0] 	# OTU_IDs are the first column
		Counts = values[1:]	# Counts for each gene/category are in columns 2 to the end of the file
		Hits = 0
		for count in Counts:
			if float(count)>0: # If the OTU has 1 or more copies of the gene/category, add a 1 to the counter (Hits)
				Hits+=1
		# Count the number of 1s
		Category_Length = len(Counts)	# Count the total number of genes/categories being looked at for a given trait
		Percent_Coverage = (float(Hits) / float(Category_Length)) * 100		# Determine the percent of the category covered
		if Percent_Coverage >= threshold:
			OTU_dict[OTU_ID] = 1	# Add the OTU_ID as a key in the dictionary with a binary (yes/no) value depending on threshold set
		else:
			OTU_dict[OTU_ID] = 0	
	return OTU_dict
	
def write_header(args, output_file):
	output_file.write("OTU_ID")	
	for inputFileName in args['input']:
		header = os.path.basename(inputFileName)
		header = os.path.splitext(header)[0]
		output_file.write("\t" + header) # Write the first line of the output file with the input file names as trait headers
	output_file.write("\n")
	
def write_outputs(dictList, output_file):
	# In a new line, write the OTU ID and the binary (yes/no) coverage for each trait
	otuIDs = set()
	for dicts in dictList: # For each dictionary in the list of trait dictionaries:
		otus = dicts.keys()	# The keys are the OTU IDs
		for otu in otus:	
			otuIDs.add(otu)	# Add each ID to a set of OTU IDs (this will keep only unique OTUs)
	for id in otuIDs:
		output_file.write(str(id)+'\t')	# Write the ID in the output file
		for dicts in dictList:
			output_file.write(str(dicts.get(id, 0)) + '\t')	# Get the value at that ID and write to output. If it doesn't have a value, write 0
		output_file.write('\n')
 	
def main(args, thresholds):

	
	dictList = [] # Make a list of the input_files
	
	for inputFileName, threshold in zip(args['input'], thresholds): # Zip the thresholds and input files as tuples
		inputFile = gzip.open(inputFileName, "rb") # Open the input file
		dictList.append(create_OTU_dict(inputFile, threshold))	# Run create_OTU_dict using the threshold value in that tuple, append that dict to the dict list
	
	output_file = open(args['output'], 'w') # Open the outputfile 	
	write_header(args, output_file)	# Write the output file
	write_outputs(dictList, output_file)
	
	output_file.close # Close the output file
      
if __name__ == '__main__':
	args = get_opts()
	args = vars(args)
	check_args(args)
	if args['threshold_All']:	# If threshold_All exists:
		thresholds = [args['threshold_All'] for input in args['input']] # Make a list of the same threshold for every input file
	else: 
		thresholds = args['threshold'] # If threshold_All doesn't exist, make a list of the individual thresholds 
	main(args, thresholds)
