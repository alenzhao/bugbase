# write trait predictions per OTU and per sample 
# 
# USAGE FROM TERMINAL:
# default:
# Rscript traits_OTU_sample.r -T prediction_input.txt -i 16s_norm_OTUs.txt -o output_directory

library('optparse')

option_list <- list(
    make_option(c("-v", "--verbose"), action="store_true", default=TRUE,
        help="Print extra output [default]"),
	make_option(c("-T", "--trait_table"), type="character", default=NULL,
        help="Prediction input table [default %default]"),
	make_option(c("-i", "--otu_table"), type="character", default=NULL,
        help="16S normalized OTU table [default %default]"),
	make_option(c("-o", "--output"), type="character", default=".",
        help="output directory [default %default]")
)
opts <- parse_args(OptionParser(option_list=option_list))

if(opts$output != "."){
	if(!file.exists(opts$output)){
		dir.create(opts$output, showWarnings = FALSE, recursive = TRUE)
	}
}



#Read in 16S-normalized OTU table
OTUs <- read.table(opts$otu_table, sep='\t',skip=1,head=T,row=1,check=F,comment="")

#Read in trait predictions
traits <- read.table(opts$trait_table,sep='\t',head=T,row=1,check=F,comment="")
names <- names(traits)[2:11]
names(traits) <- names


#Keep only matching OTUs
intersect_btwn <- intersect(rownames(traits),rownames(OTUs))
new_traits <- traits[intersect_btwn,]
new_OTUs <- OTUs[intersect_btwn,]

#Make sample by OTU tables for each trait

for(k in 1:(ncol(new_traits)-1)){
	new_table <- new_OTUs
	for(i in 1:(ncol(new_table))){
		new_table[,i] <- new_table[,i] * new_traits[,k]
		new_table[,i] <- new_table[,i] / sum(new_table[,i])
	}
	trait_name <- ((strsplit(names(new_traits)[k], ".", fixed=TRUE))[[1]])[[1]]
	outfile <- paste(trait_name, "_predictions.txt", sep="")
	outfile <- paste(opts$output,outfile,sep='/')
	write.table(new_table, outfile, sep="\t", quote=F, col.names=NA)
}


