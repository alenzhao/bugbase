# Parse usearch output and map to genes/categories
# 
# Note: --gene_map should be space-separated with gene ID in column 1
#
# usage:
# python parse_usearch_lists.py -i usearch_output.txt -m resfams_category_to_gene_mapping.txt -o img_to_gene_table.txt

import sys
import os
import optparse

def get_opts():
    p = optparse.OptionParser()
    p.add_option("-i", "--input", type="string", \
        default=None, help="Input usearch output file, where IMG was used as query [required].")
    p.add_option("-o", "--output", type="string", \
        default=None, help="Output file [required].")
    p.add_option("-m", "--gene_map", type="string", \
        default=None, help="space separated and have genes in column 1 [required]")
    p.add_option("--verbose", action="store_true", \
        help="Print all output.")
    opts, args = p.parse_args(sys.argv)

    return opts, args

def check_opts(opts):
	if opts.input is None:
		raise ValueError('\n\nPlease include an input file.')
	if opts.output is None:
		raise ValueError('\n\nPlease include an output file.')
	if opts.gene_map is None:
		raise ValueError('\n\nPlease include a gene map.')


def create_bacteria_dict(input_file):
	bacteria_dict = {}
	# For each line in input file strip the lines
	# and split at tabs
	# img_ID are the first column, and the first half of the string
	# gene_ID are the second column
	for line in input_file:
		words = line.strip().split("\t")
		img_ID = words[0].split("_")[0]
		gene_ID = words[1]
	
        # For each line in input_file check to see if
		# the img_ID is in 'bacteria_dict',if not, add it as a set
		# then for that given img_ID add the 
		# gene_ID on that line to the given img_ID set
		if not bacteria_dict.has_key(img_ID):
			bacteria_dict[img_ID] = set()
			bacteria_dict[img_ID] = {}
		if not bacteria_dict[img_ID].has_key(gene_ID):
			bacteria_dict[img_ID][gene_ID] = 0
		bacteria_dict[img_ID][gene_ID] += 1
	return bacteria_dict
    
def get_gene_IDs(gene_map):
	# create a set called gene_ID_set
	# by splitting each line in the gene_map
	# based on spaces and taking the first column as ID
	gene_ID_set = set()
	for columns in gene_map:
		IDs = columns.split(' ')[0]
		IDs = IDs.strip()
		gene_ID_set.add(IDs)
	return gene_ID_set
	
		
def write_header(gene_ID_set, output_file):
	# In the output file write the gene_ID_set
	# with each ID seperated by tabs
	output_file.write('\t')
	for IDs in gene_ID_set:
           output_file.write(IDs + '\t')
	output_file.write('\n')
        
def write_rows(bacteria_dict, gene_ID_set, output_file):
	# For each img_ID in bacteria_dict
    # print the img_ID + tab
    # For each ID in gene_ID within the dict, print:
    # contents of each gene_ID + tab
    # or 0 + tab if not
    for img_ID in bacteria_dict:
		output_file.write(img_ID + '\t')
		for IDs in gene_ID_set:
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
	
    #open gene_map file
	gene_map = open(opts.gene_map, 'r')
        
	# a dict mapping img IDs to a list of gene IDs
	bacteria_dict = create_bacteria_dict(input_file)

    # a set of all gene IDs (no duplicates)
	gene_ID_set = get_gene_IDs(gene_map)
        
    # run the function write_header        
	write_header(gene_ID_set, output_file)
	
	#run the function write_rows
	write_rows(bacteria_dict, gene_ID_set, output_file)
		
	# close the output file
	output_file.close
	      
if __name__ == '__main__':
	opts, args = get_opts()
	check_opts(opts)
	main(opts)	
