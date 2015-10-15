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

import site
import sys
import os
import random
import operator
import csv
from subprocess import Popen, PIPE, STDOUT
from optparse import OptionParser

# These are the environment paths added by the module:

# Python
os.environ['PATH'] = os.environ['PATH'] + '/soft/python-2.7/bin'

# QIIME
os.environ['PATH'] = os.environ['PATH'] + ':/soft/qiime/1.8.0/precise64/bin'
os.environ['LD_LIBRARY_PATH'] = '/soft/qiime/1.8.0/precise64/lib'
os.environ['PYTHONPATH'] = '/soft/qiime/1.8.0/precise64/lib'

# PyCogent
os.environ['PYTHONPATH'] =  os.environ['PYTHONPATH'] + ':/web/research/bugbase.cs.umn.edu/site-packages/PyCogent-1.5.3'

# PICRUSt
os.environ['PYTHONPATH'] = os.environ['PYTHONPATH'] + ':/web/research/bugbase.cs.umn.edu/picrust'
os.environ['PATH'] = os.environ['PATH'] + ':/web/research/bugbase.cs.umn.edu/picrust/scripts'

# R
os.environ['PATH'] = os.environ['PATH'] + ':/soft/r/3.1.2/linux_x86_64/bin'
os.environ['PATH'] = os.environ['PATH'] + ':/soft/r/3.1.2/linux_x86_64/rstudio-0.98.1087/bin'

# BugBase
os.environ['PATH'] = os.environ['PATH'] + ':/web/research/bugbase.cs.umn.edu/bugbase/bin'
os.environ['BUGBASE_PATH'] = '/web/research/bugbase.cs.umn.edu/bugbase/'

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
		help="mapping file (required)")
	parser.add_option("-o", "--output",
		default=".",
		type='string',
		help="Output directory (default %default)")
	parser.add_option("-c","--map_column",
		default=None,
		type='string',
		help="name of column that lists treatment groups",)
	# parser.add_option("-T","--trait",
	#   action="append",
	#   default=None,
	#   type='string'
	#   help="trait you would like to set the threshold for",)
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
	return parser

def run_commands(commands, print_only=False, verbose=True, error_on_fail=True):
	return_vals = []

	# Run all commands
	for cmd in commands:
		print cmd
		if not print_only:
			proc = Popen(cmd,shell=True,universal_newlines=True,stdout=PIPE,stderr=PIPE)
			stdout, stderr = proc.communicate()

		# If requested, prints all output from the program
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
	otu_table = "/web/research/bugbase.cs.umn.edu/uploads/" + options.input_OTU 
	
	if options.plot_all is False:
		if options.mapping_file is None:
			print "ERROR_MESSAGE]Mapping file must be specified"
		else:
			map = "/web/research/bugbase.cs.umn.edu/uploads/" + options.mapping_file
		if options.map_column is None:
			print "[ERROR_MESSAGE]column header must be specified"
		else:
			column = options.map_column
		if options.groups is not None:
			groups = options.groups.split(",")
 
		# Make sure map column is valid
		with open(map, 'rU') as input_map:
			reader = csv.reader(input_map, delimiter='\t')
			headers = reader.next()
		if column in headers:
			print column + " was specified as map column header\n"
		else:
			print "[ERROR_MESSAGE]Column header specified does not exist in mapping file\n"
			print "[ERROR_MESSAGE]These are the available column headers: "+ ', '.join(headers)
			sys.exit()
		
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
						print "[ERROR_MESSAGE]A minimum of two groups must be tested"
						sys.exit()
				else:
					groups_avail = list(set(groups_avail))
					print "[ERROR_MESSAGE]Groups specified do not exist in mapping file"
					print "[ERROR_MESSAGE]These are the groups available under " + column + " header: " + ', '.join(groups_avail)
					sys.exit()
			
	# If threshold is user-specified, state what will be used
	if options.threshold is not None:
		print "[ERROR_MESSAGE]A user-specified threshold of %s percent will be used for all traits" %(options.threshold)

	commands = []
		 
	# Make directories needed

	output_folder = "/web/research/bugbase.cs.umn.edu/results/" + options.output

	if output_folder != ".":
		try:
			os.stat(output_folder)
		except:
			os.makedirs(output_folder)    
	try:
		os.stat(os.path.join(output_folder, "category_coverage"))
	except:
		os.makedirs(os.path.join(output_folder, "category_coverage"))
	try:
		os.stat(os.path.join(output_folder, "normalized_otu"))
	except:
		os.makedirs(os.path.join(output_folder, "normalized_otu"))
	try:
		os.stat(os.path.join(options.output, "prediction_files"))
	except:
		os.makedirs(os.path.join(options.output, "prediction_files"))
	try:
		os.stat(os.path.join(options.output, "predicted_phenotypes"))
	except:
		os.makedirs(os.path.join(options.output, "predicted_phenotypes"))     
	
	# Normalize the OTU_table by 16S copy number
	commands[:]= []
	cmd = "normalize_by_copy_number.py -i " + otu_table + " -o %s/normalized_otu/normalized_otu.biom" %(output_folder)
	commands.append(cmd)
	
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)
						
	# Run PICRUSt with OTU table and the treshold tables found in the thresholds directory
	commands[:] = []
	thresholds = []
	files = os.listdir("%s/lib/precalculated_files/" %(bugbase_dir))
	
	for f in files:
		if f.endswith(".txt.gz"):
			thresholds.append(f)
	for t in thresholds:
		cmd = "predict_metagenomes.py -i %s/normalized_otu/normalized_otu.biom" %(output_folder) + " -o %s/prediction_files/threshold_predictions/" %(output_folder) + t + " -c %s/lib/precalculated_files/thresholds/" %(bugbase_dir) + t + " -f --normalize_by_otu" 
		commands.append(cmd)
	
	# Run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)
						
	# For all files as ".txt.gz", move them to ".txt
	files = os.listdir("%s/prediction_files/threshold_predictions/" %(output_folder))
	for f in files:
		if f.endswith('.txt.gz'):
			sourcefile = os.path.join("%s/prediction_files/threshold_predictions/" %(output_folder), f)
			destfile = os.path.splitext(sourcefile)[0]
			os.rename(sourcefile, destfile)
											 
	# Make category coverage plots and calculate variance from PICRUSt outputs and map
	commands[:] = []
	OTU_thresholds = []
	files = os.listdir("%s/prediction_files/threshold_predictions/" %(output_folder))
	for f in files:
		if f.endswith(".txt"):
			OTU_thresholds.append(f)
	if options.plot_all is False:
		if options.groups is None:
			for t in OTU_thresholds:
				cmd = "Rscript %s/bin/trait_coverage_plots.r -i %s/prediction_files/threshold_predictions/" %(bugbase_dir, output_folder) + t + " -m " + map + " -c " + column + " -o %s/category_coverage/" %(output_folder) + t
				commands.append(cmd)
		else:
			for t in OTU_thresholds:
				cmd = "Rscript %s/bin/trait_coverage_plots.r -i %s/prediction_files/threshold_predictions/" %(bugbase_dir, output_folder) + t + " -m " + map + " -c " + column + " -o %s/category_coverage/" %(output_folder) + t + " -g " + ",".join(groups)
				commands.append(cmd)
	else:
		for t in OTU_thresholds:
			cmd = "Rscript %s/bin/trait_coverage_plots_all.r -i %s/prediction_files/threshold_predictions/" %(bugbase_dir, output_folder) + t + " -o %s/category_coverage/" %(output_folder) + t
			commands.append(cmd)

	# Run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)
	 
	# Make category coverage tables based on threshold set or input file in category_coverage/
	commands[:] = []
	variance = {}
	files = os.listdir("%s/category_coverage" %(output_folder)) 
	for f in files:
		if f.endswith(".txt"):
			variance[f] = {} 
	for v in variance: 
		var_dict = {}
		with open(os.path.join("%s/category_coverage/" %(output_folder), v), "r") as inputFile:
			for line in list(inputFile)[1:]: # for the rows (excluding header) in the input file
				values = line.strip().split("\t")
				threshold = float(values[0])
				var = float(values[2])  
				var_dict[threshold] = var
			variance[v] = max(var_dict.iteritems(), key=operator.itemgetter(1))[0] # find the greatest variance

	if options.threshold is None:
		cmd = "category_coverage.py -o %s/prediction_files/prediction_input.txt " %(output_folder)
		for traitfile,threshold in variance.items():
			traitfile = os.path.join("%s/lib/precalculated_files/" %(bugbase_dir), traitfile)
			if threshold == 0:
				threshold = 1
			else:
				threshold = threshold
			cmd += " -i " + traitfile + ".gz" + " -T " + str(threshold)
		commands.append(cmd)
	else:
		cmd = "category_coverage.py -o %s/prediction_files/prediction_input.txt -t %s" %(output_folder, options.threshold)
		for traitfile,threshold in variance.items():
			traitfile = os.path.join("%s/lib/precalculated_files/" %(bugbase_dir), traitfile)
			cmd += " -i " + traitfile + ".gz"
		commands.append(cmd)
		
	# Run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)
	 
	# Run PICRUSt with OTU table and the input table.
	commands[:] =[]
	cmd = "predict_metagenomes.py -i %s/normalized_otu/normalized_otu.biom" %(output_folder) + " -o %s/prediction_files/phenotype_predictions.txt -c %s/prediction_files/prediction_input.txt -f --normalize_by_otu"  %(output_folder,output_folder)
	commands.append(cmd)
	
	# Run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)
	 
	# Plot phenotype predictions  
	commands[:] = []
	traits = []
	with open("%s/prediction_files/picrust_prediction.txt" %(output_folder)) as trait_prediction:
		for line in list(trait_prediction)[2:]:
			values = line.strip().split("\t")
			trait = values[0]
			traits.append(trait)
	if options.plot_all is False:
		if options.groups is None:
			for t in traits:
				cmd = "Rscript %s/bin/make-plot.r -T %s/prediction_files/phenotype_predictions.txt -m " %(bugbase_dir, output_folder) + map + " -c " + column + " -t " + t  + " -o %s/predicted_phenotypes/" %(output_folder)
				commands.append(cmd)
		else:
			for t in traits:
				cmd = "Rscript %s/bin/make-plot.r -T %s/prediction_files/phenotype_predictions.txt -m " %(bugbase_dir, output_folder) + map + " -c " + column + " -t " + t  + " -o %s/predicted_phenotypes/" %(output_folder) + " -G " + ",".join(groups)
				commands.append(cmd)
	else:
		for t in traits:
			cmd = "Rscript %s/bin/make-plot_all.r -T %s/prediction_files/phenotype_predictions.txt -t " %(bugbase_dir, output_folder) + t  + " -o %s/predicted_phenotypes/" %(output_folder)
			commands.append(cmd)  
		
	# Run commands
	return_vals = run_commands(commands, print_only=options.print_only, verbose=options.verbose)
		
	print "[SUCCESSFUL] Bugs have been analyzed"
