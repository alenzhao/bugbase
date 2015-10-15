# Creates trait coverage plots and calculates variance

# USAGE FROM TERMINAL
# default:
# Rscript trait_coverage_plots.r -i threshold_table.txt -m mapping_file.txt -c map_column  

# Specify groups to plot and output file names:
# Rscript trait_coverage_plots.r -i threshold_table.txt -m mapping_file.txt -c map_column -g treatment_groups -o filename

# Suppress truncation (specified treatment groups still an option):
# Rscript trait_coverage_plots.r -i threshold_table.txt -m mapping_file.txt -c map_column -s -t proportion_of_x_to_truncate   

# Specify truncation (specified treatment groups still an option):
# Rscript trait_coverage_plots.r -i threshold_table.txt -m mapping_file.txt -c map_column -t proportion_of_x_to_truncate   

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
	make_option(c("-m", "--mappingfile"),
		type="character",
		default=NULL,
        help="mapping file [default %default]"),
	make_option(c("-c", "--mapcolumn"),
		type="character",
		default=NULL,
		help="name of column that lists treatment groups [default %default]"),
	make_option(c("-g", "--groups"),
		type="character",
		default=NULL,
		help="treatment groups you would like to plot, separated by commas with no spaces [default %default]"),
	make_option(c("-s", "--suppress_truncation"),
    	action="store_true",
    	default=FALSE,
        help="suppress truncation of plot x axis [default]"),
    make_option(c("-t", "--truncation_threshold"),
    	type="numeric",
    	default=.0001,
        help="Minimum proportion at which to truncate plot [default %default]"),
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

# Truncate zero columns in threshold table if requested
if(!opts$suppress_truncation){
	keep.ix <- colMeans(Threshold_Table) >= opts$truncation_threshold
#	print(keep.ix)
	last.column <- max(which(keep.ix))
#	print(last.column)
	Threshold_Table <- Threshold_Table[,1:last.column,drop=F]
}

# Calculate the variance for each row
stdevs <- apply(Threshold_Table,2,sd)
vars <- apply(Threshold_Table,2,var)
means <- apply(Threshold_Table,2,mean)
coeff_var <- stdevs/means

# Load mapping file
map <- read.table(opts$mappingfile,sep='\t',head=T,row=1,check=F,comment='')

# Double-check that map and thresholds have same sample IDs
cat("\nMake sure the number of samples in the mapping file and threshold table are the same.\nIf they do not match, analysis will not be valid.\n\n")
cat("Dimensions of threshold table:\n")
dim(Threshold_Table)
cat("Dimensions of map:\n")
dim(map)
cat("\n")
#length(intersect(rownames(map),rownames(Threshold_Table)))

# Ensure same order of samples in map and traits
map <- map[rownames(Threshold_Table),]

map_column <- opts$mapcolumn

# Define treatment groups
if(is.null(opts$groups)){
	groups <- sort(unique(map[,map_column]))
} else {
	groups <- c(opts$groups)
	groups <- strsplit(groups, ",")[[1]]
	# get indices of which rows to keep
	ix.keep <- map[,map_column] %in% groups

	# keep only subset of samples belonging to requested groups
	map <- droplevels(as.data.frame(map[ix.keep,]))
	Threshold_Table <- Threshold_Table[ix.keep,,drop=F]
}

thresholds <- as.numeric(colnames(Threshold_Table))

# Save thresholds, means, and variances to file
output.table <- data.frame(Threshold=thresholds, Mean=means, Variance=vars)
outfile <- gsub(".txt", "", opts$threshold_table)
if(is.null(opts$output_file)){
	write.table(output.table, file=paste(outfile),sep='\t',quote=F,row.names=FALSE )
} else {
	write.table(output.table, file=paste(opts$output_file),sep='\t',quote=F,row.names=FALSE )
}

# Show number of samples in each treatment group
cat("\nNumber of samples in each treatment group (unordered):\n")
table(map[,map_column])

# Set colors
cols <- brewer.pal(9, 'Set1')[-6]

# Assign pdf name
if(is.null(opts$output_file)){
	filename <- paste(outfile, ".pdf", sep='')
} else {
	outFile <- gsub(".txt", "", opts$output_file)
	filename <- paste(outFile, ".pdf", sep='')
}

pdf(filename, height=5,width=5);
par(oma=c(0.5,0.5,0.5,0.5),mar=c(5,4,2,2), cex.axis=0.75, cex.lab=.75, cex=0.75,
	lwd=2.5, bg="transparent")
		
# Plot the mean phenotype abundance for each threshold
plot(thresholds, Threshold_Table[1,,drop=F], type="n", xlab="Threshold (% of category covered)", ylab="Proportion of Microbiome", ylim = c(0, 1))
axis(side=1, lwd=1.5)
axis(side=2, lwd=1.5)
for(i in 1:length(groups)){
	group <- groups[i]
	ix <- map[,map_column]==group
	means <- colMeans(Threshold_Table[ix,,drop=F])
	lines(thresholds, means, col=cols[i])
 	legend(x=max(thresholds)/3, y=0.8+(0.04*i), group, cex=0.65, lty=1, col=cols[i], bty="n")	
}

dev.off()
	