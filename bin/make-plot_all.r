# Plot trait predictions per treatment group and run Mann-Whitney U test
# 
# USAGE FROM TERMINAL:
# default:
# Rscript make-plot.r -T predicted_traits.txt -o output_file

library('optparse')
library('beeswarm')


option_list <- list(
    make_option(c("-v", "--verbose"), action="store_true", default=TRUE,
        help="Print extra output [default]"),
	make_option(c("-o", "--output"), type="character", default=".",
        help="output directory [default %default]"),
	make_option(c("-T", "--trait_table"), type="character", default=NULL,
        help="trait table [default %default]"),
    make_option(c("-t", "--trait"), type="character", default=NULL,
        help="trait to plot [default %default]")
)
opts <- parse_args(OptionParser(option_list=option_list))


if(opts$output != "."){
	if(!file.exists(opts$output)){
		dir.create(opts$output, showWarnings = FALSE, recursive = TRUE)
	}
}

traits <- read.table(opts$trait_table,sep='\t',skip=1,head=T,row=1,check=F,comment="")

# transpose because samples were in the columns
traits <- t(traits)

cat("\n\n RESULTS: \n\n")

# check dimensions of traits
cat("\ndimensions of trait table:\n")
dim(traits)

# show all rows, first 5 columns
#traits[,1:5]

# load 
# map <- read.table(opts$mappingfile,sep='\t',head=T,row=1,check=F,comment='')

# double-check that map and traits have same sample IDs
# cat("\nMake sure the number of samples in the map matches the samples in the trait table\n")
# length(intersect(rownames(map),rownames(traits)))

# ensure same order of samples in map and traits
# map <- map[rownames(traits),]

# see what traits are available
# colnames(traits)

# define map column
# map_column <- opts$mapcolumn

# define trait to test
trait <- c(opts$trait)
trait_name <- trait_name <- ((strsplit(trait, ".", fixed=TRUE))[[1]])[[1]]

# if(opts$transform == 'asin-sqrt'){
#	traits <- asin(sqrt(traits))
#}

# define treatment groups
# if(is.null(opts$groups)){
# 	groups <- sort(unique(map[,map_column]))
# } else {
# 	groups <- c(opts$groups)
# 	groups <- strsplit(groups, ",")[[1]]
# 	# get indices of which rows to keep
# 	ix.keep <- map[,map_column] %in% groups
# 
# 	# keep only subset of samples belonging to requested groups
# 	map <- droplevels(as.data.frame(map[ix.keep,]))
# 	traits <- traits[ix.keep,]
# }

# show number of samples in each body site and trait
#cat("\nNumber of samples in each treatment group (unordered):\n")
#table(map[,map_column])

#non-parametric tests - either two classes or multi-class, print to screen and file
#if(length(groups)==2){
#	group.pvalue <- wilcox.test(traits[,trait] ~ map[,map_column])$p.value
outfile <- paste(trait_name, "_stats.txt", sep="")	

sink(paste(opts$output, outfile,sep='/'))
cat("mean proportion with this trait is:\n")
print(mean(traits[,trait]))
cat("median proportion with this trait is:\n")
print(median(traits[,trait]))


sink()
# 	cat("p-value is:\n")
# 	print(group.pvalue)
# 	
# 	cat("FDR-corrected p-value is:\n")
# 	print(p.adjust(group.pvalue,'fdr'))
# 	
# 	outfile <- paste(opts$trait, "_stats.txt", sep="")
# 
# 	sink(paste(opts$output,outfile,sep='/'))
# 	
# 	cat("p-values is:\n")
# 	print(group.pvalue)
# 	
# 	cat("\nFDR-corrected p-value is:\n")
# 	print(p.adjust(group.pvalue,'fdr'))
# 
# 	sink()
# 	
# } else {
# 	group.pvalue <- kruskal.test(traits[,trait] ~ map[,map_column])$p.value
# 
# 	# also run pairwise tests if > 2 categories
# 	pw.pvalues <- NULL
# 	pw.names <- NULL
# 	for(i in 1:(length(groups) - 1)){
# 		for(j in (i+1):length(groups)){
# 			ix.trait.i <- map[,map_column] == groups[i]
# 			ix.trait.j <- map[,map_column] == groups[j]
# 			
# 			pvalue <- wilcox.test(traits[ix.trait.i,trait], traits[ix.trait.j,trait])$p.value
# 			
# 			pw.pvalues <- c(pw.pvalues, pvalue)
# 			test.name <- paste(groups[i], "_vs_", groups[j],sep='')
# 			pw.names <- c(pw.names, test.name)
# 		}
# 	}
# 	names(pw.pvalues) <- pw.names
# 	
# 	cat("Pairwise p-values are:\n")
# 	print(pw.pvalues)
# 	
# 	cat("FDR-corrected pairwise p-values are:\n")
# 	print(p.adjust(pw.pvalues,'fdr'))
# 	
# 	outfile <- paste(opts$trait, "_stats.txt", sep="")
# 	
# 	sink(paste(opts$output, outfile, sep='/'))
# 	
# 	cat("Pairwise p-values are:\n")
# 	print(pw.pvalues)
# 	
# 	cat("\nFDR-corrected pairwise p-values are:\n")
# 	print(p.adjust(pw.pvalues,'fdr'))
# 
# 	cat("\nGroup p-value is:\n")
# 	print(group.pvalue)
# 
# 	sink()
# }


# adjust if needed
# cat("\nNon-parametric Wilcox Test\n")
# cat("\nfdr adjusted p-values for treatment groups:")
# cat("\none vs two, one vs three, one vs four, two vs three, two vs four and three vs four\n\n")
# p.adjust(p.values,'fdr')
# cat("\n")

# get palette 1 from R ColorBrewer
# set transparency to 44 out of FF
library('RColorBrewer')
cols <- sprintf('%s44',brewer.pal(9,'Set1'))

#assign pdf name
file <- c(".pdf")
name <- paste(trait[1], ".pdf", sep='')
name <- paste(opts$output, name, sep="/")
# note you can also use sprintf - google for formatting
# name <- sprintf('%s_%d.pdf',trait[1],length(groups))

# now save the plot as a pdf h/w 5 inches
pdf(name, height=6,width=6);
par(mar=c(8,5,1,1), oma=c(0.5,0.5,0.5,0.5))
beeswarm(traits[,trait],corral='random',cex.axis=.55,pch=16,col=cols, xlab='',ylab='Proportion of Microbiome',cex=1, cex.lab=0.65, las=2)
bxplot(traits[,trait], add=TRUE)
dev.off()