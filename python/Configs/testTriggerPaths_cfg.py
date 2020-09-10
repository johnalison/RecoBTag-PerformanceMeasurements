###
### command-line arguments
###
import FWCore.ParameterSet.VarParsing as vpo
opts = vpo.VarParsing('analysis')

opts.register('reco', 'HLT_TRKv06_TICL',
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'keyword defining reconstruction methods for JME inputs')

opts.register('BTVreco', 'default',
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'which reco to load for BTV sequence, default = default')

opts.register('skipEvents', 0,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of events to be skipped')

opts.register('dumpPython', None,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'path to python file with content of cms.Process')

opts.register('numThreads', 1,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of threads')

opts.register('numStreams', 1,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of streams')

opts.register('wantSummary', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'show cmsRun summary at job completion')

opts.register('globalTag', None,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'argument of process.GlobalTag.globaltag')

opts.register('output', 'out.root',
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'path to output ROOT file')

opts.parseArguments()

###
### base configuration file
### (choice of reconstruction sequence)
###

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
   logmsg = '\n\n'+' '*2+'Valid arguments for option "reco" are'
   for recoArg in [
     'HLT_TRKv00',
     'HLT_TRKv00_skimmedTracks',
     'HLT_TRKv00_TICL',
     'HLT_TRKv00_TICL_skimmedTracks',
     'HLT_TRKv02',
     'HLT_TRKv02_skimmedTracks',
     'HLT_TRKv02_TICL',
     'HLT_TRKv02_TICL_skimmedTracks',
     'HLT_TRKv06',
     'HLT_TRKv06_skimmedTracks',
     'HLT_TRKv06_TICL',
     'HLT_TRKv06_TICL_skimmedTracks',
   ]:
     logmsg += '\n'+' '*4+recoArg
   raise RuntimeError('invalid argument for option "reco": "'+opt_reco+'"'+logmsg+'\n')




# skimming of tracks
if opt_skimTracks:
   from JMETriggerAnalysis.Common.hltPhase2_skimmedTracks import customize_hltPhase2_skimmedTracks
   process = customize_hltPhase2_skimmedTracks(process)


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


###
### trigger paths
###


process.hltPFCHSCentralJetQuad30 = cms.EDFilter( "HLT1PFJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 30.0 ),
    MinN = cms.int32( 4 ),
    MaxEta = cms.double( 2.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltAK4PFCHSJetsCorrected" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 86 ),
    MaxMass = cms.double( -1.0 )
)

process.hlt1PFCHSCentralJet75 = cms.EDFilter( "HLT1PFJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 75.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltAK4PFCHSJetsCorrected" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 0 ),
    MaxMass = cms.double( -1.0 )
)

process.hlt2PFCHSCentralJet60 = cms.EDFilter( "HLT1PFJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 60.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltAK4PFCHSJetsCorrected" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 0 ),
    MaxMass = cms.double( -1.0 )
)

process.hlt3PFCHSCentralJet45 = cms.EDFilter( "HLT1PFJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 45.0 ),
    MinN = cms.int32( 3 ),
    MaxEta = cms.double( 2.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltAK4PFCHSJetsCorrected" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 0 ),
    MaxMass = cms.double( -1.0 )
)

process.hlt4PFCHSCentralJet40 = cms.EDFilter( "HLT1PFJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 40.0 ),
    MinN = cms.int32( 4 ),
    MaxEta = cms.double( 2.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltAK4PFCHSJetsCorrected" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 0 ),
    MaxMass = cms.double( -1.0 )
)

process.hltPFCHSCentralJetQuad30forHt = cms.EDProducer( "HLTPFJetCollectionProducer",
    TriggerTypes = cms.vint32( 86 ),
    HLTObject = cms.InputTag( "hltPFCHSCentralJetQuad30" )
)

process.hltHtMhtPFCHSCentralJetsQuadC30 = cms.EDProducer( "HLTHtMhtProducer",
    usePt = cms.bool( True ),
    minPtJetHt = cms.double( 30.0 ),
    maxEtaJetMht = cms.double( 999.0 ),
    minNJetMht = cms.int32( 0 ),
    jetsLabel = cms.InputTag( "hltPFCHSCentralJetQuad30forHt" ),
    maxEtaJetHt = cms.double( 2.5 ),
    minPtJetMht = cms.double( 0.0 ),
    minNJetHt = cms.int32( 4 ),
    pfCandidatesLabel = cms.InputTag("particleFlowTmp"),
    excludePFMuons = cms.bool( False )
)

process.hltPFCHSCentralJetsQuad30HT330 = cms.EDFilter( "HLTHtMhtFilter",
    saveTags = cms.bool( True ),
    mhtLabels = cms.VInputTag( 'hltHtMhtPFCHSCentralJetsQuadC30' ),
    meffSlope = cms.vdouble( 1.0 ),
    minHt = cms.vdouble( 330.0 ),
    minMht = cms.vdouble( 0.0 ),
    htLabels = cms.VInputTag( 'hltHtMhtPFCHSCentralJetsQuadC30' ),
    minMeff = cms.vdouble( 0.0 )
)



# modify simple BtagSequence
process.hltDeepBLifetimeTagInfosPFMod = process.hltDeepBLifetimeTagInfosPF.clone(jets = "hltPFCHSJetForBtag")
# process.hltDeepBLifetimeTagInfosPFMod = process.hltDeepBLifetimeTagInfosPF.clone(jets = "hltAK4PFCHSJetsCorrected")
process.hltDeepSecondaryVertexTagInfosPFMod = process.hltDeepSecondaryVertexTagInfosPF.clone(trackIPTagInfos = "hltDeepBLifetimeTagInfosPFMod")
process.hltDeepCombinedSecondaryVertexBJetTagsInfosMod = process.hltDeepCombinedSecondaryVertexBJetTagsInfos.clone(svTagInfos = "hltDeepSecondaryVertexTagInfosPFMod")
process.hltDeepCombinedSecondaryVertexBJetTagsPFMod = process.hltDeepCombinedSecondaryVertexBJetTagsPF.clone(src = "hltDeepCombinedSecondaryVertexBJetTagsInfosMod")


process.HLTBtagDeepCSVSequencePFMod = cms.Sequence(
    process.hltPFCHSJetForBtagSelector
    +process.hltPFCHSJetForBtag
    +process.hltDeepBLifetimeTagInfosPFMod
    +process.hltDeepInclusiveVertexFinderPF
    +process.hltDeepInclusiveSecondaryVerticesPF
    +process.hltDeepTrackVertexArbitratorPF
    +process.hltDeepInclusiveMergedVerticesPF
    +process.hltDeepSecondaryVertexTagInfosPFMod
    +process.hltDeepCombinedSecondaryVertexBJetTagsInfosMod
    +process.hltDeepCombinedSecondaryVertexBJetTagsPFMod)


process.hltBTagPFCHSDeepCSV4p5Triple = cms.EDFilter("HLTPFJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 3 ),
    JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFMod','probb' ),
    TriggerType = cms.int32( 86 ),
    # Jets = cms.InputTag( "hltPFCHSJetForBtag" ),
    Jets = cms.InputTag( "hltAK4PFCHSJetsCorrected" ),
    # Jets = cms.InputTag( "hltAK4PFCHSJets" ),
    MinTag = cms.double( 0.24 ),
    MaxTag = cms.double( 999999.0 )
)


process.hltPFPuppiCentralJetQuad30 = process.hltPFCHSCentralJetQuad30.clone(inputTag ="hltAK4PuppiJetsCorrected")

process.hlt1PFPuppiCentralJet75 = process.hlt1PFCHSCentralJet75.clone(inputTag = "hltAK4PuppiJetsCorrected")

process.hlt2PFPuppiCentralJet60 = process.hlt2PFCHSCentralJet60.clone(inputTag = "hltAK4PuppiJetsCorrected")

process.hlt3PFPuppiCentralJet45 = process.hlt3PFCHSCentralJet45.clone(inputTag = "hltAK4PuppiJetsCorrected")

process.hlt4PFPuppiCentralJet40 = process.hlt4PFCHSCentralJet40.clone(inputTag = "hltAK4PuppiJetsCorrected")

process.hltPFPuppiCentralJetQuad30forHt = process.hltPFCHSCentralJetQuad30forHt.clone(HLTObject = "hltPFPuppiCentralJetQuad30" )

process.hltHtMhtPFPuppiCentralJetsQuadC30 = process.hltHtMhtPFCHSCentralJetsQuadC30.clone(jetsLabel =  "hltPFPuppiCentralJetQuad30forHt")

process.hltPFPuppiCentralJetsQuad30HT330 = cms.EDFilter( "HLTHtMhtFilter",
    saveTags = cms.bool( True ),
    mhtLabels = cms.VInputTag( 'hltHtMhtPFPuppiCentralJetsQuadC30' ),
    meffSlope = cms.vdouble( 1.0 ),
    minHt = cms.vdouble( 330.0 ),
    minMht = cms.vdouble( 0.0 ),
    htLabels = cms.VInputTag( 'hltHtMhtPFPuppiCentralJetsQuadC30' ),
    minMeff = cms.vdouble( 0.0 )
)
process.hltDeepBLifetimeTagInfosPFPuppiMod = process.hltDeepBLifetimeTagInfosPFPuppi.clone(jets = "hltPFPuppiJetForBtag")
process.hltDeepSecondaryVertexTagInfosPFPuppiMod = process.hltDeepSecondaryVertexTagInfosPF.clone(trackIPTagInfos = "hltDeepBLifetimeTagInfosPFPuppiMod")
process.hltDeepCombinedSecondaryVertexBJetTagsInfosPuppiMod = process.hltDeepCombinedSecondaryVertexBJetTagsInfos.clone(svTagInfos = "hltDeepSecondaryVertexTagInfosPFPuppiMod")
process.hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod = process.hltDeepCombinedSecondaryVertexBJetTagsPF.clone(src = "hltDeepCombinedSecondaryVertexBJetTagsInfosPuppiMod")

process.HLTBtagDeepCSVSequencePFPuppiMod = cms.Sequence(
    process.hltPFPuppiJetForBtagSelector
    +process.hltPFPuppiJetForBtag
    +process.hltDeepBLifetimeTagInfosPFPuppiMod
    +process.hltDeepInclusiveVertexFinderPF
    +process.hltDeepInclusiveSecondaryVerticesPF
    +process.hltDeepTrackVertexArbitratorPF
    +process.hltDeepInclusiveMergedVerticesPF
    +process.hltDeepSecondaryVertexTagInfosPFPuppiMod
    +process.hltDeepCombinedSecondaryVertexBJetTagsInfosPuppiMod
    +process.hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod)


process.hltBTagPFPuppiDeepCSV4p5Triple = cms.EDFilter( "HLTPFJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 3 ),
    JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod','probb' ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltPFPuppiJetForBtag" ),
    MinTag = cms.double( 0.24 ),
    MaxTag = cms.double( 999999.0 )
)





process.hltDoublePFCHSJets128Eta2p3 = cms.EDFilter( "HLT1PFJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 128.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.3 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltAK4PFCHSJetsCorrected" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MaxMass = cms.double( -1.0 )
)

process.hltDoublePFCHSJets128Eta2p3MaxDeta1p6 = cms.EDFilter( "HLT2PFJetPFJet",
    saveTags = cms.bool( True ),
    MinMinv = cms.double( 0.0 ),
    originTag2 = cms.VInputTag( 'hltAK4PFCHSJetsCorrected' ),
    MinDelR = cms.double( 0.0 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    originTag1 = cms.VInputTag( 'hltAK4PFCHSJetsCorrected' ),
    triggerType1 = cms.int32( 85 ),
    triggerType2 = cms.int32( 85 ),
    MaxMinv = cms.double( 1.0E7 ),
    MinDeta = cms.double( -1000.0 ),
    MaxDelR = cms.double( 1000.0 ),
    inputTag1 = cms.InputTag( "hltDoublePFCHSJets128Eta2p3" ),
    inputTag2 = cms.InputTag( "hltDoublePFCHSJets128Eta2p3" ),
    MaxDphi = cms.double( 1.0E7 ),
    MaxDeta = cms.double( 1.6 ),
    MaxPt = cms.double( 1.0E7 ),
    MinDphi = cms.double( 0.0 )
)

process.hltSelectorPFCHSJets80L1FastJet = cms.EDFilter( "EtMinPFJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltAK4PFCHSJetsCorrected" ),
    etMin = cms.double( 80.0 )
)

process.hltSelector6PFCHSCentralJetsL1FastJet = cms.EDFilter( "LargestEtPFJetSelector",
    maxNumber = cms.uint32( 6 ),
    filter = cms.bool( False ),
    src = cms.InputTag( "hltSelectorPFCHSJets80L1FastJet" )
)

process.hltBTagPFCHSDeepCSV0p71Double6Jets80 = cms.EDFilter( "HLTPFJetTagWithMatching",
    saveTags = cms.bool( True ),
    deltaR = cms.double( 10.0 ),
    MinJets = cms.int32( 2 ),
    JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFMod','probb' ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltSelector6PFCHSCentralJetsL1FastJet" ),
    MinTag = cms.double( 0.52 ),
    MaxTag = cms.double( 999999.0 )
)



process.hltDoublePFPuppiJets128Eta2p3 = process.hltDoublePFCHSJets128Eta2p3.clone(
    inputTag = "hltAK4PuppiJetsCorrected",
)
process.hltDoublePFPuppiJets128Eta2p3MaxDeta1p6 =  cms.EDFilter( "HLT2PFJetPFJet",
    saveTags = cms.bool( True ),
    MinMinv = cms.double( 0.0 ),
    originTag2 = cms.VInputTag( 'hltAK4PuppiJetsCorrected' ),
    MinDelR = cms.double( 0.0 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    originTag1 = cms.VInputTag( 'hltAK4PuppiJetsCorrected' ),
    triggerType1 = cms.int32( 85 ),
    triggerType2 = cms.int32( 85 ),
    MaxMinv = cms.double( 1.0E7 ),
    MinDeta = cms.double( -1000.0 ),
    MaxDelR = cms.double( 1000.0 ),
    inputTag1 = cms.InputTag( "hltDoublePFPuppiJets128Eta2p3" ),
    inputTag2 = cms.InputTag( "hltDoublePFPuppiJets128Eta2p3" ),
    MaxDphi = cms.double( 1.0E7 ),
    MaxDeta = cms.double( 1.6 ),
    MaxPt = cms.double( 1.0E7 ),
    MinDphi = cms.double( 0.0 )
)

process.hltSelectorPFPuppiJets80L1FastJet = process.hltSelectorPFCHSJets80L1FastJet.clone(
    src = "hltAK4PuppiJetsCorrected"
)
process.hltSelector6PFPuppiCentralJetsL1FastJet = process.hltSelector6PFCHSCentralJetsL1FastJet.clone(
    src = "hltSelectorPFPuppiJets80L1FastJet"
)
process.hltBTagPFPuppiDeepCSV0p71Double6Jets80 = cms.EDFilter( "HLTPFJetTagWithMatching",
    saveTags = cms.bool( True ),
    deltaR = cms.double( 10.0 ),
    MinJets = cms.int32( 2 ),
    JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod','probb' ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltSelector6PFPuppiCentralJetsL1FastJet" ),
    MinTag = cms.double( 0.52 ),
    MaxTag = cms.double( 999999.0 )
)

## single-object filters
_singlePFJet100 = cms.EDFilter('HLT1PFJet',
  MaxEta = cms.double(5.0),
  MaxMass = cms.double(-1.0),
  MinE = cms.double(-1.0),
  MinEta = cms.double(-1.0),
  MinMass = cms.double(-1.0),
  MinN = cms.int32(1),
  MinPt = cms.double(100.0),
  inputTag = cms.InputTag(''),
  saveTags = cms.bool(True),
  triggerType = cms.int32(85),
)
process.hltSingleAK4PFCHSJet100 = _singlePFJet100.clone(inputTag = 'hltAK4PFCHSJetsCorrected', MinPt = 100.)
process.L1TPFCHSFilter90 = cms.EDFilter('L1TPFJetFilter',
    inputTag = cms.InputTag("ak4PFL1PuppiCorrected"),
    MinN = cms.int32(1),
    MinPt = cms.double(90.),
    saveTags = cms.bool(True)
)
process.L1TPuppiJetFilterN2Pt40 = cms.EDFilter('L1TPFJetFilter',
    inputTag = cms.InputTag("ak4PFL1PuppiCorrected"),
    MinN = cms.int32(2),
    MinPt = cms.double(40.),
    saveTags = cms.bool(True)
)
process.HLT_AK4PFCHSJet100_v1 = cms.Path(
    # process.L1TPFCHSFilter90
    process.HLTParticleFlowSequence
    + process.HLTAK4PFCHSJetsReconstruction
    + process.hltSingleAK4PFCHSJet100)

## paths
process.HLT_PFHT330PT30_QuadPFCHSJet_75_60_45_40_TriplePFCHSBTagDeepCSV_4p5_v1 = cms.Path(
    process.HLTParticleFlowSequence
    +process.HLTAK4PFCHSJetsReconstruction
    +process.hltPFCHSCentralJetQuad30
    +process.hlt1PFCHSCentralJet75
    +process.hlt2PFCHSCentralJet60
    +process.hlt3PFCHSCentralJet45
    +process.hlt4PFCHSCentralJet40
    +process.hltPFCHSCentralJetQuad30forHt
    +process.hltHtMhtPFCHSCentralJetsQuadC30
    +process.hltPFCHSCentralJetsQuad30HT330
    +process.HLTBtagDeepCSVSequencePFMod
    +process.hltBTagPFCHSDeepCSV4p5Triple
)

# process.hltL1DoubleJet112er2p3dEtaMax1p6
process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV_4p5_v1 = cms.Path(
    process.HLTParticleFlowSequence
    +process.HLTAK4PuppiJetsReconstruction
    +process.hltPFPuppiCentralJetQuad30
    +process.hlt1PFPuppiCentralJet75
    +process.hlt2PFPuppiCentralJet60
    +process.hlt3PFPuppiCentralJet45
    +process.hlt4PFPuppiCentralJet40
    +process.hltPFPuppiCentralJetQuad30forHt
    +process.hltHtMhtPFPuppiCentralJetsQuadC30
    +process.hltPFPuppiCentralJetsQuad30HT330  #problematic???
    +process.HLTBtagDeepCSVSequencePFPuppiMod
    +process.hltBTagPFPuppiDeepCSV4p5Triple
)

process.HLT_DoublePFCHSJets128MaxDeta1p6_DoublePFCHSBTagDeepCSV_p71_v1 = cms.Path(
    process.HLTParticleFlowSequence
    +process.HLTAK4PFCHSJetsReconstruction
    +process.hltSelectorPFCHSJets80L1FastJet
    +process.hltSelector6PFCHSCentralJetsL1FastJet
    +process.hltDoublePFCHSJets128Eta2p3
    +process.hltDoublePFCHSJets128Eta2p3MaxDeta1p6
    +process.HLTBtagDeepCSVSequencePFMod
    + process.hltBTagPFCHSDeepCSV0p71Double6Jets80
)

process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepCSV_p71_v1 = cms.Path(
    process.HLTParticleFlowSequence
    +process.HLTAK4PuppiJetsReconstruction
    +process.hltSelectorPFPuppiJets80L1FastJet
    +process.hltSelector6PFPuppiCentralJetsL1FastJet
    +process.hltDoublePFPuppiJets128Eta2p3
    +process.hltDoublePFPuppiJets128Eta2p3MaxDeta1p6
    +process.HLTBtagDeepCSVSequencePFPuppiMod
    + process.hltBTagPFPuppiDeepCSV0p71Double6Jets80
)




###
### job configuration (input, output, GT, etc)
###

# update process.GlobalTag.globaltag
if opts.globalTag is not None:
   process.GlobalTag.globaltag = opts.globalTag

# fix for AK4PF Phase-2 JECs
process.GlobalTag.toGet.append(cms.PSet(
  record = cms.string('JetCorrectionsRecord'),
  tag = cms.string('JetCorrectorParametersCollection_PhaseIIFall17_V5b_MC_AK4PF'),
  label = cms.untracked.string('AK4PF'),
))

# max number of events to be processed
process.maxEvents.input = opts.maxEvents

# number of events to be skipped
process.source.skipEvents = cms.untracked.uint32(opts.skipEvents)

# multi-threading settings
process.options.numberOfThreads = cms.untracked.uint32(opts.numThreads if (opts.numThreads > 1) else 1)
process.options.numberOfStreams = cms.untracked.uint32(opts.numStreams if (opts.numStreams > 1) else 1)

# show cmsRun summary at job completion
process.options.wantSummary = cms.untracked.bool(opts.wantSummary)

# EDM input
if opts.inputFiles:
   process.source.fileNames = opts.inputFiles
else:
   process.source.fileNames = [
        # '/store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/40000/F9F5095B-DC0A-6F48-8148-E221616F0C9E.root',
     # 'file:/afs/cern.ch/work/s/sewuchte/private/BTag_Upgrade/april_CMSSW_11_1_0_pre6/TestL1/CMSSW_11_1_0_pre6/src/RecoBTag/PerformanceMeasurements/python/Configs/testGENSIM.root',
     '/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/227B9AFA-2612-694B-A2E7-B566F92C4B55.root',
   ]
process.MessageLogger = cms.Service("MessageLogger",
       destinations   = cms.untracked.vstring('detailedInfo','debugInfo', 'critical','cerr'),
       critical       = cms.untracked.PSet(threshold = cms.untracked.string('ERROR')),
       detailedInfo   = cms.untracked.PSet(threshold = cms.untracked.string('INFO')),
       debugInfo   = cms.untracked.PSet(threshold = cms.untracked.string('DEBUG')),
       cerr           = cms.untracked.PSet(threshold  = cms.untracked.string('WARNING'))
)
process.schedule = cms.Schedule(*[
  process.HLT_AK4PFCHSJet100_v1,
  # process.HLT_PFHT330PT30_QuadPFCHSJet_75_60_45_40_TriplePFCHSBTagDeepCSV_4p5_v1,
  # process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV_4p5_v1,
  # process.HLT_DoublePFCHSJets128MaxDeta1p6_DoublePFCHSBTagDeepCSV_p71_v1,
  # process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepCSV_p71_v1,

])
# EDM output
process.RECOoutput = cms.OutputModule('PoolOutputModule',
  dataset = cms.untracked.PSet(
    dataTier = cms.untracked.string('RECO'),
    filterName = cms.untracked.string('')
  ),
  fileName = cms.untracked.string(opts.output),
  outputCommands = cms.untracked.vstring((
    'drop *',
    'keep edmTriggerResults_*_*_*',
  )),
  splitLevel = cms.untracked.int32(0)
)

process.RECOoutput_step = cms.EndPath(process.RECOoutput)
process.schedule.append(process.RECOoutput_step)

# dump content of cms.Process to python file
if opts.dumpPython is not None:
   open(opts.dumpPython, 'w').write(process.dumpPython())
