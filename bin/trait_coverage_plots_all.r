# Creates trait coverage plots and calculates variance

# USAGE FROM TERMINAL
# default:
# Rscript trait_coverage_plots.r -i threshold_table.txt 

library('optparse')
library('RColorBrewer')

# Make option list and parse command line
option_list <- list(
    make_option(c("-v", "--verbose"), 
    	action="store_true", 
    	default=FALSE, 
    	help="print extra output [default]"),
	make_option(c("-i", "--threshold_table"), 
		type="character",
		default=NULL,
        help="input threshold table created by picrust [default %default]"),
	make_option(c("-o", "--output_file"),
		type="character",
		default=NULL,
		help="name for output files (variance and plots) [default %default]")
)
opts <- parse_args(OptionParser(option_list=option_list))

# Import the predicted threshold table (PICRUSt output)
# Samples are columns, rows are thresholds
Threshold_Table <- read.table(opts$threshold_table,sep='\t',skip=1,head=T,row=1,check=F,comment="")

# Transpose because samples are the columns
Threshold_Table <- t(Threshold_Table)

# truncate zero columns in threshold table if requested
#if(!opts$suppress_truncation){
#	keep.ix <- colMeans(Threshold_Table) >= opts$truncation_threshold
#	print(keep.ix)
#	last.column <- max(which(keep.ix))
#	print(last.column)
#	Threshold_Table <- Threshold_Table[,1:last.column,drop=F]
#}

# Calculate the variance for each row
stdevs <- apply(Threshold_Table,2,sd)
vars <- apply(Threshold_Table,2,var)
means <- apply(Threshold_Table,2,mean)
coeff_var <- stdevs/means

# Set thresholds
thresholds <- as.numeric(colnames(Threshold_Table))

# Save thresholds, means, and variances to file
output.table <- data.frame(Threshold=thresholds, Mean=means, Variance=vars)
outfile <- gsub(".txt", "", opts$threshold_table)
if(is.null(opts$output_file)){
	write.table(output.table, file=paste(outfile),sep='\t',quote=F,row.names=FALSE )
} else {
	write.table(output.table, file=paste(opts$output_file),sep='\t',quote=F,row.names=FALSE )
}

# Set colors
cols <- brewer.pal(9, 'Set1')[-6]

# Assign pdf name
if(is.null(opts$output_file)){
	filename <- paste(outfile, ".pdf", sep='')
} else {
	outFile <- gsub(".txt", "", opts$output_file)
	filename <- paste(outFile, ".pdf", sep='')
}

# Plot the mean phenotype prediction for each threshold
pdf(filename, height=5,width=5);
par(oma=c(0.5,0.5,0.5,0.5),mar=c(5,4,2,2), cex.axis=0.75, cex.lab=.75, cex=0.75,
	lwd=2.5, bg="transparent")	

plot(thresholds, Threshold_Table[1,,drop=F], type="n", xlab="Threshold (% of category covered)", ylab="Proportion of Microbiome", ylim = c(0, 1))
axis(side=1, lwd=1.5)
axis(side=2, lwd=1.5)
lines(thresholds, means)

dev.off()
	