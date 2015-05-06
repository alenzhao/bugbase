#!/usr/bin/env python
# Runs cross-validation predictions of known traits.

# USAGE
# Default settings
# cross_validation.py -i trait_table.txt -t GG_tree.nwk -m GG_to_IMGv350.txt -o cv

# with 2-fold cross validation and verbose output
# cross_validation.py -i trait_table.txt -t GG_tree.nwk -m GG_to_IMGv350.txt -k 2 -o cv -v

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
	parser.add_option("-P","--parallel",
   		action="store_true",
		default=False,
		help="Run commands in parallel (default %default)",)
	parser.add_option("-i", "--trait_table",
		default=None,
		type='string',
		help="IMG trait table (required)")
	parser.add_option("-t", "--tree",
		default=None,
		type='string',
		help="Phylogenetic tree with Greengenes OTUs as tips (required)")
	parser.add_option("-m", "--gg2img",
		default=None,
		type='string',
		help="Greengenes to IMG mapping file (required)")
	parser.add_option("-o", "--outdir",
		default=".",
		type='string',
		help="Output directory (default %default)")
	parser.add_option("-k","--nfolds",
		default=10,
		type='int',
		help="Number of cross validation folds (-1 means leave-one-out) (default %default)")
	return parser

def run_commands(commands, parallel=False, print_only=False, verbose=True, error_on_fail=True):
	return_vals = []

	# run all commands
	procs = []

	for i, cmd in enumerate(commands):
		if verbose:
			print cmd
		if not print_only:
			proc = Popen(cmd,shell=True,universal_newlines=True,stdout=PIPE,stderr=PIPE)
			procs.append(proc)
			if not parallel:
				stdout, stderr = proc.communicate()
				return_vals.append(proc.returncode)
	
	if parallel:
		for proc in procs:
			stdout, stderr = proc.communicate()
			# if requested, prints all output from the program
			if verbose:
				print stdout
				print stderr
			if error_on_fail == True and proc.returncode != 0:
				print stdout
				print stderr
				raise ValueError('Command failed: ' + cmd)	
	return(return_vals)
    
if __name__ == '__main__':
	parser = make_option_parser()
	(options, args) = parser.parse_args()
	
	# make directories needed
	if options.outdir != ".":
		try:
			os.stat(options.outdir)
		except:
			os.makedirs(options.outdir)

	# make cross-validation files
	cmd = "make_cross_validation_inputs.r -i " + options.trait_table + " -m " + options.gg2img + " -k '" + str(options.nfolds) + "' -o " + options.outdir
	# run commands
	return_vals = run_commands([cmd], print_only=options.print_only, verbose=options.verbose)
	
	# run predictions on each cv train file
	format_commands = []
	asr_commands = []
	predict_commands = []
	
	train_dir = os.path.join(options.outdir, "training_files")
	test_dir = os.path.join(options.outdir, "test_files")
	training_files = os.listdir(train_dir)
	test_files = []
	for training_file in training_files:
		if not training_file.endswith('.txt'):
			continue
		test_file = os.path.join(test_dir,training_file[0:-9] + "test.txt")
		test_files.append(test_file)
		training_file = os.path.join(train_dir, training_file)
		training_subdir = os.path.splitext(training_file)[0]
		try:
			os.stat(training_subdir)
		except:
			os.makedirs(training_subdir)
		
		format_dir = os.path.join(training_subdir, "format")
		cmd = "format_tree_and_trait_table.py -t " + options.tree + " -i " + training_file + " -m " + options.gg2img + " -o " + format_dir
		format_commands.append(cmd)
		cmd = "ancestral_state_reconstruction.py -i " + os.path.join(format_dir, "trait_table.tab") + " -t " + os.path.join(format_dir, "pruned_tree.newick") + " -o " + os.path.join(training_subdir, "asr_counts.tab")
		asr_commands.append(cmd)
	
		cmd = "predict_traits.py -i " + os.path.join(format_dir, "trait_table.tab") + " -t " + os.path.join(format_dir, "reference_tree.newick") + " -r " + os.path.join(training_subdir, "asr_counts.tab") + " -o " + os.path.join(training_subdir, "precalculated_traits.txt")
		cmd += " -l " + test_file
		predict_commands.append(cmd)

	# run commands
	return_vals = run_commands(format_commands, parallel=options.parallel, print_only=options.print_only, verbose=options.verbose)
	return_vals = run_commands(asr_commands, parallel=options.parallel, print_only=options.print_only, verbose=options.verbose)
	return_vals = run_commands(predict_commands, parallel=options.parallel, print_only=options.print_only, verbose=options.verbose)

	# now combine all prediction files
	cmd = "head -n 1 " + test_files[0] + " > " + os.path.join(options.outdir,"trait_table_GG_subset_predicted.txt")
	commands = [cmd]
	cmd = "for f in " + ' '.join(test_files) + "; do grep -v '#' $f >> " +  os.path.join(options.outdir,"trait_table_GG_subset_predicted.txt") + "; done"
	commands.append(cmd)
	
	# run final command
	return_vals = run_commands(commands, parallel=options.parallel, print_only=options.print_only, verbose=options.verbose)
