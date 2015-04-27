#!/usr/bin/env python
# Runs BugBase analysis:
# creates category coverage plots 
# predicts traits per sample
# plots microbiome traits per treatment group

# USAGE
# Default thresholds, all treatment groups:
# analyze_bugs.py -i otu_table.txt -m mapping_file.txt -c map_column -o output_directory_name 

# Default thresholds, specific treatment groups:
# analyze_bugs.py -i otu_table.txt -m mapping_file.txt -c map_column -g treatment_groups 

# Specific thresholds (specified treatment groups still an option):
# analyze_bugs.py -i otu_table.txt -m mapping_file.txt -c map_column Analyze_bugs.py -T trait -t trait_threshold  

# category_coverage.py -i precalc_table.txt -t threshold_All (percent of category, 0-100) or -T individual_thresholds (percent of category, 0-100) -o output_file.txt
# trait_coverage_plots.r -s suppress_truncation -t truncation_threshold -c map_column -m map_file  -T threshold_table -G treatment_groups
# make_plots.r -c map_column, -m map_file, -T trait_table, -t trait, -x transform -G groups
# predict_metagenomes.py -i OTU_table.biom -f -c precalc_file.txt --normalize_by_otu

import sys
import os
import random
import operator
from subprocess import Popen, PIPE, STDOUT
from optparse import OptionParser

def make_option_parser():
	parser = OptionParser(usage="usage: %prog [options] filename",
		version="%prog 1.0")
	parser.add_option("-v","--verbose",
   		action="store_true",
		default=False,
		help="Verbose output (default %default)",)
	parser.add_option("-p","--print_only",
		action="store_true",
		default=False,
		help="Only print commands (default %default)",)
	parser.add_option("-s","--suppress_delete",
		action="store_true",
		default=False,
		help="Only print commands for deletion, don't actually delete files (default %default)",)
	parser.add_option("-i", "--input_OTU",
		default=None,
		type='string',
		help="OTU table (required)")
	parser.add_option("-m", "--mapping_file",
		default=None,
		type='string',
		help="mapping file (required)")
	parser.add_option("-o", "--output",
		default=".",
		type='string',
		help="Output directory (default %default)")
	parser.add_option("-c","--map_column",
		default=None,
		type='string',
		help="name of column that lists treatment groups",)
# 	parser.add_option("-T","--trait",
# 		action="append",
# 		default=None,
# 		type='string'
# 		help="trait you would like to set the threshold for",)
# 	parser.add_option("-t","--threshold",
# 		action="append",
# 		default=None,
# 		type='float'
# 		help="threshold (0 to 100) you would like to set for the trait listed",)
# 	parser.add_option("-g","--groups"
# 		default=None,
# 		type='string',
# 		help="treatment groups you would like to plot, separated by commas with no spaces",)
	return parser

def run_commands(commands, print_only=False, verbose=True, error_on_fail=True):
    return_vals = []
    

    # run all commands
    for cmd in commands:
        print cmd
        if not print_only:
            proc = Popen(cmd,shell=True,universal_newlines=True,stdout=PIPE,stderr=PIPE)
            stdout, stderr = proc.communicate()

			# if requested, prints all output from the program
            if verbose:
                print stdout
                print stderr
            if error_on_fail == True and proc.returncode != 0:
                print stdout
                print stderr
                raise ValueError('Command failed: ' + cmd)

            return_vals.append(proc.returncode)
    return(return_vals)
    
if __name__ == '__main__':
	parser = make_option_parser()
	(options, args) = parser.parse_args()
	
	
	if not 'BUGBASE_PATH' in os.environ:
		raise ValueError('BUGBASE_PATH not in system environment variables')
	bugbase_dir = os.environ['BUGBASE_PATH']
	print bugbase_dir
	
	# name user inputs
	otu_table = options.input_OTU
	map = options.mapping_file
	column = options.map_column

	commands = []
	
	# make directories needed
	if options.output != ".":
		try:
			os.stat(options.output)
		except:
			os.makedirs(options.output)			
	try:
		os.stat(os.path.join(options.output, "picrust_thresholds"))
	except:
		os.makedirs(os.path.join(options.output, "picrust_thresholds"))			
	try:
		os.stat(os.path.join(options.output, "threshold_variances"))
	except:
		os.makedirs(os.path.join(options.output, "threshold_variances"))			
	try:
		os.stat(os.path.join(options.output, "picrust_thresholds"))
	except:
		os.makedirs(os.path.join(options.output, "normalized_otu"))			
	
	# run commands
   
	# normalize the OTU_table by 16S copy number
	cmd = "normalize_by_copy_number.py -i " + otu_table + " -o %s/normalized_otu/" %(options.output) + otu_table
	commands.append(cmd)
	
	# run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)
   		 			
	# run PICRUSt with OTU table and the treshold tables found in the thresholds directory
 	commands[:] = []
 	thresholds = []
 	files = os.listdir("%s/lib/precalculated_files/" %(bugbase_dir))
	
	for f in files:
 		if f.endswith(".txt.gz"):
 			thresholds.append(f)
 	for t in thresholds:
 		cmd = "predict_metagenomes.py -i %s/normalized_otu/" %(options.output) + otu_table + " -o %s/picrust_thresholds/" %(options.output) + t + " -c %s/lib/precalculated_files/thresholds/" %(bugbase_dir) + t + " -f --normalize_by_otu" 
 		commands.append(cmd)
	
	# run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)
   		 			
   	# for all files output as ".txt.gz", move them to ".txt"
 	files = os.listdir("%s/picrust_thresholds/" %(options.output))
	for f in files:
		if f.endswith('.txt.gz'):
			sourcefile = os.path.join("%s/picrust_thresholds/" %(options.output), f)
			destfile = os.path.splitext(sourcefile)[0]
			print sourcefile
			print destfile
			print
			
			os.rename(sourcefile, destfile)
   		 			
	# make trait coverage plots and calculate variance from picrust outputs and map
	commands[:] = []
	OTU_thresholds = []
 	files = os.listdir("%s/picrust_thresholds/" %(options.output))
 	for f in files:
 		if f.endswith(".txt"):
 			OTU_thresholds.append(f)
 	for t in OTU_thresholds:
 		cmd = "Rscript %s/bin/trait_coverage_plots.r -i %s/picrust_thresholds/" %(bugbase_dir, options.output) + t + " -m " + map + " -c " + column + " -o %s/threshold_variances/" %(options.output) + t
 		commands.append(cmd)

	# run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)
   
	# make category coverage tables based on threshold table or input  files = os.listdir("threshold_variances/")
	commands[:] = []
	variance = {} # create a dictionary
 	files = os.listdir("%s/threshold_variances" %(options.output)) 
 	for f in files:
 		if f.endswith(".txt"): 
 			variance[f] = {} 
 	for v in variance: 
 		var_dict = {} 
 		with open(os.path.join("%s/threshold_variances/" %(options.output), v), "r") as inputFile:
 			for line in list(inputFile)[1:]: # for the rows (excluding header) in the input file
 				values = line.strip().split("\t") 
 				threshold = float(values[0]) 	
 				var = float(values[2])	
 				var_dict[threshold] = var 
 			variance[v] = max(var_dict.iteritems(), key=operator.itemgetter(1))[0] # find the greatest variance, but it's threshold (key) as the value in the variance dict

# 	cmd = "category_coverage.py -o %s/picrust_input.txt " %(options.output)
#  	for traitfile,threshold in variance.items():
# 		traitfile = os.path.join("%s/picrust_thresholds/" %(options.output), traitfile)
# 	 	cmd += " -i " + traitfile + " -T " + str(threshold)
#  	commands.append(cmd)


	cmd = "category_coverage.py -o %s/picrust_input.txt " %(options.output)
 	for traitfile,threshold in variance.items():

		traitfile = os.path.join("%s/lib/precalculated_files/" %(bugbase_dir), traitfile)

		print traitfile



	 	cmd += " -i " + traitfile + ".gz" + " -T " + str(threshold)
 	commands.append(cmd)
	
	# run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)
   
	# run PICRUSt with OTU table and the input table.
	commands[:] =[]
	cmd = "predict_metagenomes.py -i %s/normalized_otu/" %(options.output) + otu_table + " -o %s/picrust_prediction.txt -c %s/picrust_input.txt -f --normalize_by_otu"  %(options.output,options.output)
	commands.append(cmd)
	
	# run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)
   
	# plot trait predictions	
	commands[:] = []
	traits = []
	with open("%s/picrust_prediction.txt" %(options.output)) as trait_prediction:
		for line in list(trait_prediction)[2:]:
			values = line.strip().split("\t")
			trait = values[0]
			traits.append(trait)
	for t in traits:
		cmd = "Rscript %s/bin/make-plot.r -T %s/picrust_prediction.txt -m " %(bugbase_dir, options.output) + map + " -c " + column + " -t " + t  + " -o %s/" %(options.output)
		commands.append(cmd)
	
	# run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)

	# delete necessary files and directorie
# 	to_remove = [otu_table,map]   
# 	for f in to_remove:
# 		if options.suppress_delete: 
# 			print "rm ",f
# 		else:
# 			try:
# 				os.remove(f)
# 			except OSError:
# 				print "Could not remove file " + f
#     
# 	dir_to_remove = ["normalized_otu/","picrust_thresholds/"]
#     
# 	for f in to_remove:
# 		if options.suppress_delete: 
# 			print "rm ",f
# 		else:
# 			try:
# 				os.remove(f)
# 			except OSError:
# 				print "Could not remove file " + f
# 	if not options.print_only:
# 		for i,cmd in enumerate(commands):
# 			if return_vals[i] != 0:
# 				print "Warning: command",cmd,"had return value",return_vals[i]
