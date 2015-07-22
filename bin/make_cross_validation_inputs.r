#!/usr/bin/env Rscript
library("optparse", verbose=F, warn.conflicts =F)

# make option list and parse command line
option_list <- list(
  # preprocessing parameters
  make_option(c("-i", "--trait_table"), type="character", default=NULL,
              help="IMG trait table [default: %default]"),
  make_option(c("-m", "--gg2img"), type="character", default=NULL,
              help="Greengenes to IMG mapping file [default: %default]"),
  make_option(c("-k","--kfolds"), type="numeric",default=10,
              help="Number of cross-validation folds (-1 for leave-one-out) [default: %default]."),
  make_option(c("-o","--outdir"), type="character",default=".",
              help="Output directory [default: %default].")
)

opts <- parse_args(OptionParser(option_list=option_list),
                   args=commandArgs(trailing=TRUE))

# create output directory if needed
if(opts$outdir != ".") dir.create(opts$outdir,showWarnings=FALSE, recursive=TRUE)

# create subdir for train files
dir.create(paste(opts$outdir, 'training_files',sep='/'),showWarnings=FALSE, recursive=TRUE)

# create subdir for test files
dir.create(paste(opts$outdir, 'test_files',sep='/'),showWarnings=FALSE, recursive=TRUE)

# run with 
# Rscript make_cross_validation_inputs
gg2img <- read.table(opts$gg2img,sep='\t',head=TRUE, comment.char='', row.names=NULL)
traits <- read.table(opts$trait_table,sep='\t',head=TRUE, row.names=NULL)

# keep only those traits present in gg mapping
traits <- traits[traits[,1] %in% gg2img[,2],]
traits_gg <- traits
traits_gg[,1] <- gg2img[match(traits_gg[,1],gg2img[,2]),1]

# save the subset table
write.table(traits_gg, file=sprintf("%s/trait_table_GG_subset.txt", opts$outdir), col.names=TRUE,quote=F,sep='\t', row.names=FALSE)

k <- opts$kfolds
if( k == -1) k <- nrow(traits)

folds <- sample(rep(1:k,ceiling(nrow(traits)/k))[1:nrow(traits)])


# save train tables
for(i in 1:k) {
	write.table(traits_gg[folds != i,],file=sprintf('%s/training_files/trait_table_GG_subset_fold_%05d_train.txt',opts$outdir, i),sep='\t',quote=F,col.names=TRUE,row.names=FALSE)
}


for(i in 1:k) {
	sink(sprintf("%s/test_files/trait_table_GG_subset_fold_%05d_test.txt", opts$outdir, i))
	cat('#OTU ID')
	for (n in 1:ncol(traits_gg)){
		cat("\ttrait_count")
	}
	cat('\n')
	write.table(traits_gg[folds == i,],sep='\t',quote=F,col.names=FALSE,row.names=FALSE)
	sink(NULL)
}
	