### configuration file to re-run customized HLT Menu on RAW
###
### command-line arguments
###
import FWCore.ParameterSet.VarParsing as vpo
opts = vpo.VarParsing('analysis')

opts.register('skipEvents', 0,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of events to be skipped')

opts.register('numThreads', 1,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of threads')

opts.register('numStreams', 1,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of streams')

opts.register('gt', None,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'argument of process.GlobalTag.globaltag')

opts.register('logs', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'create log files configured via MessageLogger')

opts.register('reco', 'hltPhase2_TRKv06',
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'Which tracking version to run')

opts.register('outName', 'JetTree_mc.root',
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'Name of the output root file')

opts.register('wantSummary', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'show cmsRun summary at job completion')

opts.register('dumpPython', None,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'Path to python file with content of cms.Process')

opts.register('trkdqm', True,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'added monitoring histograms for selected Tracks and Vertices')

opts.register('L1', True,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'run L1 trigger')

opts.register('BTVreco', 'default',
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'which reco to load for BTV sequence, default = default')

opts.register('pfdqm', True,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'added monitoring histograms for selected PF-Candidates')



opts.parseArguments()

# flag: skim original collection of generalTracks (only tracks associated to first N pixel vertices)
opt_skimTracks = False

opt_reco = opts.reco
if opt_reco.endswith('_skimmedTracks'):
   opt_reco = opt_reco[:-len('_skimmedTracks')]
   opt_skimTracks = True

if opt_reco == 'hltPhase2_TRKv00':
   from RecoBTag.PerformanceMeasurements.Configs.hltPhase2_TRKv00_cfg import cms, process
elif opt_reco == 'hltPhase2_TRKv02':
   from RecoBTag.PerformanceMeasurements.Configs.hltPhase2_TRKv02_cfg import cms, process
elif opt_reco == 'hltPhase2_TRKv06':
   from RecoBTag.PerformanceMeasurements.Configs.hltPhase2_TRKv06_cfg import cms, process
elif opt_reco == 'hltPhase2_TRKv00_TICL':
   from RecoBTag.PerformanceMeasurements.Configs.hltPhase2_TRKv00_TICL_cfg import cms, process
elif opt_reco == 'hltPhase2_TRKv02_TICL':
   from RecoBTag.PerformanceMeasurements.Configs.hltPhase2_TRKv02_TICL_cfg import cms, process
elif opt_reco == 'hltPhase2_TRKv06_TICL':
   from RecoBTag.PerformanceMeasurements.Configs.hltPhase2_TRKv06_TICL_cfg import cms, process
else:
   raise RuntimeError('invalid argument for option "reco": "'+opt_reco+'"')

opt_BTVreco = opts.BTVreco
if opt_BTVreco == 'default':
      from RecoBTag.PerformanceMeasurements.Configs.hltPhase2_BTV import customize_hltPhase2_BTV
      process = customize_hltPhase2_BTV(process)
elif opt_BTVreco == 'cutsV1':
      from RecoBTag.PerformanceMeasurements.Configs.hltPhase2_BTV_cuts import customize_hltPhase2_BTV
      process = customize_hltPhase2_BTV(process)
else:
   raise RuntimeError('invalid argument for option "BTVreco": "'+opt_BTVreco+'"')





# reset path to EDM input files
process.source.fileNames = []
process.source.secondaryFileNames = []

# skimming of tracks
if opt_skimTracks:
   from JMETriggerAnalysis.Common.hltPhase2_skimmedTracks import customize_hltPhase2_skimmedTracks
   process = customize_hltPhase2_skimmedTracks(process)

if opts.L1:
   from JMETriggerAnalysis.Common.hltPhase2_L1 import customize_hltPhase2_L1
   process = customize_hltPhase2_L1(process)

# if opts.FastPV:
#     process.noFilter_PFDeepCSV = cms.Path(process.HLTBtagDeepCSVSequencePFFastPV)
#     process.noFilter_PFProba = cms.Path(process.HLTBtagProbabiltySequencePFFastPV)
#     process.noFilter_PFBProba = cms.Path(process.HLTBtagBProbabiltySequencePFFastPV)
#     process.noFilter_PFDeepCSVPuppi = cms.Path(process.HLTBtagDeepCSVSequencePFPuppiFastPV)
#     process.noFilter_PFProbaPuppi = cms.Path(process.HLTBtagProbabiltySequencePFPuppiFastPV)
#     process.noFilter_PFBProbaPuppi = cms.Path(process.HLTBtagBProbabiltySequencePFPuppiFastPV)
# else:
process.noFilter_PFDeepCSV = cms.Path(process.HLTBtagDeepCSVSequencePF)
process.noFilter_PFProba = cms.Path(process.HLTBtagProbabiltySequencePF)
process.noFilter_PFBProba = cms.Path(process.HLTBtagBProbabiltySequencePF)
process.noFilter_PFDeepCSVPuppi = cms.Path(process.HLTBtagDeepCSVSequencePFPuppi)
process.noFilter_PFProbaPuppi = cms.Path(process.HLTBtagProbabiltySequencePFPuppi)
process.noFilter_PFBProbaPuppi = cms.Path(process.HLTBtagBProbabiltySequencePFPuppi)

process.schedule.extend([process.noFilter_PFDeepCSV, process.noFilter_PFProba, process.noFilter_PFBProba])
process.schedule.extend([process.noFilter_PFDeepCSVPuppi, process.noFilter_PFProbaPuppi, process.noFilter_PFBProbaPuppi])


# max number of events to be processed
process.maxEvents.input = opts.maxEvents

# number of events to be skipped
process.source.skipEvents = cms.untracked.uint32(opts.skipEvents)

# multi-threading settings
process.options.numberOfThreads = cms.untracked.uint32(opts.numThreads if (opts.numThreads > 1) else 1)
process.options.numberOfStreams = cms.untracked.uint32(opts.numStreams if (opts.numStreams > 1) else 1)

# show cmsRun summary at job completion
process.options.wantSummary = cms.untracked.bool(opts.wantSummary)

# MessageLogger
if opts.logs:
   process.MessageLogger = cms.Service('MessageLogger',
     destinations = cms.untracked.vstring(
       'cerr',
       'logError',
       'logInfo',
       'logDebug',
     ),
     # scram b USER_CXXFLAGS="-DEDM_ML_DEBUG"
     debugModules = cms.untracked.vstring(
       'PixelVerticesSelector',
       'TracksClosestToFirstVerticesSelector',
       'JMETriggerNTuple',
     ),
     categories = cms.untracked.vstring(
       'FwkReport',
     ),
     cerr = cms.untracked.PSet(
       threshold = cms.untracked.string('WARNING'),
       FwkReport = cms.untracked.PSet(
         reportEvery = cms.untracked.int32(1),
       ),
     ),
     logError = cms.untracked.PSet(
       threshold = cms.untracked.string('ERROR'),
       extension = cms.untracked.string('.txt'),
       FwkReport = cms.untracked.PSet(
         reportEvery = cms.untracked.int32(1),
       ),
     ),
     logInfo = cms.untracked.PSet(
       threshold = cms.untracked.string('INFO'),
       extension = cms.untracked.string('.txt'),
       FwkReport = cms.untracked.PSet(
         reportEvery = cms.untracked.int32(1),
       ),
     ),
     logDebug = cms.untracked.PSet(
       threshold = cms.untracked.string('DEBUG'),
       extension = cms.untracked.string('.txt'),
       FwkReport = cms.untracked.PSet(
         reportEvery = cms.untracked.int32(1),
       ),
     ),
   )

# input EDM files [primary]
if opts.inputFiles:
   process.source.fileNames = opts.inputFiles
else:
   process.source.fileNames = [
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/20000/2FA69DD4-0651-084E-87B6-E5F38B007D5D.root",
     # ttbar NoPu
     "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/40000/FF494CD0-A72D-494F-8C89-8C6422D24504.root",
     "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/40000/FF1F2446-2FDB-5E4A-8CBE-A5E62A4518C2.root",
     "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/40000/FD048324-6F32-D944-B680-3633DBD45186.root",
     "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/40000/FC872EC1-9102-8545-A726-DDA51C276E6C.root",
     "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/40000/FBBEC820-DA08-AA44-8BC6-0469ED6C0D74.root",
     "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/40000/FA97BECF-51BE-7146-9946-B0560434E42B.root",
     "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/40000/F9F5095B-DC0A-6F48-8148-E221616F0C9E.root",

     # ttbarPU200
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240001/BCAB284F-B065-F343-9E48-478FDFBA70A0.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/FFE0A906-20D1-764B-BA0E-CB0E4CC062D3.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/FFCD7B10-9213-D746-B800-FD3F4A963297.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/FF55BD2C-752F-424E-BD6A-238F8CF2B0A1.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/FFB39BB4-5A91-2E46-B53A-415EE63A6DB8.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/FF3DA176-02DA-224A-84AD-9FE986A028E4.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/FF27A61A-E4BF-414A-8A82-AEDABD724723.root",

   ]




#===========
# Begin BTagAna

###############################
####### Parameters ############
###############################

groups = ["HLTEventInfo","HLTJetInfo","HLTTagVar","HLTJetTrack","HLTJetSV","HLTCSVTagVar"]
if opts.L1:
    groups.append("L1ObjectInfo")


from RecoBTag.PerformanceMeasurements.BTagAnalyzer_cff import *
btagana_tmp = bTagAnalyzer.clone()
print('Storing the variables from the following groups:')
options_to_change = set() #store which swtiches we need on
# for requiredGroup in options.groups:
for requiredGroup in groups:
  print(requiredGroup)
  found=False
  for existingGroup in btagana_tmp.groups:
    if(requiredGroup==existingGroup.group):
      existingGroup.store=True
      for var in existingGroup.variables:
        if "CaloJet." in var:
          var = var.split(".")[1]
        if "PFJet." in var:
          var = var.split(".")[1]
        if "PuppiJet." in var:
          var = var.split(".")[1]
        options_to_change.update([i for i in variableDict[var].runOptions])
      found=True
      break
  if(not found):
    print('WARNING: The group ' + requiredGroup + ' was not found')



# update process.GlobalTag.globaltag
if opts.gt is not None:
   process.GlobalTag.globaltag = opts.gt
print "Running with globalTag: %s"%(process.GlobalTag.globaltag)

# fix for AK4PF Phase-2 JECs
process.GlobalTag.toGet.append(cms.PSet(
  record = cms.string('JetCorrectionsRecord'),
  tag = cms.string('JetCorrectorParametersCollection_PhaseIIFall17_V5b_MC_AK4PF'),
  label = cms.untracked.string('AK4PF'),
))

#~ outFilename = 'JetTree_mc.root'
outFilename = opts.outName


## Output file
process.TFileService = cms.Service("TFileService",
   fileName = cms.string(outFilename)
)



#-------------------------------------
from RecoBTag.PerformanceMeasurements.BTagHLTAnalyzer_cff import *
process.btagana = bTagHLTAnalyzer.clone()

#------------------
#Handle groups
for requiredGroup in process.btagana.groups:
   for storedGroup in btagana_tmp.groups:
     if (requiredGroup.group == storedGroup.group):
       requiredGroup.store = storedGroup.store

process.btagana.MaxEta                = 4.5
process.btagana.MinPt                 = 25
# process.btagana.triggerTable          = cms.InputTag('TriggerResults::RECO2') # Data and MC
process.btagana.triggerTable          = cms.InputTag('TriggerResults') # Data and MC
# process.btagana.primaryVertexColl     = cms.InputTag('hltVerticesPF')
process.btagana.primaryVertexColl     = cms.InputTag('offlinePrimaryVertices') #change with new Offline like sequence

process.btagana.runHLTJetVariables     = cms.bool(True)
process.btagana.runOnData = False

# if opts.FastPV:
    # process.btagana.PFJets               = cms.InputTag('hltAK4PFCHSJetsCorrected')
    # process.btagana.PFJetTags            = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsInfosFastPV')
    # process.btagana.PFSVs                = cms.InputTag('hltDeepSecondaryVertexTagInfosPFFastPV')
    # process.btagana.PFJetDeepCSVTags     = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsPFFastPV:probb')
    # process.btagana.PFJetBPBJetTags      = cms.InputTag('hltPfJetBProbabilityBJetTagsFastPV')
    # process.btagana.PFJetPBJetTags       = cms.InputTag('hltPfJetProbabilityBJetTagsFastPV')
    #
    # process.btagana.PuppiJets            = cms.InputTag('hltAK4PuppiJetsCorrected')
    # process.btagana.PuppiJetTags         = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsInfosPuppiFastPV')
    # process.btagana.PuppiSVs             = cms.InputTag('hltDeepSecondaryVertexTagInfosPFPuppiFastPV')
    # process.btagana.PuppiJetDeepCSVTags  = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsPFPuppiFastPV:probb')
    # process.btagana.PuppiJetBPBJetTags   = cms.InputTag('hltPfJetBProbabilityBJetTagsPuppiFastPV')
    # process.btagana.PuppiJetPBJetTags    = cms.InputTag('hltPfJetProbabilityBJetTagsPuppiFastPV')
    # process.btagana.PuppiJetCSVTags      = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsPFPuppiFastPV')
# else:
process.btagana.PFJets               = cms.InputTag('hltAK4PFCHSJetsCorrected')
process.btagana.PFJetTags            = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsInfos')
process.btagana.PFSVs                = cms.InputTag('hltDeepSecondaryVertexTagInfosPF')
process.btagana.PFJetDeepCSVTags     = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsPF:probb')
process.btagana.PFJetBPBJetTags      = cms.InputTag('hltPfJetBProbabilityBJetTags')
process.btagana.PFJetPBJetTags       = cms.InputTag('hltPfJetProbabilityBJetTags')

process.btagana.PuppiJets            = cms.InputTag('hltAK4PuppiJetsCorrected')
process.btagana.PuppiJetTags         = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsInfosPuppi')
process.btagana.PuppiSVs             = cms.InputTag('hltDeepSecondaryVertexTagInfosPFPuppi')
process.btagana.PuppiJetDeepCSVTags  = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsPFPuppi:probb')
process.btagana.PuppiJetBPBJetTags   = cms.InputTag('hltPfJetBProbabilityBJetTagsPuppi')
process.btagana.PuppiJetPBJetTags    = cms.InputTag('hltPfJetProbabilityBJetTagsPuppi')
process.btagana.PuppiJetCSVTags      = cms.InputTag('hltCombinedSecondaryVertexBJetTagsPFPuppi')

process.btagana.analyzeL1Objects     =  cms.bool(opts.L1)
process.btagana.L1VertexColl         =  cms.InputTag('L1TkPrimaryVertex')
process.btagana.L1BarrelTrackColl    =  cms.InputTag('pfTracksFromL1TracksBarrel')
process.btagana.L1HGcalTrackColl     =  cms.InputTag('pfTracksFromL1TracksHGCal')
process.btagana.L1PFJets             =  cms.InputTag('ak4PFL1PFCorrected')
process.btagana.L1PuppiJets          =  cms.InputTag('ak4PFL1PuppiCorrected')

#---------------------------------------
## Event counter
from RecoBTag.PerformanceMeasurements.eventcounter_cfi import eventCounter
process.allEvents = eventCounter.clone()
process.selectedEvents = eventCounter.clone()
#---------------------------------------

# update JESC via local SQLite file
# from CondCore.CondDB.CondDB_cfi import CondDB
# CondDBJECFile = CondDB.clone(connect = 'sqlite_fip:RecoBTag/PerformanceMeasurements/data/PhaseIIFall17_V5b_MC.db' )
# process.jec = cms.ESSource('PoolDBESSource', CondDBJECFile, toGet = cms.VPSet())
# for _tmp in [
#   'AK4PF',
# #      'AK4PFchs',
# #      'AK4PFPuppi',
# #      'AK8PF',
# #      'AK8PFchs',
# #      'AK8PFPuppi',
# ]:
#   process.jec.toGet.append(
#     cms.PSet(
#       record = cms.string('JetCorrectionsRecord'),
#       tag = cms.string('JetCorrectorParametersCollection_PhaseIIFall17_V5b_MC_'+_tmp),
#       label = cms.untracked.string(_tmp),
#     )
#   )

# Add an ESPrefer to override JEC that might be available from the global tag
# process.es_prefer_jec = cms.ESPrefer('PoolDBESSource', 'jec')

# Tracking Monitoring
if opts.trkdqm:

   if opt_reco in ['HLT_TRKv00', 'HLT_TRKv00_TICL', 'HLT_TRKv02', 'HLT_TRKv02_TICL']:
      process.reconstruction_pixelTrackingOnly_step = cms.Path(process.reconstruction_pixelTrackingOnly)
      process.schedule.extend([process.reconstruction_pixelTrackingOnly_step])

   from JMETriggerAnalysis.Common.TrackHistogrammer_cfi import TrackHistogrammer
   process.TrackHistograms_hltPixelTracks = TrackHistogrammer.clone(src = 'pixelTracks')
   process.TrackHistograms_hltGeneralTracks = TrackHistogrammer.clone(src = 'generalTracks')

   process.trkMonitoringSeq = cms.Sequence(
       process.TrackHistograms_hltPixelTracks
     + process.TrackHistograms_hltGeneralTracks
   )

   if opt_skimTracks:
      process.TrackHistograms_hltGeneralTracksOriginal = TrackHistogrammer.clone(src = 'generalTracksOriginal')
      process.trkMonitoringSeq += process.TrackHistograms_hltGeneralTracksOriginal

   if opts.L1:
       from JMETriggerAnalysis.Common.L1TrackHistogrammer_cfi import L1TrackHistogrammer
       from JMETriggerAnalysis.Common.L1VertexHistogrammer_cfi import L1VertexHistogrammer
       from JMETriggerAnalysis.Common.L1JetHistogrammer_cfi import L1JetHistogrammer
       from JMETriggerAnalysis.Common.JetHistogrammer_cfi import JetHistogrammer
       process.TrackHistograms_L1BarrelTracks = L1TrackHistogrammer.clone(src = 'pfTracksFromL1TracksBarrel')
       process.TrackHistograms_L1HGCalTracks = L1TrackHistogrammer.clone(src = 'pfTracksFromL1TracksHGCal')
       process.trkMonitoringSeq += process.TrackHistograms_L1BarrelTracks
       process.trkMonitoringSeq += process.TrackHistograms_L1HGCalTracks
       process.VertexHistograms_L1PrimaryVertices = L1VertexHistogrammer.clone(src = 'L1TkPrimaryVertex')
       process.trkMonitoringSeq += process.VertexHistograms_L1PrimaryVertices
       process.JetHistograms_L1PFCHSCorrected = L1JetHistogrammer.clone(src = 'ak4PFL1PFCorrected')
       process.JetHistograms_L1PFPUPPICorrected = L1JetHistogrammer.clone(src = 'ak4PFL1PuppiCorrected')
       process.JetHistograms_L1PFCHS = JetHistogrammer.clone(src = 'ak4PFL1PF')
       process.JetHistograms_L1PFPUPPI = JetHistogrammer.clone(src = 'ak4PFL1Puppi')
       process.trkMonitoringSeq += process.JetHistograms_L1PFCHSCorrected
       process.trkMonitoringSeq += process.JetHistograms_L1PFPUPPICorrected
       process.trkMonitoringSeq += process.JetHistograms_L1PFCHS
       process.trkMonitoringSeq += process.JetHistograms_L1PFPUPPI

   from JMETriggerAnalysis.Common.VertexHistogrammer_cfi import VertexHistogrammer
   process.VertexHistograms_hltPixelVertices = VertexHistogrammer.clone(src = 'pixelVertices')
   process.VertexHistograms_hltPrimaryVertices = VertexHistogrammer.clone(src = 'offlinePrimaryVertices')

   process.trkMonitoringSeq += cms.Sequence(
       process.VertexHistograms_hltPixelVertices
     + process.VertexHistograms_hltPrimaryVertices
   )

#   from Validation.RecoVertex.PrimaryVertexAnalyzer4PUSlimmed_cfi import vertexAnalysis, pixelVertexAnalysisPixelTrackingOnly
#   process.vertexAnalysis = vertexAnalysis.clone(vertexRecoCollections = ['offlinePrimaryVertices'])
#   process.pixelVertexAnalysis = pixelVertexAnalysisPixelTrackingOnly.clone(vertexRecoCollections = ['pixelVertices'])
#
#   process.trkMonitoringSeq += cms.Sequence(
#       process.vertexAnalysis
#     + process.pixelVertexAnalysis
#   )

   process.trkMonitoringEndPath = cms.EndPath(process.trkMonitoringSeq)
   process.schedule.extend([process.trkMonitoringEndPath])


if opts.pfdqm:

   from JMETriggerAnalysis.Common.pfCandidateHistogrammerRecoPFCandidate_cfi import pfCandidateHistogrammerRecoPFCandidate
   from JMETriggerAnalysis.Common.pfCandidateHistogrammerPatPackedCandidate_cfi import pfCandidateHistogrammerPatPackedCandidate

   _candTags = [
     ('_simPFCands', 'simPFProducer', '', pfCandidateHistogrammerRecoPFCandidate),
     ('_hltPFCands', 'particleFlowTmp', '', pfCandidateHistogrammerRecoPFCandidate),
     ('_hltPuppiCands', 'hltPuppi', '(pt > 0)', pfCandidateHistogrammerRecoPFCandidate),
     #~ ('_offlinePFCands', 'packedPFCandidates', '', pfCandidateHistogrammerPatPackedCandidate),
   ]

   _regTags = [
     ['', ''],
     ['_HB'   , '(0.0<=abs(eta) && abs(eta)<1.5)'],
     ['_HGCal', '(1.5<=abs(eta) && abs(eta)<3.0)'],
     ['_HF'   , '(3.0<=abs(eta) && abs(eta)<5.0)'],
   ]

   _pidTags = [
     ['', ''],
     ['_chargedHadrons', '(abs(pdgId) == 211)'],
     ['_neutralHadrons', '(abs(pdgId) == 130)'],
     ['_photons'       , '(abs(pdgId) ==  22)'],
   ]

   process.pfMonitoringSeq = cms.Sequence()
   for _candTag in _candTags:
     for _regTag in _regTags:
       for _pidTag in _pidTags:
         _modName = 'PFCandidateHistograms'+_candTag[0]+_regTag[0]+_pidTag[0]
         setattr(process, _modName, _candTag[3].clone(
           src = _candTag[1],
           cut = ' && '.join([_tmp for _tmp in [_candTag[2], _regTag[1], _pidTag[1]] if _tmp]),
         ))
         process.pfMonitoringSeq += getattr(process, _modName)

   process.pfMonitoringEndPath = cms.EndPath(process.pfMonitoringSeq)
   process.schedule.extend([process.pfMonitoringEndPath])


process.p = cms.Path(
    process.allEvents
    * process.selectedEvents
)
process.schedule.extend([process.p])
process.analysisNTupleEndPath = cms.EndPath(process.btagana)
process.schedule.extend([process.analysisNTupleEndPath])

# dump content of cms.Process to python file
if opts.dumpPython is not None:
   open(opts.dumpPython, 'w').write(process.dumpPython())

# print-outs
print '--- runHLTBTagAnalyzer_PhaseII_cfg.py ---\n'
print 'process.maxEvents.input =', process.maxEvents.input
print 'process.source.skipEvents =', process.source.skipEvents
print 'process.source.fileNames =', process.source.fileNames
print 'process.source.secondaryFileNames =', process.source.secondaryFileNames
print 'numThreads =', opts.numThreads
print 'numStreams =', opts.numStreams
print 'logs =', opts.logs
print 'wantSummary =', opts.wantSummary
print 'process.GlobalTag.globaltag =', process.GlobalTag.globaltag
print 'dumpPython =', opts.dumpPython
print 'doTrackHistos =', opts.trkdqm
print 'rerunL1 =', opts.L1
print 'doParticleFlowHistos =', opts.pfdqm
print 'option: reco =', opt_reco, '(skimTracks = '+str(opt_skimTracks)+')'
print 'option: BTVreco =', opt_BTVreco
print '\n-------------------------------'
