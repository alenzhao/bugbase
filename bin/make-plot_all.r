# Plot phenotype predictions for all samples
# 
# USAGE FROM TERMINAL:
# default:
# Rscript make-plot.r -T predicted_traits.txt -o output_file

library('optparse')
library('beeswarm')

# Make option list and parse command line
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

# Transpose because samples were in the columns
traits <- t(traits)

cat("\n\n RESULTS: \n\n")

# check dimensions of trait table
cat("\ndimensions of trait table:\n")
dim(traits)

# Define trait to test
trait <- c(opts$trait)
trait_name <- trait_name <- ((strsplit(trait, ".", fixed=TRUE))[[1]])[[1]]

# Output the mean/median phenotype abundance
outfile <- paste(trait_name, "_stats.txt", sep="")	

sink(paste(opts$output, outfile,sep='/'))

cat("mean proportion with this trait is:\n")
print(mean(traits[,trait]))

cat("median proportion with this trait is:\n")
print(median(traits[,trait]))


sink()

# Get the Set1 color palette, and set transparency to 65%
library('RColorBrewer')
cols <- sprintf('%s65',brewer.pal(9,'Set1'))

# Assign pdf name
file <- c(".pdf")
name <- paste(trait[1], ".pdf", sep='')
name <- paste(opts$output, name, sep="/")
# note you can also use sprintf - google for formatting
# name <- sprintf('%s_%d.pdf',trait[1],length(groups))

# Save the plot as a pdf h/w 6 inches
pdf(name, height=6,width=6);
par(mar=c(8,5,1,1), oma=c(0.5,0.5,0.5,0.5))
beeswarm(traits[,trait],corral='random',cex.axis=.55,pch=16,col=cols, xlab='',ylab='Proportion of Microbiome',cex=1, cex.lab=0.65, las=2)
bxplot(traits[,trait], add=TRUE)
dev.off()