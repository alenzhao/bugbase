# input: character vector; each is a document
# output: list of 2-row matrices for input to LDA package
"format.doc.term.mtx.for.lda" <- function(x, verbose=FALSE){
	res = list()
	for(i in 1:nrow(x)){
		if(verbose && i %% 100 == 0) cat(i,'')
		xi <- as.numeric(x[i,])
		ix <- which(xi > 0)
				
		res.i <- matrix(0,2,length(ix))
		res.i[1,] <- ix - 1
		res.i[2,] <- xi[ix]
		res.i <- apply(res.i, 2, as.integer)		
		res[[i]] <- res.i
				
	}
	if(verbose) cat('\n')
	return(res)
}


"topic.term.rar" <- function(topics){
	pwt <- sweep(topics, 1, rowSums(topics),'/')
	ptw <- sweep(topics, 2, colSums(topics),'/')
	rar <- sqrt(pwt * ptw)
}

"prob.topic.given.term" <- function(topics){
	ptw <- sweep(topics, 2, colSums(topics),'/')
	ptw[is.nan(ptw)] <- 0
	return(ptw)
}


# returns ix of topics with highest rar for given term
"top.topics.for.term" <- function(rar, term, min.rar=0.01){
	ix <- order(rar[,term],decreasing=TRUE)
	ix <- ix[rar[ix,term] > min.rar]
	if(length(ix) == 0) return(NULL)
	return(ix)
}

"display.topics" <- function(rar, ix=NULL, n.display=15){
	if(is.null(ix)) ix <- 1:nrow(rar)
	top.words <- sapply(ix, function(ixx) {xx <- rar[ixx,]; colnames(rar)[rev(order(xx))][1:n.display]})
	return(top.words)
}

# if cross.ref is a vocab word, includes links only to docs containing that word 
"display.topics.html" <- function(topics, docs, cross.ref=NULL,
		cross.ref.min.cooccur=0.001, ix=NULL, n.display=15, n.docs.link=100, filename='topics.html',
		exclude.topics=NULL){
	rar <- topic.term.rar(topics)
	ptw <- prob.topic.given.term(topics)

	# weight of topics in documents
	etd <- ptw %*% t(docs)
	etd <- sweep(etd, 2, rowSums(docs),'/')
	etw <- etd %*% x # co-occurrence topic-word
	etw <- sweep(etw,2,colSums(x),'/')
	
	# filter by cross.ref
	if(is.null(cross.ref)){
		doc.ix <- 1:nrow(docs)
 		topic.order <- rev(order(apply(rar,1,max)))

	} else {
		cross.ref.case <- cross.ref
		cross.ref <- tolower(cross.ref)
		doc.ix <- which(docs[,cross.ref] > 0)
		topic.order <- which(etw[,cross.ref] > cross.ref.min.cooccur)
		topic.order <- topic.order[rev(order(etw[topic.order,cross.ref]))]
	}

 	top.docs <- top.documents.per.topic(rar, docs, n.display=NULL)
	
	max.font <- 6
	min.font <- 3
	n.colors <- 10
	
	if(is.null(ix)) ix <- 1:nrow(rar)
	top.words <- display.topics(rar,ix=ix,n.display=n.display)
	rar.top.words <- sapply(ix, function(ixx) {xx <- rar[ixx,]; rev(sort(xx))[1:n.display]})

	# precalc font sizes
	fontsizes <- rar.top.words
	fontsizes <- sweep(fontsizes,2,apply(fontsizes,2,min),'-')
	fontsizes <- sweep(fontsizes,2,1/apply(fontsizes,2,max) * (max.font - min.font),'*')
	fontsizes <- round(fontsizes + min.font)

	fontcolor.options <- rev(colorRampPalette(c('#000000','#bbbbbb'))(n.colors))
	fontcolors <-  rar.top.words
	fontcolors <- sweep(fontcolors,2,apply(fontcolors,2,min),'-')
	fontcolors <- sweep(fontcolors,2,1/apply(fontcolors,2,max) * (n.colors-1),'*')
	fontcolors <- round(fontcolors + 1)

	res <- NULL
	res <- c(res,'<html><body style="width:80%; margin:0px auto; margin-top: 20px; margin-bottom: 40px;">\n')
	if(!is.null(cross.ref)) res <- c(res,sprintf('<h2>Topics discussing %s</h2>',cross.ref.case))
	if(!is.null(exclude.topics)) topic.order <- topic.order[!(topic.order %in% exclude.topics)]
	# sort topics by max rar
	for(i in topic.order){
		res <- c(res,sprintf('<font size=5>%d. </font>',i))
		top.docs.i <- top.docs[,i]

		if(!is.null(cross.ref))	top.docs.i <- cross.reference(docs,top.docs.i,cross.ref)
		for(j in 1:nrow(top.words)){
			top.docs.i.j <- cross.reference(docs, top.docs.i, top.words[j,i])
			if(n.docs.link < length(top.docs.i.j)) top.docs.i.j <- top.docs.i.j[1:n.docs.link]
			if(length(top.docs.i.j) > 0) url <- doc.IDs.to.URL(top.docs.i.j)
			res <- c(res,sprintf('<font size="%d" color="%s">',
				round(fontsizes[j,i]),
				fontcolor.options[round(fontcolors[j,i])])
			)
			if(length(top.docs.i.j) > 0) res <- c(res,sprintf('<a href="%s">',url))
			res <- c(res,top.words[j,i])
			if(length(top.docs.i.j) > 0) res <- c(res,'</a>')
			res <- c(res,'</font>')
		}
		res <- c(res,'<br>')
	}
	res <- c(res,'</body></html>')
	if(!is.null(filename)){
		sink(filename)
		cat(paste(res,collapse='\n'))
		sink(NULL)
	} else {
		return(paste(res,collapse='\n'))
	}
}


"make.topic.wordle.text" <- function(topics, docs, size=10000, n.display=200){
	rar <- topic.term.rar(topics)
	top.words <- display.topics(rar,n.display=n.display)
	rar.top.words <- sapply(1:nrow(rar), function(ixx) {xx <- rar[ixx,]; rev(sort(xx))[1:n.display]})

	for(i in 1:nrow(rar)){
		sink(sprintf('wordle_text_topic_%d.txt',i))
		cat(sample(top.words[,i],size=1000, prob=rar[i,top.words[,i]],replace=TRUE),sep='\n')
		sink(NULL)
	}
}



# makes top-level html page listing genera
"make_genera_html" <- function(topics, docs, 
			n.terms.display=25, n.docs.link=20,
			genera.file='genera.txt',filename='genera.html',
			exclude.topics=NULL,
			verbose=FALSE){
	genera <- scan(genera.file,w='c')
	res <- '<html><body style="width:80%; margin:0px auto; margin-top: 20px; margin-bottom: 40px;">\n'
	res <- c(res,'<h2>Genera:</h2>')
	
	for(genus in genera){
		genus.lower <- tolower(genus)
		genus <- paste(toupper(substring(genus,1,1)),substring(genus,2),sep='')
		if(verbose) cat(genus,'')
		if(genus.lower %in% colnames(docs)){
			filename.i <- sprintf('genera-%s.html',genus.lower)
			display.topics.html(topics,docs,cross.ref=genus,n.docs.link=n.docs.link,n.display=n.terms.display,filename=filename.i,exclude.topics=exclude.topics)
			res <- c(res,sprintf('<a href="%s">%s</a></br>',filename.i,genus))
		}
	}
	if(verbose) cat('\n')
	res <- c(res,'</body></html>')
	if(!is.null(filename)){
		sink(filename)
		cat(paste(res,collapse='\n'))
		sink(NULL)
	} else {
		return(paste(res,collapse='\n'))
	}
}


# returns table of documents with highest representation of given topic
"top.documents.per.topic" <- function(topics, docs, ix=NULL, n.display=15, as.url=FALSE){
	if(is.null(ix)) ix <- 1:nrow(topics)
	ptw <- prob.topic.given.term(topics)
	
	# expected number of words in document
	etd <- ptw %*% t(docs)
	# expected fraction of document from each topic
	etd <- sweep(etd, 2, rowSums(docs),'/')
	
	top.docs <- sapply(ix, function(ixx) {xx <- etd[ixx,]; colnames(etd)[rev(order(xx))]})
	if(!is.null(n.display)) top.docs <- top.docs[,1:n.display]
	if(as.url){
		urls <- NULL
		for(i in 1:ncol(top.docs)){
			urls <- c(urls,doc.IDs.to.URL(top.docs[,i]))
		}
		return(urls)
	}

	return(top.docs)
}

# converts list of document IDs to URL
"doc.IDs.to.URL" <- function(IDs){
	words <- "http://www.ncbi.nlm.nih.gov/pubmed/?term="
	words <- c(words, paste(IDs,collapse="%5Buid%5D++OR+"))
	words <- c(words,'%5Buid%5D')
	return(paste(words,collapse=''))
}

# returns subset of documents containing given term
"cross.reference" <- function(docs, IDs, cross.ref){
	IDs <- IDs[docs[IDs,cross.ref] > 0]
	return(IDs)
}