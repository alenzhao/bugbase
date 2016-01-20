#!/usr/bin/env python
# Runs BugBase analysis:
# - creates category coverage plots 
# - predicts phenotype abundance per microbiome sample
# - plots phenotype abundances per treatment group

# USAGE
# Default thresholds, default treatment groups:
# analyze_bugs.py -i otu_table.biom -m mapping_file.txt -c map_column -o output_directory_name 

# Default thresholds, specific treatment groups:
# analyze_bugs.py -i otu_table.biom -m mapping_file.txt -c map_column -g treatment_group_1,treatment_group_2 

# Specific thresholds (specified treatment groups are still an option):
# analyze_bugs.py -i otu_table.biom -m mapping_file.txt -c map_column Analyze_bugs.py -T trait -t trait_threshold  

import sys
import os
import random
import operator
import csv
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
	parser.add_option("-i", "--input_OTU",
		default=None,
		type='string',
		help="OTU table (required)")
	parser.add_option("-m", "--mapping_file",
		default=None,
		type='string',
		help="mapping file (default %default)")
	parser.add_option("-o", "--output",
		default=".",
		type='string',
		help="Output directory (default %default)")
	parser.add_option("-c","--map_column",
		default=None,
		type='string',
		help="name of column that lists treatment groups (default %default)",)
# 	parser.add_option("-T","--trait",
# 		action="append",
# 		default=None,
# 		type='string'
# 		help="trait you would like to set the threshold for",)
	parser.add_option("-t","--threshold",
		default=None,
		type='float',
		help="threshold (0 to 100) you would like to set for the trait listed",)
	parser.add_option("-g","--groups",
		default=None,
		type='string',
		help="treatment groups you would like to plot, separated by commas with no spaces",)
	parser.add_option("-a","--plot_all",
		action="store_true",
		default=False,
		help="Plot all samples without treatment-group seperation and no statistics",)
	parser.add_option("-z","--continuous",
		action="store_true",
		default=False,
		help="Plot data according to a continuous variable",)
	return parser

def run_commands(commands, print_only=False, verbose=True, error_on_fail=True):
    return_vals = []   

    # Run all commands
    for cmd in commands:
        print cmd
        if not print_only:
            proc = Popen(cmd,shell=True,universal_newlines=True,stdout=PIPE,stderr=PIPE)
            stdout, stderr = proc.communicate()

			# If requested, prints all outputs from the program
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
	
 	# Name user inputs
	otu_table = options.input_OTU
	otu_table2 = otu_table.replace(".biom",".txt" )
	
	if options.plot_all is False:
		if options.mapping_file is None:
			raise ValueError('mapping file must be specified')
		else:
			map = options.mapping_file
		if options.map_column is None:
			raise ValueError('column header must be specified')
		else:	
			column = options.map_column
		if options.groups is not None:
			groups = options.groups.split(",")

		# Make sure map column is valid
		with open(map, 'rU') as input_map:
			reader = csv.reader(input_map, delimiter='\t')
			headers = reader.next()
		if column in headers:
			print "\n" + column + " was specified as map column header\n"
		else:
			print "\n" + column + " was specified as map column header\n"
			print "\nERROR: Column header does not exist in mapping file\n"
			print "These are the available column headers:"
			print headers
			sys.exit()
		
		# If continuous is selected, groups cannot be specified
		if options.continuous is True:
			options.groups is None

		# If groups are specified, check they are valid	
		if options.groups is not None:
			groups_avail = []
			with open(map, 'rU') as input_map:
				reader = csv.reader(input_map, delimiter='\t')
				headers = reader.next()
				column_index = headers.index(column)
				for row in reader:
					name = str(row[column_index])
					groups_avail.append(name)		
			for group_defined in groups:
				if group_defined in groups_avail:
					if len(groups) <= 1:
						print "ERROR: a minimum of two groups must be tested\n"
						sys.exit()
				else:
					groups_avail = list(set(groups_avail))
					print "ERROR: Groups specified do not exist in mapping file\n"
					print "These are the groups available under " + column + " header:"
					print groups_avail
					sys.exit()

	# If threshold is user-specified, state what will be used
	if options.threshold is not None:
		print "a user-specified threshold of %s percent will be used for all traits\n" %(options.threshold)
	
	commands = []
			
	# Make directories needed
	if options.output != ".":
		try:
			os.stat(options.output)
		except:
			os.makedirs(options.output)		
	try:
		os.stat(os.path.join(options.output, "category_coverage"))
	except:
		os.makedirs(os.path.join(options.output, "category_coverage"))			
	try:
		os.stat(os.path.join(options.output, "normalized_otu"))
	except:
		os.makedirs(os.path.join(options.output, "normalized_otu"))
	try:
		os.stat(os.path.join(options.output, "prediction_files"))
	except:
		os.makedirs(os.path.join(options.output, "prediction_files"))
	try:
		os.stat(os.path.join(options.output, "predicted_phenotypes"))
	except:
		os.makedirs(os.path.join(options.output, "predicted_phenotypes"))			
   
	# Normalize the OTU_table by 16S copy number
	cmd = "normalize_by_copy_number.py -i " + otu_table + " -o %s/normalized_otu/" %(options.output) + otu_table
	commands.append(cmd)
	
	# Run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)
   		 			
	# Run PICRUSt with OTU table and the treshold tables found in the thresholds directory
 	commands[:] = []
 	thresholds = []
 	files = os.listdir("%s/lib/precalculated_files/" %(bugbase_dir))
	
	for f in files:
 		if f.endswith(".txt.gz"):
 			thresholds.append(f)
 	for t in thresholds:
 		cmd = "predict_metagenomes.py -i %s/normalized_otu/" %(options.output) + otu_table + " -o %s/prediction_files/threshold_predictions/" %(options.output) + t + " -c %s/lib/precalculated_files/thresholds/" %(bugbase_dir) + t + " -f --normalize_by_otu" 
 		commands.append(cmd)
	
	# Run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)
   		 			
   	# For all files as ".txt.gz", move them to ".txt"
 	files = os.listdir("%s/prediction_files/threshold_predictions/" %(options.output))
	for f in files:
		if f.endswith('.txt.gz'):
			sourcefile = os.path.join("%s/prediction_files/threshold_predictions/" %(options.output), f)
			destfile = os.path.splitext(sourcefile)[0]
			os.rename(sourcefile, destfile)
   		 			
	# Make category coverage plots and calculate variance from PICRUSt outputs and map
	commands[:] = []
	OTU_thresholds = []
 	files = os.listdir("%s/prediction_files/threshold_predictions/" %(options.output))
 	for f in files:
 		if f.endswith(".txt"):
 			OTU_thresholds.append(f)
 	if options.plot_all is False:
 		if options.groups is None:
 			for t in OTU_thresholds:
 				cmd = "Rscript %s/bin/trait_coverage_plots.r -i %s/prediction_files/threshold_predictions/" %(bugbase_dir, options.output) + t + " -m " + map + " -c " + column + " -o %s/category_coverage/" %(options.output) + t
 				commands.append(cmd)
 		else:
 			for t in OTU_thresholds:
 				cmd = "Rscript %s/bin/trait_coverage_plots.r -i %s/prediction_files/threshold_predictions/" %(bugbase_dir, options.output) + t + " -m " + map + " -c " + column + " -o %s/category_coverage/" %(options.output) + t + " -g " + ",".join(groups)
 				commands.append(cmd)
 	else:
 		for t in OTU_thresholds:
 			cmd = "Rscript %s/bin/trait_coverage_plots_all.r -i %s/prediction_files/threshold_predictions/" %(bugbase_dir, options.output) + t + " -o %s/category_coverage/" %(options.output) + t
 			commands.append(cmd)

	# Run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)
   
	# Make category coverage tables based on threshold set or from files in category_coverage/
	commands[:] = []
	variance = {}
 	files = os.listdir("%s/category_coverage" %(options.output)) 
 	for f in files:
 		if f.endswith(".txt"): 
 			variance[f] = {} 
 	for v in variance: 
 		var_dict = {} 
 		with open(os.path.join("%s/category_coverage/" %(options.output), v), "r") as inputFile:
 			for line in list(inputFile)[1:]: # for the rows (excluding header) in the input file
 				values = line.strip().split("\t") 
 				threshold = float(values[0]) 	
 				var = float(values[2])	
 				var_dict[threshold] = var 
 			variance[v] = max(var_dict.iteritems(), key=operator.itemgetter(1))[0] # find the greatest variance
 			
 	if options.threshold is None:
 		cmd = "category_coverage.py -o %s/prediction_files/prediction_input.txt " %(options.output)
 		for traitfile,threshold in variance.items():
			traitfile = os.path.join("%s/lib/precalculated_files/" %(bugbase_dir), traitfile)
			if threshold == 0:
				threshold = threshold + 1
			else:
				threshold = threshold
	 		cmd += " -i " + traitfile + ".gz" + " -T " + str(threshold)
 		commands.append(cmd)
 		
 	else:
 		cmd = "category_coverage.py -o %s/prediction_files/prediction_input.txt -t %s" %(options.output, options.threshold)
 		for traitfile,threshold in variance.items():
 			traitfile = os.path.join("%s/lib/precalculated_files/" %(bugbase_dir), traitfile)
 			cmd += " -i " + traitfile + ".gz"
		commands.append(cmd)
		
	# Run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)
   
	# Run PICRUSt with OTU table and the input table
	commands[:] =[]
	cmd = "predict_metagenomes.py -i %s/normalized_otu/" %(options.output) + otu_table + " -o %s/prediction_files/phenotype_predictions.txt -c %s/prediction_files/prediction_input.txt -f --normalize_by_otu"  %(options.output,options.output)
	commands.append(cmd)
	
	# Run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)
	
	# Make trait by OTU and sample tables
	commands[:] =[]
	cmd = "biom convert -i %s/normalized_otu/" %(options.output) + otu_table +  " -o %s/normalized_otu/" %(options.output) + otu_table2 + " -b --table-type \"OTU table\""
	commands.append(cmd)

	# Run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)

	# Make trait by OTU and sample tables
	commands[:] =[]
	cmd = "Rscript %s/bin/traits_OTU_sample.r -i %s/normalized_otu/" %(bugbase_dir, options.output) + otu_table2 + " -T %s/prediction_files/prediction_input.txt -o %s/prediction_files/otu_trait_contributions" %(options.output, options.output)
	commands.append(cmd)

	# Run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)

	# Plot phenotype predictions	
	commands[:] = []
	traits = []
	with open("%s/prediction_files/phenotype_predictions.txt" %(options.output)) as trait_prediction:
		for line in list(trait_prediction)[2:]:
			values = line.strip().split("\t")
			trait = values[0]
			traits.append(trait)
	if options.plot_all is False:
		if options.groups is None:
			if options.continuous is False:		
				for t in traits:
					cmd = "Rscript %s/bin/make-plot.r -T %s/prediction_files/phenotype_predictions.txt -m " %(bugbase_dir, options.output) + map + " -c " + column + " -t " + t  + " -o %s/predicted_phenotypes/" %(options.output)
					commands.append(cmd)
			else:
				for t in traits:
					cmd = "Rscript %s/bin/make-plot.r -T %s/prediction_files/phenotype_predictions.txt -m " %(bugbase_dir, options.output) + map + " -c " + column + " -z -t " + t  + " -o %s/predicted_phenotypes/" %(options.output)
					commands.append(cmd)
		else:
			for t in traits:
				cmd = "Rscript %s/bin/make-plot.r -T %s/prediction_files/phenotype_predictions.txt -m " %(bugbase_dir, options.output) + map + " -c " + column + " -t " + t  + " -o %s/predicted_phenotypes/" %(options.output) + " -G " + ",".join(groups)
				commands.append(cmd)	
	else:
		for t in traits:
			cmd = "Rscript %s/bin/make-plot_all.r -T %s/prediction_files/phenotype_predictions.txt -t " %(bugbase_dir, options.output) + t  + " -o %s/predicted_phenotypes/" %(options.output)
			commands.append(cmd)
			
	# Run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)
	
