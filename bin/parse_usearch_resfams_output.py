# Parse usearch output and map to resfams genes/categories
# 
# Note: --resfams_map should be tab-delimited and have resfams category in column 1
# and gene name in column 2
#
# usage:
# python parse_usearch_resfams_output.py -i usearch_output.txt -r resfams_category_to_gene_mapping.txt -o img_to_resfams_table.txt

import sys
import os
import optparse

def get_opts():
    p = optparse.OptionParser()
    p.add_option("-i", "--input", type="string", \
        default=None, help="Input usearch output file, where IMG was used as query [required].")
    p.add_option("-o", "--output", type="string", \
        default=None, help="Output file [required].")
    p.add_option("-r", "--resfams_map", type="string", \
        default=None, help="tab-delimited and have resfams category in column 1 and gene name in column 2 [required]")
    p.add_option("--verbose", action="store_true", \
        help="Print all output.")
    opts, args = p.parse_args(sys.argv)

    return opts, args

def check_opts(opts):
	if opts.input is None:
		raise ValueError('\n\nPlease include an input file.')
	if opts.output is None:
		raise ValueError('\n\nPlease include an output file.')
	if opts.resfams_map is None:
		raise ValueError('\n\nPlease include a resfams map.')


def create_bacteria_dict(input_file):
	bacteria_dict = {}
	# For each line in input file strip the lines
	# and split at tabs
	# img_ID are the first column, and the first half of the string
	# resfams_ID are the second column
	for line in input_file:
		words = line.strip().split("\t")
		img_ID = words[0].split("_")[0]
		resfams_ID = words[1]
	
        # For each line in input_file check to see if
		# the img_ID is in 'genes',if not, add it as a set
		# then for that given img_ID add the 
		# resfams_ID on that line to the given img_ID set
		if not bacteria_dict.has_key(img_ID):
			bacteria_dict[img_ID] = set()
			bacteria_dict[img_ID] = {}
		if not bacteria_dict[img_ID].has_key(resfams_ID):
			bacteria_dict[img_ID][resfams_ID] = 0
		bacteria_dict[img_ID][resfams_ID] += 1
	return bacteria_dict
    
def get_resfams_IDs(resfams_map):
	# create a set called resfams_ID_set
	# by splitting each line in the resfams map
	# based on tabs and taking the second column as IDs
	resfams_ID_set = set()
	for columns in resfams_map:
		IDs = columns.split('\t')[1]
		IDs = IDs.strip()
		resfams_ID_set.add(IDs)
	return resfams_ID_set
	
		
def write_header(resfams_ID_set, output_file):
	# In the output file write the resfams_ID_set
	# with each ID seperated by tabs
	output_file.write('\t')
	for IDs in resfams_ID_set:
           output_file.write(IDs + '\t')
	output_file.write('\n')
        
def write_rows(bacteria_dict, resfams_ID_set, output_file):
	# For each img_ID in bacteria_dict
    # print the img_ID + tab
    # For each ID in resfams_ID within the dict, print:
    # contents of each resfams_ID + tab
    # or 0 + tab if not
    for img_ID in bacteria_dict:
		output_file.write(img_ID + '\t')
		for IDs in resfams_ID_set:
			if IDs in bacteria_dict[img_ID]:
				output_file.write(str(bacteria_dict[img_ID][IDs]) + '\t')
			else:
				output_file.write('0\t')
		output_file.write('\n')          
	 	
def main(opts):
	# open input file
	input_file = open(opts.input, "r")
	
    # create an output file and open it 
	output_file = open(opts.output, "w")
	
    #open resfam_maps file
	resfams_map = open(opts.resfams_map, 'r')
        
	# a dict mapping img IDs to a list of resfams_IDs
	bacteria_dict = create_bacteria_dict(input_file)

    # a set of all resfams IDs (no duplicates)
	resfams_ID_set = get_resfams_IDs(resfams_map)
        
    # run the function write_header        
	write_header(resfams_ID_set, output_file)
	
	#run the function write_rows
	write_rows(bacteria_dict, resfams_ID_set, output_file)
		
	# close the output file
	output_file.close
	      
if __name__ == '__main__':
	opts, args = get_opts()
	check_opts(opts)
	main(opts)	
