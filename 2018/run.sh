SAMPLE="$1"
INDEX="$2"
INPUT="$3"
NMAX="$4"
SEED="$5"



source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630

if [ -r CMSSW_10_2_7/src ] ; then
    echo "release CMSSW_10_2_7 already exists"
else
    scram p CMSSW CMSSW_10_2_7
fi

cd CMSSW_10_2_7/src
eval `scram runtime -sh`
cd -

echo 'cmssw release = ' $CMSSW_BASE

echo "--------------------------"
echo "sample name = $SAMPLE"
echo "index = $INDEX"
echo "input file = $INPUT"
echo "max events = $NMAX"
echo "skip events = $SEED"
echo "--------------------------"

echo "================= [LOG] GS step1 starts ===================="
cmsRun GS_step1_template.py $SAMPLE $INDEX $INPUT $NMAX $SEED
echo "================= [LOG] GS step1 ends ===================="


if [ -r CMSSW_10_2_5/src ] ; then
    echo "release CMSSW_10_2_5 already exists"
else
    scram p CMSSW CMSSW_10_2_5
fi

cd CMSSW_10_2_5/src
eval `scram runtime -sh`
cd -

echo 'cmssw release = ' $CMSSW_BASE


echo "================= [LOG] DR step1 starts ===================="
cmsRun DR_step1_template.py $SAMPLE $INDEX
echo "================= [LOG] DR step1 ends ===================="

#echo "removing GS sample ..."
rm GS_${SAMPLE}_${INDEX}.root

echo "================= [LOG] DR step2 starts ===================="
cmsRun DR_step2_template.py $SAMPLE $INDEX
echo "================= [LOG] DR step2 ends ===================="

echo "removing DR step1 sample ..."
rm DR_step1_${SAMPLE}_${INDEX}.root


echo "================= [LOG] miniAOD starts ===================="
cmsRun miniAOD_template.py $SAMPLE $INDEX
echo "================= [LOG] miniAOD ends ===================="

echo "removing DR step2 sample ..."
rm DR_step2_${SAMPLE}_${INDEX}.root



if [ -r CMSSW_10_2_9/src ] ; then
    echo "release CMSSW_10_2_9 already exists"
else
    scram p CMSSW CMSSW_10_2_9
fi

cd CMSSW_10_2_9/src
eval `scram runtime -sh`
cd -

echo 'cmssw release = ' $CMSSW_BASE

echo "================= [LOG] nanoAOD starts ===================="
cmsRun nanoAOD_template.py $SAMPLE $INDEX
echo "================= [LOG] nanoAOD ends ===================="

echo "removing DR step2 sample ..."
rm miniAOD_${SAMPLE}_${INDEX}.root