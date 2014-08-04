# tables a vector of categories for taxa, summarizes sample counts 
# functions must be a vector of categories named with taxon names
"summarize.by.category" <- function(taxa, functions){
	# get only overlapping feature names
	features <- intersect(colnames(taxa),names(functions))
	
	if(length(features) < 2) stop('Too few features overlap between functions and taxa')
	taxa <- taxa[,features]
	functions <- functions[features]
	
	function.types <- sort(unique(functions))
	res <- matrix(0,nrow(taxa),length(function.types))
	rownames(res) <- rownames(taxa)
	colnames(res) <- function.types
	for(function.type in function.types){
		function.ix <- functions == function.type
		res[,function.type] <- rowSums(taxa[,function.ix,drop=F])
	}
	res[res > 1] <- 1
	res[res < 0] <- 0
	
	return(res)
}