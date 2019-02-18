SAMPLE="$1"
INDEX="$2"
INPUT="$3"
NMAX="$4"
SEED="$5"



source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630

if [ -r CMSSW_9_3_6 ] ; then
    echo "release CMSSW_7_1_26 already exists"
else
    scram p CMSSW CMSSW_9_3_6
fi

cd CMSSW_9_3_6/src
eval `scram runtime -sh` 
cd -


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

if [ -r CMSSW_9_4_0_patch1/src ] ; then
    echo "release CMSSW_8_0_21 already exists"
else
    scram p CMSSW CMSSW_9_4_0_patch1
fi

cd CMSSW_9_4_0_patch1/src
eval `scram runtime -sh`
cd -


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


if [ -r CMSSW_9_4_6_patch1/src ] ; then
    echo "release CMSSW_8_0_21 already exists"
else
    scram p CMSSW CMSSW_9_4_6_patch1
fi

cd CMSSW_9_4_6_patch1/src
eval `scram runtime -sh`
cd -


echo "================= [LOG] miniAOD starts ===================="
cmsRun miniAOD_template.py $SAMPLE $INDEX
echo "================= [LOG] miniAOD ends ===================="

echo "removing DR step2 sample ..."
rm DR_step2_${SAMPLE}_${INDEX}.root


echo "================= [LOG] nanoAOD starts ===================="
cmsRun nanoAOD_template.py $SAMPLE $INDEX
echo "================= [LOG] nanoAOD ends ===================="

echo "removing DR step2 sample ..."
rm miniAOD_${SAMPLE}_${INDEX}.root