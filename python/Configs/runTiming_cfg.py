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

opts.register('numThreads', 4,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of threads')

opts.register('numStreams', 0,
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

opts.register('reco', 'HLT_TRKv06_TICL',
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


opts.register('BTVreco', 'cutsV1',
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'which reco to load for BTV sequence, default = default')


opts.parseArguments()

# flag: skim original collection of generalTracks (only tracks associated to first N pixel vertices)
opt_skimTracks = False

opt_reco = opts.reco
if opt_reco.endswith('_skimmedTracks'):
   opt_reco = opt_reco[:-len('_skimmedTracks')]
   opt_skimTracks = True

if   opt_reco == 'HLT_TRKv00':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv00_cfg      import cms, process
elif opt_reco == 'HLT_TRKv00_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv00_TICL_cfg import cms, process
elif opt_reco == 'HLT_TRKv02':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv02_cfg      import cms, process
elif opt_reco == 'HLT_TRKv02_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv02_TICL_cfg import cms, process
elif opt_reco == 'HLT_TRKv06':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv06_cfg      import cms, process
elif opt_reco == 'HLT_TRKv06_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv06_TICL_cfg import cms, process
else:
   raise RuntimeError('invalid argument for option "reco": "'+opt_reco+'"')

opt_BTVreco = opts.BTVreco
if opt_BTVreco == 'default':
      from RecoBTag.PerformanceMeasurements.Configs.hltPhase2_BTV import customize_hltPhase2_BTV
      process = customize_hltPhase2_BTV(process)
elif opt_BTVreco == 'cutsV1':
      from RecoBTag.PerformanceMeasurements.Configs.hltPhase2_BTV_cuts import customize_hltPhase2_BTV
      process = customize_hltPhase2_BTV(process)
elif opt_BTVreco == 'cutsV2':
      from RecoBTag.PerformanceMeasurements.Configs.hltPhase2_BTV_cutsV2 import customize_hltPhase2_BTV
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

# process.noFilter_PFDeepCSV = cms.Path(process.HLTBtagDeepCSVSequencePF)
# process.noFilter_PFProba = cms.Path(process.HLTBtagProbabiltySequencePF)
# process.noFilter_PFBProba = cms.Path(process.HLTBtagBProbabiltySequencePF)
process.noFilter_PFDeepCSVPuppi = cms.Path(process.HLTBtagDeepCSVSequencePFPuppi)
# process.noFilter_PFDeepFlavourPuppi = cms.Path(process.HLTBtagDeepFlavourSequencePFPuppi)
# process.noFilter_PFProbaPuppi = cms.Path(process.HLTBtagProbabiltySequencePFPuppi)
# process.noFilter_PFBProbaPuppi = cms.Path(process.HLTBtagBProbabiltySequencePFPuppi)

# process.schedule.extend([process.noFilter_PFDeepCSV, process.noFilter_PFProba, process.noFilter_PFBProba])
# process.schedule.extend([process.noFilter_PFDeepCSVPuppi, process.noFilter_PFProbaPuppi, process.noFilter_PFBProbaPuppi, process.noFilter_PFDeepFlavourPuppi])
process.schedule.extend([process.noFilter_PFDeepCSVPuppi])


# max number of events to be processed
process.maxEvents.input = opts.maxEvents

# number of events to be skipped
process.source.skipEvents = cms.untracked.uint32(opts.skipEvents)

# multi-threading settings
process.options.numberOfThreads = cms.untracked.uint32(opts.numThreads if (opts.numThreads > 1) else 1)
process.options.numberOfStreams = cms.untracked.uint32(opts.numStreams if (opts.numStreams > 1) else 1)
process.options.sizeOfStackForThreadsInKB = cms.untracked.uint32(10240)

# show cmsRun summary at job completion
# process.options.wantSummary = cms.untracked.bool(opts.wantSummary)
process.options.wantSummary = cms.untracked.bool(True)

# MessageLogger
if opts.logs:
   process.MessageLogger = cms.Service('MessageLogger',
     destinations = cms.untracked.vstring(
       'cerr',
       'logError',
       'logInfo',
       'logDebug',
     ),
     debugModules = cms.untracked.vstring(
       'PixelVerticesSelector',
       'TracksClosestToFirstVerticesSelector',
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
     # ttbar NoPu
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/40000/FF494CD0-A72D-494F-8C89-8C6422D24504.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/40000/FF1F2446-2FDB-5E4A-8CBE-A5E62A4518C2.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/40000/FD048324-6F32-D944-B680-3633DBD45186.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/40000/FC872EC1-9102-8545-A726-DDA51C276E6C.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/40000/FBBEC820-DA08-AA44-8BC6-0469ED6C0D74.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/40000/FA97BECF-51BE-7146-9946-B0560434E42B.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/40000/F9F5095B-DC0A-6F48-8148-E221616F0C9E.root",

     # ttbarPU200
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240001/BCAB284F-B065-F343-9E48-478FDFBA70A0.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/110000/005E74D6-B50E-674E-89E6-EAA9A617B476.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/110000/007F7BCB-2251-FE48-A5D4-68DE9E4F1271.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/110000/00B081CE-A285-1242-8CB5-F28F10285592.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/110000/00BF98ED-FE5E-6341-A1F3-7AA1EF8C3BEB.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/110000/00C33DFD-2283-2A42-9A6E-AC76311FFCC5.root",
     # "/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/110000/0159AC9E-5057-2147-A47A-E43D88B04AC0.root",
     # "file:/eos/home-s/sewuchte/TimingFilesPhase2/PU200/BCAB284F-B065-F343-9E48-478FDFBA70A0.root",
     # "file:/eos/home-s/sewuchte/TimingFilesPhase2/PU200/005E74D6-B50E-674E-89E6-EAA9A617B476.root",
     # "file:/eos/home-s/sewuchte/TimingFilesPhase2/PU200/007F7BCB-2251-FE48-A5D4-68DE9E4F1271.root",
     # "file:/eos/home-s/sewuchte/TimingFilesPhase2/PU200/00B081CE-A285-1242-8CB5-F28F10285592.root",
     # "file:/eos/home-s/sewuchte/TimingFilesPhase2/PU200/00BF98ED-FE5E-6341-A1F3-7AA1EF8C3BEB.root",
     # "file:/eos/home-s/sewuchte/TimingFilesPhase2/PU200/00C33DFD-2283-2A42-9A6E-AC76311FFCC5.root",
     # "file:/eos/home-s/sewuchte/TimingFilesPhase2/PU200/0159AC9E-5057-2147-A47A-E43D88B04AC0.root",

     "/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/227B9AFA-2612-694B-A2E7-B566F92C4B55.root",
   ]


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



# del process.pfDeepBoostedJetTask
# del process.inclusiveCandidateVertexingCvsLTask
# del process.inclusiveCandidateVertexingTask
# del process.inclusiveCandidateVertexing
# del process.inclusiveCandidateVertexingCvsL
#
#
# del process.inclusiveVertexFinder
# del process.inclusiveVertexFinderDefault
# del process.vertexMerger
#
#
# del process.inclusiveVertexingTask
#
# del process.globalrecoTask
# process.globalrecoTask = cms.Task(process.MeasurementTrackerEventPreSplitting, process.caloJetsForTrkTask, process.caloTowersRecTask, process.ecalClustersTask, process.egammaGlobalRecoTask, process.fastTimingGlobalRecoTask, process.generalV0Candidates, process.hcalGlobalRecoTask, process.iterTICLTask, process.jetGlobalRecoTask, process.muonGlobalRecoTask, process.muoncosmicrecoTask, process.offlineBeamSpot, process.offlinePrimaryVertices, process.offlinePrimaryVertices4D, process.offlinePrimaryVertices4DWithBS, process.offlinePrimaryVertices4DnoPID, process.offlinePrimaryVertices4DnoPIDWithBS, process.offlinePrimaryVerticesWithBS, process.particleFlowClusterTask, process.pfTrackingGlobalRecoTask, process.quickTrackAssociatorByHits, process.siPixelClusterShapeCachePreSplitting, process.standalonemuontrackingTask, process.tofPID, process.tofPID4DnoPID, process.tpClusterProducer, process.trackRefsForJetsBeforeSorting, process.trackRefsForJetsBeforeSorting4D, process.trackRefsForJetsBeforeSorting4DnoPID, process.trackTimeValueMapProducer, process.trackWithVertexRefSelectorBeforeSorting, process.trackWithVertexRefSelectorBeforeSorting4D, process.trackWithVertexRefSelectorBeforeSorting4DnoPID, process.trackingGlobalRecoTask, process.unsortedOfflinePrimaryVertices, process.unsortedOfflinePrimaryVertices4D, process.unsortedOfflinePrimaryVertices4DnoPID)
#
# del process.reconstruction_withPixellessTkTask
#
# process.reconstruction_withPixellessTkTask = cms.Task(process.ConvStepTask, process.DetachedQuadStepTask, process.InitialStepPreSplittingTask, process.LowPtQuadStepTask, process.LowPtTripletStepTask, process.MeasurementTrackerEventPreSplitting, process.PFTauTask, process.PixelPairStepTask, process.ak4CaloJetsForTrk, process.btaggingTask, process.caloTowerForTrk, process.caloTowersRecTask, process.conversionOpenTrackTask, process.conversionStepTracks, process.cosmicDCTracksSeqTask, process.ctfTracksPixelLessTask, process.doAlldEdXEstimatorsTask, process.duplicateTrackCandidates, process.duplicateTrackClassifier, process.earlyGeneralTracks, process.ecalClustersTask, process.egammaGlobalRecoTask, process.egammaHighLevelRecoPostPFTask, process.egammaHighLevelRecoPrePFTask, process.electronSeedsSeqTask, process.fastTimingGlobalRecoTask, process.firstStepPrimaryVertices, process.firstStepPrimaryVerticesUnsorted, process.fixedGridRhoFastjetAllTmp, process.generalTracks, process.generalV0Candidates, process.gsfTracksOpenConversions, process.hcalGlobalRecoTask, process.hgcalTrackCollection, process.highPtTripletStepClusters, process.highPtTripletStepHitDoublets, process.highPtTripletStepHitTriplets, process.highPtTripletStepSeedLayers, process.highPtTripletStepSeeds, process.highPtTripletStepSelector, process.highPtTripletStepTrackCandidates, process.highPtTripletStepTrackingRegions, process.highPtTripletStepTracks,  process.initialStepHitDoublets, process.initialStepHitQuadruplets, process.initialStepSeedLayers, process.initialStepSeeds, process.initialStepSelector, process.initialStepTrackCandidates, process.initialStepTrackRefsForJets, process.initialStepTrackingRegions, process.initialStepTracks, process.iterTICLTask, process.jetGlobalRecoTask, process.jetHighLevelRecoTask, process.localrecoTask, process.logErrorHarvester, process.lowPtGsfElectronTask, process.mergedDuplicateTracks, process.metrecoPlusHCALNoiseTask, process.muonGlobalRecoTask, process.muonSeededStepTask, process.muoncosmichighlevelrecoTask, process.muoncosmicrecoTask, process.muonshighlevelrecoTask, process.offlineBeamSpot, process.offlinePrimaryVertices, process.offlinePrimaryVertices4D, process.offlinePrimaryVertices4DWithBS, process.offlinePrimaryVertices4DnoPID, process.offlinePrimaryVertices4DnoPIDWithBS, process.offlinePrimaryVerticesWithBS, process.particleFlowBlock, process.particleFlowClusterTask, process.particleFlowEGammaFinalTask, process.particleFlowEGammaFullTask, process.particleFlowLinksTask, process.particleFlowTmp, process.particleFlowTmpBarrel, process.particleFlowTmpPtrs, process.particleFlowTrackWithDisplacedVertexTask, process.pfGsfElectronMVASelectionTask, process.pfParticleSelectionTask, process.pfTrack, process.pfTrackingGlobalRecoTask, process.preDuplicateMergingGeneralTracks, process.quickTrackAssociatorByHits, process.recoPFMETTask, process.reducedRecHitsTask, process.siPixelClusterShapeCachePreSplitting, process.simPFProducer, process.standalonemuontrackingTask, process.tofPID, process.tofPID4DnoPID, process.tpClusterProducer, process.trackExtrapolator, process.trackRefsForJetsBeforeSorting, process.trackRefsForJetsBeforeSorting4D, process.trackRefsForJetsBeforeSorting4DnoPID, process.trackTimeValueMapProducer, process.trackWithVertexRefSelectorBeforeSorting, process.trackWithVertexRefSelectorBeforeSorting4D, process.trackWithVertexRefSelectorBeforeSorting4DnoPID, process.trackerClusterCheck, process.unsortedOfflinePrimaryVertices, process.unsortedOfflinePrimaryVertices4D, process.unsortedOfflinePrimaryVertices4DnoPID)
#
# process.reconstructionTask = cms.Task(process.ConvStepTask, process.DetachedQuadStepTask, process.InitialStepPreSplittingTask, process.LowPtQuadStepTask, process.LowPtTripletStepTask, process.MeasurementTrackerEventPreSplitting, process.PFTauTask, process.PixelPairStepTask, process.ak4CaloJetsForTrk, process.btaggingTask, process.caloTowerForTrk, process.caloTowersRecTask, process.conversionOpenTrackTask, process.conversionStepTracks, process.cosmicDCTracksSeqTask, process.doAlldEdXEstimatorsTask, process.duplicateTrackCandidates, process.duplicateTrackClassifier, process.earlyGeneralTracks, process.ecalClustersTask, process.egammaGlobalRecoTask, process.egammaHighLevelRecoPostPFTask, process.egammaHighLevelRecoPrePFTask, process.electronSeedsSeqTask, process.fastTimingGlobalRecoTask, process.firstStepPrimaryVertices, process.firstStepPrimaryVerticesUnsorted, process.fixedGridRhoFastjetAllTmp, process.generalTracks, process.generalV0Candidates, process.gsfTracksOpenConversions, process.hcalGlobalRecoTask, process.hgcalTrackCollection, process.highPtTripletStepClusters, process.highPtTripletStepHitDoublets, process.highPtTripletStepHitTriplets, process.highPtTripletStepSeedLayers, process.highPtTripletStepSeeds, process.highPtTripletStepSelector, process.highPtTripletStepTrackCandidates, process.highPtTripletStepTrackingRegions, process.highPtTripletStepTracks, process.initialStepHitDoublets, process.initialStepHitQuadruplets, process.initialStepSeedLayers, process.initialStepSeeds, process.initialStepSelector, process.initialStepTrackCandidates, process.initialStepTrackRefsForJets, process.initialStepTrackingRegions, process.initialStepTracks, process.iterTICLTask, process.jetGlobalRecoTask, process.jetHighLevelRecoTask, process.localrecoTask, process.logErrorHarvester, process.lowPtGsfElectronTask, process.mergedDuplicateTracks, process.metrecoPlusHCALNoiseTask, process.muonGlobalRecoTask, process.muonSeededStepTask, process.muoncosmichighlevelrecoTask, process.muoncosmicrecoTask, process.muonshighlevelrecoTask, process.offlineBeamSpot, process.offlinePrimaryVertices, process.offlinePrimaryVertices4D, process.offlinePrimaryVertices4DWithBS, process.offlinePrimaryVertices4DnoPID, process.offlinePrimaryVertices4DnoPIDWithBS, process.offlinePrimaryVerticesWithBS, process.particleFlowBlock, process.particleFlowClusterTask, process.particleFlowEGammaFinalTask, process.particleFlowEGammaFullTask, process.particleFlowLinksTask, process.particleFlowTmp, process.particleFlowTmpBarrel, process.particleFlowTmpPtrs, process.particleFlowTrackWithDisplacedVertexTask, process.pfGsfElectronMVASelectionTask, process.pfParticleSelectionTask, process.pfTrack, process.pfTrackingGlobalRecoTask, process.preDuplicateMergingGeneralTracks, process.quickTrackAssociatorByHits, process.recoPFMETTask, process.reducedRecHitsTask, process.siPixelClusterShapeCachePreSplitting, process.simPFProducer, process.standalonemuontrackingTask, process.tofPID, process.tofPID4DnoPID, process.tpClusterProducer, process.trackExtrapolator, process.trackRefsForJetsBeforeSorting, process.trackRefsForJetsBeforeSorting4D, process.trackRefsForJetsBeforeSorting4DnoPID, process.trackTimeValueMapProducer,  process.trackWithVertexRefSelectorBeforeSorting, process.trackWithVertexRefSelectorBeforeSorting4D, process.trackWithVertexRefSelectorBeforeSorting4DnoPID, process.trackerClusterCheck, process.unsortedOfflinePrimaryVertices, process.unsortedOfflinePrimaryVertices4D, process.unsortedOfflinePrimaryVertices4DnoPID)
#
# process.reconstruction_trackingOnlyTask = cms.Task(process.ConvStepTask, process.InitialStepPreSplittingTask, process.MeasurementTrackerEventPreSplitting, process.caloJetsForTrkTask, process.conversionStepTracks, process.doAlldEdXEstimatorsTask, process.duplicateTrackCandidates, process.duplicateTrackClassifier, process.earlyGeneralTracks, process.electronSeedsSeqTask, process.fastTimingGlobalRecoTask, process.generalTracks, process.generalV0Candidates, process.hcalGlobalRecoTask, process.iterTrackingEarlyTask, process.localrecoTask, process.mergedDuplicateTracks, process.muonSeededStepTask, process.offlineBeamSpot, process.offlinePrimaryVertices, process.offlinePrimaryVertices4D, process.offlinePrimaryVertices4DWithBS, process.offlinePrimaryVertices4DnoPID, process.offlinePrimaryVertices4DnoPIDWithBS, process.offlinePrimaryVerticesWithBS, process.preDuplicateMergingGeneralTracks, process.quickTrackAssociatorByHits, process.siPixelClusterShapeCachePreSplitting, process.standalonemuontrackingTask, process.tofPID, process.tofPID4DnoPID, process.tpClusterProducer, process.trackExtrapolator, process.trackRefsForJetsBeforeSorting, process.trackRefsForJetsBeforeSorting4D, process.trackRefsForJetsBeforeSorting4DnoPID, process.trackTimeValueMapProducer,  process.trackWithVertexRefSelectorBeforeSorting, process.trackWithVertexRefSelectorBeforeSorting4D, process.trackWithVertexRefSelectorBeforeSorting4DnoPID, process.trackerClusterCheck, process.unsortedOfflinePrimaryVertices, process.unsortedOfflinePrimaryVertices4D, process.unsortedOfflinePrimaryVertices4DnoPID)
#
#
# process.reconstruction_HcalNZSTask = cms.Task(process.MeasurementTrackerEventPreSplitting, process.caloJetsForTrkTask, process.caloTowersRecTask, process.ecalClustersTask, process.egammaGlobalRecoTask, process.fastTimingGlobalRecoTask, process.generalV0Candidates, process.hcalGlobalRecoTask, process.highlevelrecoTask,  process.iterTICLTask, process.jetGlobalRecoTask, process.localreco_HcalNZSTask, process.logErrorHarvester, process.muonGlobalRecoTask, process.muoncosmicrecoTask, process.offlineBeamSpot, process.offlinePrimaryVertices, process.offlinePrimaryVertices4D, process.offlinePrimaryVertices4DWithBS, process.offlinePrimaryVertices4DnoPID, process.offlinePrimaryVertices4DnoPIDWithBS, process.offlinePrimaryVerticesWithBS, process.particleFlowClusterTask, process.pfTrackingGlobalRecoTask, process.quickTrackAssociatorByHits, process.siPixelClusterShapeCachePreSplitting, process.standalonemuontrackingTask, process.tofPID, process.tofPID4DnoPID, process.tpClusterProducer, process.trackRefsForJetsBeforeSorting, process.trackRefsForJetsBeforeSorting4D, process.trackRefsForJetsBeforeSorting4DnoPID, process.trackTimeValueMapProducer, process.trackWithVertexRefSelectorBeforeSorting, process.trackWithVertexRefSelectorBeforeSorting4D, process.trackWithVertexRefSelectorBeforeSorting4DnoPID, process.trackingGlobalRecoTask, process.unsortedOfflinePrimaryVertices, process.unsortedOfflinePrimaryVertices4D, process.unsortedOfflinePrimaryVertices4DnoPID)

# del process.vertexReco
# process.vertexReco = cms.Sequence(process.initialStepPVSequence+process.unsortedOfflinePrimaryVertices+process.trackWithVertexRefSelectorBeforeSorting+process.trackRefsForJetsBeforeSorting+process.offlinePrimaryVertices+process.offlinePrimaryVerticesWithBS)


# process.pfCTaggingTask = cms.Task(process.candidateVertexArbitratorCvsL, process.candidateVertexMergerCvsL, process.inclusiveCandidateSecondaryVerticesCvsL, process.inclusiveCandidateVertexFinderCvsL, process.pfCombinedCvsBJetTags, process.pfCombinedCvsLJetTags, process.pfInclusiveSecondaryVertexFinderCvsLTagInfos)
# del process.pfCTaggingTask

# process.pfBTaggingTask = cms.Task(process.candidateVertexArbitrator, process.candidateVertexMerger, process.inclusiveCandidateSecondaryVertices, process.inclusiveCandidateVertexFinder, process.pfChargeBJetTags, process.pfCombinedInclusiveSecondaryVertexV2BJetTags, process.pfCombinedMVAV2BJetTags, process.pfCombinedSecondaryVertexV2BJetTags, process.pfDeepCSVTask, process.pfGhostTrackBJetTags, process.pfGhostTrackVertexTagInfos, process.pfImpactParameterTagInfos, process.pfInclusiveSecondaryVertexFinderTagInfos, process.pfJetBProbabilityBJetTags, process.pfJetProbabilityBJetTags, process.pfSecondaryVertexTagInfos, process.pfSimpleInclusiveSecondaryVertexHighEffBJetTags, process.pfSimpleSecondaryVertexHighEffBJetTags, process.pfTrackCountingHighEffBJetTags, process.pixelClusterTagInfos, process.softPFElectronBJetTags, process.softPFElectronsTagInfos, process.softPFMuonBJetTags, process.softPFMuonsTagInfos)
# del process.pfBTaggingTask
# del process.pfBTagging
# del process.btaggingTask
# del process.pfCTagging
# del process.candidateVertexArbitrator
# del process.candidateVertexArbitratorCvsL
# del process.candidateVertexArbitratorDefault
# del process.candidateVertexMerger
# del process.candidateVertexMergerCvsL
# del process.inclusiveCandidateSecondaryVertices
# del process.inclusiveCandidateSecondaryVerticesCvsL
# del process.inclusiveSecondaryVertices
# del process.trackVertexArbitrator
# del process.trackVertexArbitratorDefault






# dump content of cms.Process to python file
if opts.dumpPython is not None:
   open(opts.dumpPython, 'w').write(process.dumpPython())


#timing test
from HLTrigger.Timer.FastTimer import customise_timer_service_print,customise_timer_service,customise_timer_service_singlejob
# process = customise_timer_service_print(process)
process = customise_timer_service(process)
# process = customise_timer_service_singlejob(process)
process.FastTimerService.dqmPathTimeRange    =  300.   # ms
process.FastTimerService.dqmModuleTimeRange  =   300.   # ms

# print-outs
print '--- runHLTBTagAnalyzer_PhaseII_cfg.py ---\n'
print 'process.maxEvents.input =', process.maxEvents.input
print 'process.source.skipEvents =', process.source.skipEvents
print 'process.source.fileNames =', process.source.fileNames
print 'numThreads =', opts.numThreads
print 'numStreams =', opts.numStreams
print 'logs =', opts.logs
print 'wantSummary =', opts.wantSummary
print 'process.GlobalTag.globaltag =', process.GlobalTag.globaltag
print 'dumpPython =', opts.dumpPython
print 'option: reco =', opt_reco, '(skimTracks = '+str(opt_skimTracks)+')'
print 'option: BTVreco =', opt_BTVreco
print '\n-------------------------------'

# nohup taskset -c 0-3 cmsRun ../RecoBTag/PerformanceMeasurements/python/Configs/runTiming_cfg.py >& full.log&
