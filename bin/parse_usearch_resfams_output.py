# Parse usearch output and map to RESFAMS genes/categories
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
    p.add_option("-r" "--resfams_map", type="string", \
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
	
	print "Hello world"