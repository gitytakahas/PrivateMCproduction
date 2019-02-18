#! /bin/bash

SAMPLE="$1" # e.g. "LowMassMuMu_13TeV"
INDEX="$2"  # index
INPUT="$3"   # input
NMAX="$4"
NSKIP="$5"

echo "sample = $SAMPLE"
echo "index = $INDEX"
echo "input = $INPUT"
echo "nmax = $NMAX"
echo "nskip = $NSKIP"

SEOUTFILES="nanoAOD*.root"
#SEOUTFILES="miniAOD*.root"

DBG=2
#JOBLOGFILES="myout.txt myerr.txt"
JOBLOGFILES="myout.txt"
BASEDIR="/t3home/ytakahas/work/prod/nanoAOD/2018"
XROOTD="root://t3dcachedb.psi.ch:1094"
SE_HOME="/pnfs/psi.ch/cms/trivcat/store/user/$USER"
JOBDIR="nanoAOD_${SAMPLE}_${INDEX}"


WORKDIR=/scratch/$USER/$SAMPLE/$JOBDIR
#OUTDIR=$WORKDIR/ # where SEOUTFILES are generated # TODO
#RESULTDIR="$BASEDIR/submit/"
REPORTDIR="$BASEDIR/job/"
SERESULTDIR="$SE_HOME/${SAMPLE}/nanoAOD/v1/" # TODO



##### MONITORING/DEBUG INFORMATION ########################################

mkdir -p $REPORTDIR
#$ -e /t3home/ytakahas/work/prod/nanoAOD/2018/job/
#$ -o /t3home/ytakahas/work/prod/nanoAOD/2018/job/

DATE_START=`date +%s`
echo "Job started at " `date`
cat <<EOF

###########################################
##       QUEUEING SYSTEM SETTINGS:       ##
###########################################
  HOME=$HOME
  USER=$USER
  JOB_ID=$JOB_ID
  JOB_NAME=$JOB_NAME
  HOSTNAME=$HOSTNAME
  TASK_ID=$TASK_ID
  QUEUE=$QUEUE
EOF


##### SET ENVIRONMENT #####################################################

if test -e "$WORKDIR"; then
   echo "ERROR: WORKDIR ($WORKDIR) already exists!" >&2
   echo "ls $TOPWORKDIR"
   echo `ls $TOPWORKDIR` >&22
   echo "ls $WORKDIR"
   echo `ls $WORKDIR` >&2
   #exit 1
fi
mkdir -p $WORKDIR
if test ! -d "$WORKDIR"; then
   echo "ERROR: Failed to create workdir ($WORKDIR)! Aborting..." >&2
   exit 1
fi

cat <<EOF

###########################################
##             JOB SETTINGS:             ##
###########################################
  STARTDIR=$STARTDIR
  BASEDIR=$BASEDIR
  WORKDIR=$WORKDIR
  RESULTDIR=$RESULTDIR
  REPORTDIR=$REPORTDIR
  SERESULTDIR=$SERESULTDIR
EOF




# CMSSW
#source $VO_CMS_SW_DIR/cmsset_default.sh 2>> myerr.txt
#cd $BASEDIR
#eval `scramv1 runtime -sh` >> myout.txt 2>> myerr.txt
#if test $? -ne 0; then
#    echo "ERROR: Failed to source scram environment" >&2
#    exit 1
#fi


# Main script
cd $WORKDIR
cp $BASEDIR/run.sh .
cp $BASEDIR/GS_step1_template.py .
cp $BASEDIR/DR_step1_template.py .
cp $BASEDIR/DR_step2_template.py .
cp $BASEDIR/miniAOD_template.py .
cp $BASEDIR/nanoAOD_template.py .

echo "start jobs ----"

CMD="source run.sh $SAMPLE $INDEX $INPUT $NMAX $NSKIP 2>&1 | tee myout.txt"
echo $CMD
$CMD
echo done

echo "---- end jobs ----"

mv nanoAOD.root nanoAOD_${SAMPLE}_${INDEX}.root 
#mv miniAOD.root miniAOD_${SAMPLE}_${INDEX}.root 

echo "change miniAOD file name"




##### RETRIEVAL OF OUTPUT FILES AND CLEANING UP ###########################

cd $WORKDIR
if test x"$JOBLOGFILES" != x; then
    mkdir -p $REPORTDIR
    if test ! -e "$REPORTDIR"; then
        echo "ERROR: Failed to create $REPORTDIR ...Aborting..." >&2
        exit 1
    fi
    for n in $JOBLOGFILES; do
        echo ">>> copying $n"
        if test ! -e $WORKDIR/$n; then
            echo "WARNING: Cannot find output file $WORKDIR/$n. Ignoring it" >&2
        else
            cp -a $WORKDIR/$n $REPORTDIR/${SAMPLE}_${INDEX}_$n
            if test $? -ne 0; then
                echo "ERROR: Failed to copy $WORKDIR/$n to $REPORTDIR/${SAMPLE}_$n" >&2
            fi
        fi
    done
fi

cd $WORKDIR
if test x"$SEOUTFILES" != x; then
    if test 0"$DBG" -ge 2; then
        debug="-v"
    fi
#    if [[ ! -d $SERESULTDIR ]]; then
#        echo ">>> $SERESULTDIR does not exist!" >&2
#        echo "uberftp t3se01.psi.ch 'mkdir $SERESULTDIR'"
#        uberftp t3se01.psi.ch 'mkdir $SERESULTDIR'
#    fi
    for n in `ls $SEOUTFILES`; do
        echo ">>> copying $WORKDIR/$n to $SERESULTDIR/$n"
        echo "xrdcp -d $DBG $debug --force $WORKDIR/$n $XROOTD/$SERESULTDIR/$n >&2"
        xrdcp -d $DBG $debug --force $WORKDIR/$n $XROOTD/$SERESULTDIR/$n >&2
        if test $? -ne 0; then
            echo "ERROR: Failed to copy $WORKDIR/$n to $SERESULTDIR/$n" >&2
        fi
    done
fi

echo "Cleaning up $WORKDIR"
rm -rf $WORKDIR



###########################################################################

DATE_END=`date +%s`
RUNTIME=$((DATE_END-DATE_START))
echo " "
echo "#####################################################"
echo "    Job finished at " `date`
echo "    Wallclock running time: $(( $RUNTIME / 3600 )):$(( $RUNTIME % 3600 /60 )):$(( $RUNTIME % 60 )) "
echo "#####################################################"
echo " "

exit 0


