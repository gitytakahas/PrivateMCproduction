# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/BTV-RunIIFall17wmLHEGS-00006-fragment.py --fileout file:BTV-RunIIFall17wmLHEGS-00006.root --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN,SIM --nThreads 8 --geometry DB:Extended --era Run2_2017 --python_filename BTV-RunIIFall17wmLHEGS-00006_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 2029
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

import sys
args = sys.argv

print '.............. enter GS_step1_template.py ............'

lhe = 'None'
nmax = 1

if len(args)!=7:
    print 'Provide [sample][index][lhe file][nmax][seed]', len(args)
    sys.exit(0)
else:
    sample = args[2]
    index = args[3]
    lhe = args[4]
    nmax = int(args[5])
    seed = int(args[6])



print 'sample name = ', sample
print 'index = ', index
print 'LHE file = ', lhe
print 'nmax = ', nmax
print 'seed = ', seed



process = cms.Process('SIM',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2017Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(nmax)
#    input = cms.untracked.int32(2029)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/BTV-RunIIFall17wmLHEGS-00006-fragment.py nevts:2029'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
#    fileName = cms.untracked.string('file:BTV-RunIIFall17wmLHEGS-00006.root'),
    fileName = cms.untracked.string("file:GS_" + sample + "_" + index + ".root"),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

#process.LHEoutput = cms.OutputModule("PoolOutputModule",
#    dataset = cms.untracked.PSet(
#        dataTier = cms.untracked.string('LHE'),
#        filterName = cms.untracked.string('')
#    ),
#    fileName = cms.untracked.string('file:BTV-RunIIFall17wmLHEGS-00006_inLHE.root'),
#    outputCommands = process.LHEEventContent.outputCommands,
#    splitLevel = cms.untracked.int32(0)
#)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
#from Configuration.Generator.MCTunes2017.PythiaCP2Settings_cfi import *

process.GlobalTag = GlobalTag(process.GlobalTag, '93X_mc2017_realistic_v3', '')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythia8CommonSettings', 
                                    'pythia8CP2Settings'),
#            'pythia8CP5Settings'), 
#        pythia8CP5Settings = cms.vstring('Tune:pp 14', 
#            'Tune:ee 7', 
#            'MultipartonInteractions:ecmPow=0.03344', 
#            'PDF:pSet=20', 
#            'MultipartonInteractions:bProfile=2', 
#            'MultipartonInteractions:pT0Ref=1.41', 
#            'MultipartonInteractions:coreRadius=0.7634', 
#            'MultipartonInteractions:coreFraction=0.63', 
#            'ColourReconnection:range=5.176', 
#            'SigmaTotal:zeroAXB=off', 
#            'SpaceShower:alphaSorder=2', 
#            'SpaceShower:alphaSvalue=0.118', 
#            'SigmaProcess:alphaSvalue=0.118', 
#            'SigmaProcess:alphaSorder=2', 
#            'MultipartonInteractions:alphaSvalue=0.118', 
#            'MultipartonInteractions:alphaSorder=2', 
#            'TimeShower:alphaSorder=2', 
#            'TimeShower:alphaSvalue=0.118'),


    pythia8CP2Settings = cms.vstring(
            'Tune:pp 14',
            'Tune:ee 7',
            'MultipartonInteractions:ecmPow=0.1391',
            'PDF:pSet=17',
            'MultipartonInteractions:bProfile=2',
            'MultipartonInteractions:pT0Ref=2.306',
            'MultipartonInteractions:coreRadius=0.3755',
            'MultipartonInteractions:coreFraction=0.3269',
            'ColourReconnection:range=2.323',
            'SigmaTotal:zeroAXB=off', 
            'SpaceShower:rapidityOrder=off',
            'SpaceShower:alphaSvalue=0.13',
            'TimeShower:alphaSvalue=0.13',
            ),
        

        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on')
    ),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
#    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/DYJetsToLL_M-10to50/DYJetsToLL_M-10to50_13TeV-madgraphMLM-pythia8_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'),
    args = cms.vstring(lhe),
    nEvents = cms.untracked.uint32(nmax),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

process.RandomNumberGeneratorService.externalLHEProducer.initialSeed = seed

# Path and EndPath definitions
process.lhe_step = cms.Path(process.externalLHEProducer)
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)
#process.LHEoutput_step = cms.EndPath(process.LHEoutput)

# Schedule definition
#process.schedule = cms.Schedule(process.lhe_step,process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step,process.LHEoutput_step)
process.schedule = cms.Schedule(process.lhe_step,process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(2)
process.options.numberOfStreams=cms.untracked.uint32(0)
# filter all path with the production filter sequence
for path in process.paths:
	if path in ['lhe_step']: continue
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
