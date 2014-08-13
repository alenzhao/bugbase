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
        default=None, help="Input usearch output file [required].")
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



if __name__ == '__main__':
	opts, args = get_opts()
	check_opts(opts)
	
        # open input file
        input_file = open(opts.input, "r")
        
        # a dict mapping img IDs to a list of resfams_IDs
        genes = {}

        # a dict of all resfams IDs (no duplicates)
        resfams_ID_list = []

        for line in input_file:
            words = line.strip().split("\t")
            img_ID = words[0].split("_")[0]
            resfams_ID = words[1]

            # for each line check to see if
            # the img_ID is in 'genes',if not, add 
            # Then for that given img_ID append
            # resfams_ID on that line for the given img_ID
            if not genes.has_key(img_ID):
                genes[img_ID] = []
            genes[img_ID].append(resfams_ID)

            # for each line check if resfams_ID 
            # is in resfams_ID_list, if not, add
            if not resfams_ID in resfams_ID_list:
                resfams_ID_list.append(resfams_ID)

        # create an output file and open it 
        output_file = open(opts.output, "w")
        
        # in the output file write the resfams_ID_list
        # with each ID seperated by tabs
        for resfams_ID in resfams_ID_list:
           output_file.write(resfams_ID + "\t")

        # for each img_ID in genes
        # print a new line with the ID and tab
        # for each resfams_ID print:
        # 1 + tab if present in genes[img_ID]
        # or 0 + tab if not present
        for img_ID in genes:
            output_file.write("\n" + img_ID + "\t")
            for resfams_ID in resfams_ID_list:
                if resfams_ID in genes[img_ID]:
                    output_file.write("1\t")
                else:
                    output_file.write("0\t")

        # close the output file
        output_file.close
