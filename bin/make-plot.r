# Plot trait predictions per treatment group and run Mann-Whitney U test
# 
# USAGE FROM TERMINAL:
# default:
# Rscript make-plot.r -T predicted_traits.txt -m map_file.txt -c map_column -t trait_name

# plot only certain treatment groups
# Rscript make-plot.r -T predicted_traits.txt -m map_file.txt -c map_column -g group1,group2

# plot arcsine square root transformed data:
# Rscript make-plot.r -T predicted_traits.txt -m map_file.txt -c map_column -x

# plot continuous data
# Rscript make-plot.r -T predicted_traits.txt -m map_file.txt -c map_column -r


library('optparse')
library('beeswarm')
library('RColorBrewer')


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
	make_option(c("-z", "--continuous"), action="store_true", default=FALSE,
        help="plot continuous data [default %default]"),
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

# transpose because samples were in the columns
traits <- t(traits)

# load 
map <- read.table(opts$mappingfile,sep='\t',head=T,row=1,check=F,comment='')

cat("\n\n RESULTS: \n\n")

# check dimensions of traits
cat("\ndimensions of trait table:\n")
dim(traits)
cat("Dimensions of the mapping file:\n")
dim(map)

# double-check that map and traits have same sample IDs
cat("\n Number of sample IDs that match between the trait table and mapping file:\n")
intersect_btwn <- intersect(rownames(map),rownames(traits))
length(intersect_btwn)

#Keep only samples that intersect between the mapping file and trait tables
new_map <- map[intersect_btwn,]
new_traits <- droplevels(as.data.frame(traits[intersect_btwn,]))
colnames(new_traits) <- colnames(traits)

# cat("\nDimensions of modified trait table:\n")
# dim(new_traits)
# cat("Dimensions of the modified mapping file:\n")
# dim(new_map)


# ensure same order of samples in map and traits
new_map <- new_map[rownames(new_traits),]


# define map column
map_column <- opts$mapcolumn

# define trait to test
trait <- c(opts$trait)
trait_name <- ((strsplit(trait, ".", fixed=TRUE))[[1]])[[1]]

if(opts$transform == 'asin-sqrt'){
	traits <- asin(sqrt(traits))
}


if(isTRUE(opts$continuous)){
	
	cor.tests <- cor.test(new_traits[,trait], new_map[,map_column])
	lm.out <- lm(new_traits[,trait] ~ new_map[,map_column])

	coeff <- summary(lm.out)$coefficients[2,]
	fstats <- summary(lm.out)$fstatistic
	p <- pf(fstats[1],fstats[2],fstats[3],lower.tail=F)

	cat("\n\nLiner Model Statistics for: ")
	cat(trait_name)
	cat("\n\nCoefficients\n")
	print(coeff)
	cat("\np-value\n")
	cat(p)
	cat("\n\nPearson's Correlation\n\n")
	cat("Correlation Estimate:\n")
	cat(cor.tests$estimate)
	cat("\n\np-value\n")
	cat(cor.tests$p.value)
	cat("\n\n")

	outfile <- paste(trait_name, "_stats.txt", sep="")
	
	sink(paste(opts$output,outfile,sep='/'))
	cat("\n\nLiner Model Statistics for: ")
	cat(trait_name)
	cat("\n\nCoefficients\n")
	print(coeff)
	cat("\np-value\n")
	cat(p)
	cat("\n\nPearson's Correlation\n\n")
	cat("Correlation Estimate:\n")
	cat(cor.tests$estimate)
	cat("\n\np-value\n")
	cat(cor.tests$p.value)
	cat("\n\n")
	sink()

	cols <- sprintf('%s95',brewer.pal(9,'Set1'))
	#Pal <- colorRampPalette(brewer.pal(9,'Set1'))
	Pal <- colorRampPalette(c(cols[1],cols[2]))
	#new_map$Col <- Pal(10)[as.numeric(cut(new_map[,map_column],breaks = 10))]
	new_map$Col <- Pal(5)[as.numeric(cut(new_map[,map_column],breaks = 5))]

	#assign pdf name
	file <- c(".pdf")
	name <- paste(trait_name, ".pdf", sep='')
	name <- paste(opts$output, name, sep="/")

	# now save the plot as a pdf h/w 6 inches
	pdf(name, height=4,width=6);
	par(mar=c(3,3,1,0.5), oma=c(0.1,0.1,0.1,0.1), mgp=c(1.5,0.5,0))
	plot(new_traits[,trait] ~ new_map[,map_column],col = new_map$Col,tck=-.02,pch=16,cex=0.8,xaxt='n',xlab='',ylab='Proportion of Microbiome',cex.lab=0.4, cex.axis=0.4,las=1)
	abline(lm.out, lty=2)
	axis(1, cex.axis=0.4, padj=-1.5)
	title(xlab=map_column, cex.lab=0.4, line=1)
	title(main=trait, cex.main=0.4, line=0.5)
	dev.off()

} else {
	# define treatment groups
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

	# show number of samples in each body site and trait
	cat("\nNumber of samples in each treatment group:\n")
	table(new_map[,map_column])

	cat("\nProportion with phenotype (mean):\n")
	tapply(new_traits[,trait], new_map[,map_column], mean)

	cat("\nProportion with phenotype (median):\n")
	tapply(new_traits[,trait], new_map[,map_column], median)

	cat("\nStandard deviation:\n")
	tapply(new_traits[,trait], new_map[,map_column], sd)

	#non-parametric tests - either two classes or multi-class, print to screen and file
	if(length(groups)==2){
		group.pvalue <- wilcox.test(new_traits[,trait] ~ new_map[,map_column])$p.value
		
		cat("\np-value is:\n")
		print(group.pvalue)
		
		cat("FDR-corrected p-value is:\n")
		print(p.adjust(group.pvalue,'fdr'))
		
		outfile <- paste(trait_name, "_stats.txt", sep="")

		sink(paste(opts$output,outfile,sep='/'))

		cat("\nNumber of samples in each treatment group:\n")
		print(table(new_map[,map_column]))

		cat("\nProportion with phenotype (mean):\n")
		print(tapply(new_traits[,trait], new_map[,map_column], mean))

		cat("\nProportion with phenotype (median):\n")
		print(tapply(new_traits[,trait], new_map[,map_column], median))

		cat("\nStandard deviation:\n")
		print(tapply(new_traits[,trait], new_map[,map_column], sd))
		
		cat("\nMann-Whitney-Wilcoxon Test was performed.\n")
		cat("p-values is:\n")
		print(group.pvalue)
		
		cat("\nFDR-corrected p-value is:\n")
		print(p.adjust(group.pvalue,'fdr'))

		sink()
		
	} else {
		group.pvalue <- kruskal.test(new_traits[,trait] ~ new_map[,map_column])$p.value

		# also run pairwise tests if > 2 categories
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

	# get palette 1 from R ColorBrewer
	# set transparency to 44 out of FF
	cols <- sprintf('%s95',brewer.pal(9,'Set1'))

	#assign pdf name
	file <- c(".pdf")
	name <- paste(trait_name, ".pdf", sep='')
	name <- paste(opts$output, name, sep="/")

	#Re-order to plot according to order specified by user (or by default occurance in file)
	new_map[,map_column] <- factor(new_map[,map_column], levels = c(groups))

	# now save the plot as a pdf h/w 6 inches
	pdf(name, height=2,width=3);
	par(mar=c(3,3,0.5,0.5), oma=c(0.1,0.1,0.1,0.1), mgp=c(1.5,0.5,0))
	beeswarm(new_traits[,trait] ~ new_map[,map_column],corral='random',ylim=c(0,1),cex.axis=.4,tck=-.02,pch=16,col=cols,xlab='',ylab='',cex=0.5, cex.lab=0.4, las=2)
	bxplot(new_traits[,trait] ~ new_map[,map_column], add=TRUE, lwd=0.75)
	title(ylab = "Proportion of Microbiome", line = 2, cex.lab = 0.4)
	title(main=trait, cex.main=0.4, line=0)
	dev.off()

}