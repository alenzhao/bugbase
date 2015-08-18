# Creates trait coverage plots and calculates variance

# USAGE FROM TERMINAL
# default:
# Rscript trait_coverage_plots.r -i threshold_table.txt 

library('optparse')
library('RColorBrewer')

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



# import the predicted threshold table (picrust output), samples are columns, rows are thresholds
Threshold_Table <- read.table(opts$threshold_table,sep='\t',skip=1,head=T,row=1,check=F,comment="")

# transpose because samples are the columns
Threshold_Table <- t(Threshold_Table)

# truncate zero columns in threshold table if requested
#if(!opts$suppress_truncation){
#	keep.ix <- colMeans(Threshold_Table) >= opts$truncation_threshold
#	print(keep.ix)
#	last.column <- max(which(keep.ix))
#	print(last.column)
#	Threshold_Table <- Threshold_Table[,1:last.column,drop=F]
#}

# calculate the variance for each row
stdevs <- apply(Threshold_Table,2,sd)
vars <- apply(Threshold_Table,2,var)
means <- apply(Threshold_Table,2,mean)
coeff_var <- stdevs/means

# load mapping file
# map <- read.table(opts$mappingfile,sep='\t',head=T,row=1,check=F,comment='')

# double-check that map and thresholds have same sample IDs
#cat("\nMake sure the number of samples in the mapping file and threshold table are the same.\nIf they do not match, analysis will not #be valid.\n\n")
#cat("Dimensions of threshold table:\n")
#dim(Threshold_Table)
#cat("Dimensions of map:\n")
#dim(map)
#cat("\n")
#length(intersect(rownames(map),rownames(Threshold_Table)))

# ensure same order of samples in map and traits
#map <- map[rownames(Threshold_Table),]

#map_column <- opts$mapcolumn

# define treatment groups
#if(is.null(opts$groups)){
#	groups <- sort(unique(map[,map_column]))
#} else {
#	groups <- c(opts$groups)
#	groups <- strsplit(groups, ",")[[1]]
#	# get indices of which rows to keep
#	ix.keep <- map[,map_column] %in% groups

#	# keep only subset of samples belonging to requested groups
#	map <- droplevels(as.data.frame(map[ix.keep,]))
#	Threshold_Table <- Threshold_Table[ix.keep,,drop=F]
#}

thresholds <- as.numeric(colnames(Threshold_Table))

# save thresholds, means, and variances to file
output.table <- data.frame(Threshold=thresholds, Mean=means, Variance=vars)
outfile <- gsub(".txt", "", opts$threshold_table)
if(is.null(opts$output_file)){
	write.table(output.table, file=paste(outfile),sep='\t',quote=F,row.names=FALSE )
} else {
	write.table(output.table, file=paste(opts$output_file),sep='\t',quote=F,row.names=FALSE )
}

# show number of samples in each body site and trait
#cat("\nNumber of samples in each treatment group (unordered):\n")
#table(map[,map_column])

# set colors
cols <- brewer.pal(9, 'Set1')[-6]

# assign pdf name
if(is.null(opts$output_file)){
	filename <- paste(outfile, ".pdf", sep='')
} else {
	outFile <- gsub(".txt", "", opts$output_file)
	filename <- paste(outFile, ".pdf", sep='')
}

pdf(filename, height=5,width=5);
par(oma=c(0.5,0.5,0.5,0.5),mar=c(5,4,2,2), cex.axis=0.75, cex.lab=.75, cex=0.75,
	lwd=2.5, bg="transparent")	

plot(thresholds, Threshold_Table[1,,drop=F], type="n", xlab="Threshold (% of category covered)", ylab="Proportion of Microbiome", ylim = c(0, 1))
axis(side=1, lwd=1.5)
axis(side=2, lwd=1.5)
# for(i in 1:length(groups)){
# 	group <- groups[i]
# 	ix <- map[,map_column]==group
# 	means <- colMeans(Threshold_Table[ix,,drop=F])
lines(thresholds, means)
#	legend(x=max(thresholds)/3, y=0.8+(0.04*i), group, cex=0.65, lty=1, col=cols[i], bty="n")	
#}

dev.off()
	