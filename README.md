## BugBase Usage and Installation

### Dependencies
* R: http://cran.r-project.org/
* The R "beeswarm" package, which can be installed by running this command in R: `install.packages('beeswarm')`
* PICRUSt: http://picrust.github.io/picrust/install.html

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

=======
