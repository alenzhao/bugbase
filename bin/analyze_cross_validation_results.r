#!/usr/bin/env Rscript
#
# Analyzes the cross validation outputs
#
# USAGE FROM TERMINAL:
# Rscript analyze_cross_validation_results.r -y IMG_trait_table.txt -Y predicted_traits.txt -o out_directory -f out_file.txt

library("optparse", verbose=F, warn.conflicts =F)

# Make option list and parse command line
option_list <- list(
  # preprocessing parameters
  make_option(c("-y", "--expected_outputs"), type="character", default=NULL,
              help="Known IMG trait table [default: %default]"),
  make_option(c("-Y", "--predicted_outputs"), type="character", default=NULL,
              help="Predicted IMG trait table [default: %default]"),
  make_option(c("-o","--outdir"), type="character",default=".",
              help="Output directory [default: %default]."),
  make_option(c("-f","--outfile"), type="character",default="results.txt",
              help="Output file [default: %default].")
)

opts <- parse_args(OptionParser(option_list=option_list),
                   args=commandArgs(trailing=TRUE))

# Create output directory if needed
if(opts$outdir != ".") dir.create(opts$outdir,showWarnings=FALSE, recursive=TRUE)

y <- read.table(opts$expected_outputs, sep='\t',head=T,row=1, comment="")
yhat <- read.table(opts$predicted_outputs, sep='\t',head=F,row=1,)

# Get only those rows in both tables
common.ids <- intersect(rownames(y), rownames(yhat))
if(length(common.ids) < nrow(y) || length(common.ids) < nrow(yhat)){
	cat('\nWarning: there are', nrow(y), "rows in the expected trait table and", nrow(yhat), 
		"rows in the predicted trait table, with only", length(common.ids),"rows in common.\n")
}
yhat <- yhat[common.ids,,drop=F]
y <- y[common.ids,,drop=F]

tf_table <- y == yhat

# Print full accuracy measure to screen and file
cat(sprintf('Overall accuracy is %.4f.\n', mean(y == yhat, na.rm=TRUE)))

cat(sprintf('Overall accuracy is %.4f.\n', mean(y == yhat, na.rm=TRUE)), file=opts$outfile)

# Assign pdf name
if(is.null(opts$outfile)){
	filename <- paste("results.pdf")
} else {
	outFile <- gsub(".txt", "", opts$outfile)
	filename <- paste(outFile, ".pdf", sep='')
}


pdf(filename, height=5,width=5);
par(oma=c(0,0,0,0),mar=c(5,4,2,2), cex.axis=0.75, cex.lab=.75, cex=0.75,
	lwd=2.5, bg="transparent")	
if(ncol(tf_table)<=1){
	plot(tf_table[,1], xlab="OTU ID", ylab="Prediction Accuracy", ylim = c(0, 1))
} else {
		plot(rowMeans(tf_table[,-1], na.rm = TRUE), xlab="OTU ID", ylab="Prediction Accuracy", ylim = c(0, 1))
}
#plot(rowMeans(tf_table[,-1]), xlab="OTU ID", ylab="Prediction Accuracy", ylim = c(0, 1))
axis(side=1, lwd=1.5)
axis(side=2, lwd=1.5)


dev.off()