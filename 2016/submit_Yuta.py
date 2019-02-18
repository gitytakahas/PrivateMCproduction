#! /usr/bin/env python
#
# Creating dir:
#   uberftp t3se01.psi.ch 'mkdir /pnfs/psi.ch/cms/trivcat/store/user/ineuteli/samples/LowMassDiTau_madgraph'
#
# Multicore jobs:
#   to submit multicore job:    qsub -pe smp 8 ...
#   in mg_configuration.txt:    run_mode=2 # multicore
#                               nb_core=8
#   note it might wait longer in queue
# 
# Luca v.s Izaak
#   https://www.diffchecker.com/JSVEi5qL

import os, sys, subprocess, time
from optparse import OptionParser

WORKPATH        =  os.getcwd() 

argv = sys.argv
usage = "This script will produce nanoAOD files, starting from GS sample (assuming it is at T3)"

parser = OptionParser(usage=usage,epilog="Success!")

(opts, args) = parser.parse_args(argv)

USER = 'ytakahas'

samples = []

for prod in ['Pair', 'Single', 'NonRes']:
#for prod in ['NonRes']:
#for prod in ['Pair']:
    for mp in [600, 800, 1000, 1200, 1400, 1600, 2000]:
#    for mp in [1000]:
        slist = ("test_LegacyRun2_2016_LQ_" + prod + "_5f_Madgraph_LO_M" + str(mp), "/t3home/ytakahas/work/prod/nanoAOD/legacy_Run2_gridpacks/" + prod + "_M" + str(mp) + "_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz")
        
        samples.append(slist)


print samples


n_cores         = 2

MYPATH = "/pnfs/psi.ch/cms/trivcat/store/user/" + USER

# ensure job report directory
REPORTDIR = "%s/job"%(WORKPATH)
if not os.path.exists(REPORTDIR):
    os.makedirs(REPORTDIR)
    print ">>> made directory " + REPORTDIR


njobs = 0

#nmax = 40000
#nmax = 10000
#nmax = 10
nmax = 250
#nmax = 2


for sample, inputfile in samples:

    cmd_mkdir1 = ("uberftp t3se01.psi.ch 'mkdir " + MYPATH + "/" + sample + "'")
    os.system(cmd_mkdir1)
    
    cmd_mkdir2 = ("uberftp t3se01.psi.ch 'mkdir " + MYPATH + "/" + sample + "/nanoAOD" + "'")
    print '>>>', cmd_mkdir2
    os.system(cmd_mkdir2)

    cmd_mkdir3 = ("uberftp t3se01.psi.ch 'mkdir " + MYPATH + "/" + sample + "/nanoAOD/v1" + "'")
    print '>>>', cmd_mkdir3
    os.system(cmd_mkdir3)

    print '='*80
    print sample, inputfile
    print '='*80


#    for index in range(2000):
    for index in range(1000):
#    for index in range(2):
#    for index in range(20):
#    for index in range(21, 1200):
#    for index in range(2000, 2500):
#    for index in range(30):
#    for index in range(16):
##    for index in range(4):

        jobname = "%s_%s"%(sample, index)

        seed = index + 1
        
#        command = "qsub -q all.q -l h_vmem=6g -pe smp %d -N %s submit_Yuta.sh %s %s %s %s %s" % (n_cores, jobname, sample, index, inputfile, nmax, seed)
        command = "qsub -q all.q -l h_vmem=6g -pe smp %d -N %s submit_Yuta.sh %s %s %s %s %s" % (n_cores, jobname, sample, index, inputfile, nmax, seed)
#        command = "qsub -q pe-test.q -l h_vmem=6g -pe smp %d -N %s submit_Yuta.sh %s %s %s %s %s" % (n_cores, jobname, sample, index, inputfile, nmax, seed)
#        command = "qsub -q pe-test.q -l h_vmem=6g -pe smp %d -N %s submit_Yuta.sh %s %s %s %s %s" % (n_cores, jobname, sample, index, inputfile, nmax, seed)
#        command = "qsub -q  pe-test.q  -pe smp %d -N %s submit_Yuta.sh %s %s %s %s %s" % (n_cores, jobname, sample, index, inputfile, nmax, seed)

        
        print "\n>>> " + command #.replace(jobname,"\033[;1m%s\033[0;0m"%jobname,1)
        
        sys.stdout.write(">>> ")
        sys.stdout.flush()
        os.system(command)
        
        njobs += 1
        
print '>>>\n>>> ' + str(njobs)  + ' done\n'

