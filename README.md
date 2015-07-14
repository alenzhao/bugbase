## BugBase Usage and Installation

### Dependencies
BugBase is written in python and has been tested on Mac OS X and Linux systems.  To install BugBase, first you must install it’s dependencies, listed below.

These can be installed with `python setup.py install:`
* python (version 2.7)
* pycogent (version 1.5.3)
* biom (version 1.3.1)

This can be installed manually with `pip install numpy==1.5.1`
* numpy (version 1.5.1)

Follow the website directions to install:
* R (http://cran.r-project.org)
* PICRUSt (http://picrust.github.io/picrust/install.html)

These R packages can be installed with this command in R: `install.packages(‘package’)`
* APE
* Optparse
* Beeswarm
* RColorBrewer

### Installation
To get the current development version of bugbase, download and extract this file:
https://github.com/danknights/bugbase/archive/master.zip

Then add these paths to your `~/.bash_profile` file. This is what is in an example `~/.bash_profile` file looks like:

```
export BUGBASE_PATH=/Users/me/lib/bugbase/
export PATH=$PATH:/Users/me/lib/bugbase/bin
```

Note: you will need change the paths to match your system. You might need to put it in ~/.bashrc instead of ~/.bash_profile depending on your system. After adding these paths to the .bash_profile or ~/.bashrc, reopen the terminal or login again.

### Demo
You can now change into the bugbase/doc/data directory, and run this command on the demo data:
`analyze_bugs.py -i HMP_s15.biom -m HMP_map.txt -c HMPBODYSUBSITE -o output`

You can view other options with `analyze_bugs.py -h`.

### Using BugBase 

BugBase has one main command, `analyze_bugs.py`, that will:
-	Normalize your OTU table according to 16S copy number
-	Plot the variance in phenotype possession for each treatment group at various thresholds
-	Determine which threshold to set for each microbiome phenotype
-	Deterimine the proportion of each microbiome with a given phenotype
-	Plot the proportions of the microbiome with a given phenotype
-	Statistical analyze those phenotype proportions (Mann Whitney U Test) according the treatment groups specified

Inputs:
- OTU table in biom format, picked against the GreenGenes database (.biom)
- Mapping file in tab-delimited text format (.txt)

	
Required:
<dl>
	<dt>Required</dt>
	<dd> -i     input OTU table (BIOM format)<\dd>
	<dd> -m     mapping file (tab-delimitted text file)<\dd>
	<dd> -c     map column header to plot by (which column denotes treatment groups)<\dd>
	<dd> -o     output directory name<\dd>
	
	<dt>Optional</dt>
	<dd> -t     Threshold value (integer, 0 - 100) you would like to set for all phenotypes<\dd>
	<dd> -g     Which treatment groups you would like to plot, comma-separated with no spaces<\dd>
	<dd> -a     Plot all samples without using a mapping file (no statistical analyses will be done)<\dd>
</dl>



=======
