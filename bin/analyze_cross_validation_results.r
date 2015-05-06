#!/usr/bin/env Rscript
library("optparse", verbose=F, warn.conflicts =F)

# make option list and parse command line
option_list <- list(
  # preprocessing parameters
  make_option(c("-y", "--expected_outputs"), type="character", default=NULL,
              help="Known IMG trait table [default: %default]"),
  make_option(c("-Y", "--predicted_outputs"), type="character", default=NULL,
              help="Predicted IMG trait table [default: %default]"),
  make_option(c("-o","--outdir"), type="character",default=".",
              help="Output directory [default: %default].")
)

opts <- parse_args(OptionParser(option_list=option_list),
                   args=commandArgs(trailing=TRUE))

# create output directory if needed
if(opts$outdir != ".") dir.create(opts$outdir,showWarnings=FALSE, recursive=TRUE)

y <- read.table('cv/trait_table_GG_subset.txt', sep='\t',head=T,row=1)
yhat <- read.table('cv/trait_table_GG_subset_predicted.txt', sep='\t',head=T,row=1)

# get only those rows in both tables
common.ids <- intersect(rownames(y), rownames(yhat))
if(length(common.ids) < nrow(y) || length(common.ids) < nrow(yhat)){
	cat('\nWarning: there are', nrow(y), "rows in the expected trait table and", nrow(yhat), 
		"rows in the predicted trait table, with only", length(common.ids),"rows in common.\n")
}
yhat <- yhat[common.ids,,drop=F]
y <- y[common.ids,,drop=F]

# print full accuracy measure
cat(sprintf('Overall accuracy is %.4f.\n', mean(y == yhat)))
