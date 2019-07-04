# python shell script

import os

#!/bin/bash

#matlab=/Applications/MATLAB_R2014b.app/bin/matlab

#echo $matlab

#$matlab -nodesktop -nojvm -nosplash  -r "A = [2 1; 1 1]; disp(eig(A)); exit(0);"

os.system("latex figures")

# Initial set of figures
for i in range(1,1+1):
    s = "%02d" % i
    os.system("dvips -Ppdf -E -p{} -l{} -o MKMO_hetclin_fig{}.eps figs_hetcycle.dvi".format(i,i,s))

# Figures with non-standard names, at end.
# os.system("dvips -Ppdf -E -p12 -l12 -o fig7A.eps figs.dvi")
# os.system("dvips -Ppdf -E -p13 -l13 -o fig00.eps figs.dvi")
# os.system("dvips -Ppdf -E -p14 -l14 -o figRH.eps figs.dvi")
# os.system("dvips -Ppdf -E -p15 -l15 -o fig11_variant.eps figs.dvi")

# compile paper (note is currently using wrong name!)

#name = "het_cycle_poincare"
#os.system("latex {}".format(name))
#os.system("dvipdf {}".format(name))





#Here's a useful comment.  Get yourself into the directory you're wanting to work in.  Get a .dvi file by running the figures.tex file in the terminal.
latex figures.tex
#just use this command for each figure after you've converted your figures file to .dvi format.  This command is for the figures on page 3.  Do not change the l bit.
dvips -Ppdf -E -p1 -l1 -o ./figures/MKMO_figure_1.eps figures.dvi