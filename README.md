# Usage:

# get bugbase
https://github.com/danknights/bugbase/archive/master.zip

# add the right paths to your ~/.bash_profile
# note: this is what is in an example ~/.bash_profile
# you will need change paths
# you might need to put it in ~/.bashrc
export PYTHONPATH=$PYTHONPATH:/Users/me/lib/picrust
export PATH=$PATH:/Users/me/lib/picrust/scripts
export BUGBASE_PATH=/Users/me/lib/bugbase/
export PATH=$PATH:/Users/me/lib/bugbase/bin

# after adding these paths to the .bash_profile, run this
# or reopen the terminal/login again
source ~/.bash_profile

# You need R and you need the "beeswarm" package installed:
R
install.packages('beeswarm', repos='http://cran.mtu.edu')
quit()


# now change into the bugbase/doc/data directory, and run:
analyze_bugs.py -i HMP_s15.biom -m HMP_map.txt -c HMPBODYSUBSITE -o output

=======
