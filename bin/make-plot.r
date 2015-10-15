# Plot phenotype predictions per treatment group and run Mann-Whitney U tests
# 
# USAGE FROM TERMINAL:
# Default:
# Rscript make-plot.r -T predicted_traits.txt -m map_file.txt -c map_column -t trait_name

# Plot only certain treatment groups
# Rscript make-plot.r -T predicted_traits.txt -m map_file.txt -c map_column -g group1,group2

# Plot arcsine square root transformed data:
# Rscript make-plot.r -T predicted_traits.txt -m map_file.txt -c map_column -x

library('optparse')
library('beeswarm')

# Make option list and parse command line
option_list <- list(
    make_option(c("-v", "--verbose"), action="store_true", default=TRUE,
        help="Print extra output [default]"),
	make_option(c("-c", "--mapcolumn"), type="character", default=NULL,
        help="Column of mapping file to plot [default %default]"),
	make_option(c("-m", "--mappingfile"), type="character", default=NULL,
        help="mapping file to plot [default %default]"),
	make_option(c("-o", "--output"), type="character", default=".",
        help="output directory [default %default]"),
	make_option(c("-T", "--trait_table"), type="character", default=NULL,
        help="trait table [default %default]"),
	make_option(c("-t", "--trait"), type="character", default=NULL,
        help="trait to plot [default %default]"),
	make_option(c("-x", "--transform"), type="character", default='none',
        help="transform to apply to outcome (none,asin-sqrt) [default %default]"),
	make_option(c("-G", "--groups"), type="character", default=NULL,
		help="treatment groups of samples, separated by commas, no spaces [default %default]")
)
opts <- parse_args(OptionParser(option_list=option_list))


if(opts$output != "."){
	if(!file.exists(opts$output)){
		dir.create(opts$output, showWarnings = FALSE, recursive = TRUE)
	}
}

traits <- read.table(opts$trait_table,sep='\t',skip=1,head=T,row=1,check=F,comment="")

# Transpose trait table because samples were in the columns
traits <- t(traits)

# Load map
map <- read.table(opts$mappingfile,sep='\t',head=T,row=1,check=F,comment='')

cat("\n\n RESULTS: \n\n")

# Check dimensions of trait table and mapping file
cat("\ndimensions of trait table:\n")
dim(traits)
cat("Dimensions of the mapping file:\n")
dim(map)

# Double-check that map and traits have same sample IDs
cat("\n Number of sample IDs that match between the trait table and mapping file:\n")
intersect_btwn <- intersect(rownames(map),rownames(traits))
length(intersect_btwn)

# Keep only samples that intersect between the mapping file and trait table
new_map <- map[intersect_btwn,]
new_traits <- droplevels(as.data.frame(traits[intersect_btwn,]))
colnames(new_traits) <- colnames(traits)

#cat("\nDimensions of modified trait table:\n")
#dim(new_traits)
#cat("Dimensions of the modified mapping file:\n")
#dim(new_map)

# Ensure same order of samples in map and traits
new_map <- new_map[rownames(new_traits),]

# Define map column to plot
map_column <- opts$mapcolumn

# Define trait to test
trait <- c(opts$trait)
trait_name <- ((strsplit(trait, ".", fixed=TRUE))[[1]])[[1]]

if(opts$transform == 'asin-sqrt'){
	traits <- asin(sqrt(traits))
}

# Define treatment groups
if(is.null(opts$groups)){
	groups <- sort(unique(new_map[,map_column]))
	groups <- lapply(groups, as.character)
} else {
	groups <- c(opts$groups)
	groups <- strsplit(groups, ",")[[1]]
	# get indices of which rows to keep
	ix.keep <- new_map[,map_column] %in% groups

	# keep only subset of samples belonging to requested groups
	new_map <- droplevels(as.data.frame(new_map[ix.keep,]))
	new_traits <- as.data.frame(new_traits[ix.keep,])
	colnames(new_traits) <- colnames(traits)
}

# Show number of samples in treatment group, and their phenotype abundance summary stats
cat("\nNumber of samples in each treatment group (unordered):\n")
table(new_map[,map_column])

cat("\nProportion with phenotype (mean):\n")
tapply(new_traits[,trait], new_map[,map_column], mean)

cat("\nProportion with phenotype (median):\n")
tapply(new_traits[,trait], new_map[,map_column], median)

cat("\nStandard deviation:\n")
tapply(new_traits[,trait], new_map[,map_column], sd)

# Non-parametric tests - either two classes or multi-class, print to screen and file
if(length(groups)==2){
	group.pvalue <- wilcox.test(new_traits[,trait] ~ new_map[,map_column])$p.value
	
	cat("\nNumber of samples in each treatment group:\n")
	print(table(new_map[,map_column]))

	cat("\nProportion with phenotype (mean):\n")
	print(tapply(new_traits[,trait], new_map[,map_column], mean))

	cat("\nProportion with phenotype (median):\n")
	print(tapply(new_traits[,trait], new_map[,map_column], median))

	cat("\nStandard deviation:\n")
	print(tapply(new_traits[,trait], new_map[,map_column], sd))
	
	cat("\np-value is:\n")
	print(group.pvalue)
	
	cat("FDR-corrected p-value is:\n")
	print(p.adjust(group.pvalue,'fdr'))
	
	outfile <- paste(trait_name, "_stats.txt", sep="")

	sink(paste(opts$output,outfile,sep='/'))
	
	cat("\nMann-Whitney-Wilcoxon Test was performed.\n")
	cat("p-values is:\n")
	print(group.pvalue)
	
	cat("\nFDR-corrected p-value is:\n")
	print(p.adjust(group.pvalue,'fdr'))

	sink()
	
} else {
	group.pvalue <- kruskal.test(new_traits[,trait] ~ new_map[,map_column])$p.value

	# Also run pairwise tests if > 2 categories, print output to screen and file
	pw.pvalues <- NULL
	pw.names <- NULL
	for(i in 1:(length(groups) - 1)){
		for(j in (i+1):length(groups)){
			ix.trait.i <- new_map[,map_column] == groups[i]
			ix.trait.j <- new_map[,map_column] == groups[j]
			
			pvalue <- wilcox.test(new_traits[ix.trait.i,trait], new_traits[ix.trait.j,trait])$p.value
			
			pw.pvalues <- c(pw.pvalues, pvalue)
			test.name <- paste(groups[i], "_vs_", groups[j],sep='')
			pw.names <- c(pw.names, test.name)
		}
	}
	names(pw.pvalues) <- pw.names
	
	cat("\nPairwise p-values are:\n")
	print(pw.pvalues)
	
	cat("FDR-corrected pairwise p-values are:\n")
	print(p.adjust(pw.pvalues,'fdr'))
	
	outfile <- paste(trait_name, "_stats.txt", sep="")
	
	sink(paste(opts$output, outfile, sep='/'))
	
	cat("\nNumber of samples in each treatment group:\n")
	print(table(new_map[,map_column]))

	cat("\nProportion with phenotype (mean):\n")
	print(tapply(new_traits[,trait], new_map[,map_column], mean))

	cat("\nProportion with phenotype (median):\n")
	print(tapply(new_traits[,trait], new_map[,map_column], median))

	cat("\nStandard deviation:\n")
	print(tapply(new_traits[,trait], new_map[,map_column], sd))
	
	cat("\nPairwise Mann-Whitney-Wilcoxon Tests were performed.\n")
	cat("Pairwise p-values are:\n")
	print(pw.pvalues)
	
	cat("\nFDR-corrected pairwise p-values are:\n")
	print(p.adjust(pw.pvalues,'fdr'))

	cat("\nKruskal-Wallis Test was performed.\n")
	cat("\nGroup p-value is:\n")
	print(group.pvalue)

	sink()
}

# Get palette 1 from R ColorBrewer
# Set transparency to 65 out of FF
library('RColorBrewer')
cols <- sprintf('%s65',brewer.pal(9,'Set1'))

# Assign pdf name
file <- c(".pdf")
name <- paste(trait_name, ".pdf", sep='')
name <- paste(opts$output, name, sep="/")

# Re-order to plot according to order specified by user (or by default occurrence in file)
new_map[,map_column] <- factor(new_map[,map_column], levels = c(groups))

# Save the plot as a pdf h/w 6 inches
pdf(name, height=6,width=6);
par(mar=c(8,5,1,1), oma=c(0.5,0.5,0.5,0.5))
beeswarm(new_traits[,trait] ~ new_map[,map_column],corral='random',cex.axis=.55,pch=16,col=cols, xlab='',ylab='Proportion of Microbiome',cex=1, cex.lab=0.65, las=2)
bxplot(new_traits[,trait] ~ new_map[,map_column], add=TRUE)
dev.off()