import FWCore.ParameterSet.Config as cms

def customize_hltPhase2_BTV_paths(reco="HLT_TRKv06p1_TICL",  BTVreco="cutsV2", name='HLTBTVPaths'):

    opt_skimTracks = False

    opt_reco = reco
    if opt_reco.endswith('_skimmedTracks'):
       opt_reco = opt_reco[:-len('_skimmedTracks')]
       opt_skimTracks = True

    if   opt_reco == 'HLT_TRKv00':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv00_cfg      import cms, process
    elif opt_reco == 'HLT_TRKv00_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv00_TICL_cfg import cms, process
    elif opt_reco == 'HLT_TRKv02':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv02_cfg      import cms, process
    elif opt_reco == 'HLT_TRKv02_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv02_TICL_cfg import cms, process
    elif opt_reco == 'HLT_TRKv06':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv06_cfg      import cms, process
    elif opt_reco == 'HLT_TRKv06_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv06_TICL_cfg import cms, process
    elif opt_reco == 'HLT_TRKv06p1':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv06p1_cfg      import cms, process
    elif opt_reco == 'HLT_TRKv06p1_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv06p1_TICL_cfg import cms, process
    elif opt_reco == 'HLT_TRKv07p2':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv07p2_cfg      import cms, process
    elif opt_reco == 'HLT_TRKv07p2_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv07p2_TICL_cfg import cms, process
    else:
       logmsg = '\n\n'+' '*2+'Valid arguments for option "reco" are'
       for recoArg in [
         'HLT_TRKv00',
         'HLT_TRKv00_TICL',
         'HLT_TRKv02',
         'HLT_TRKv02_TICL',
         'HLT_TRKv06',
         'HLT_TRKv06_TICL',
         'HLT_TRKv06p1',
         'HLT_TRKv06p1_TICL',
         'HLT_TRKv07p2',
         'HLT_TRKv07p2_TICL',
       ]:
         logmsg += '\n'+' '*4+recoArg
       raise RuntimeError('invalid argument for option "reco": "'+opt_reco+'"'+logmsg+'\n')


    # skimming of tracks
    if opt_skimTracks:
       from JMETriggerAnalysis.Common.hltPhase2_skimmedTracks import customize_hltPhase2_skimmedTracks
       process = customize_hltPhase2_skimmedTracks(process)


    opt_BTVreco = BTVreco
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
        logmsg = '\n\n'+' '*2+'Valid arguments for option "BTVreco" are'
        for recoArg in [
            'default',
            'cutsV1',
            'cutsV2',
        ]:
            logmsg += '\n'+' '*4+recoArg
        raise RuntimeError('invalid argument for option "BTVreco": "'+opt_BTVreco+'"')

    ###
    ### filter for QCD muon enriched
    ###
    process.muGenFilter = cms.EDFilter("MCSmartSingleParticleFilter",
        MaxDecayRadius = cms.untracked.vdouble(2000.0, 2000.0),
        MaxDecayZ = cms.untracked.vdouble(4000.0, 4000.0),
        MaxEta = cms.untracked.vdouble(4.5, 4.5),
        MinDecayZ = cms.untracked.vdouble(-4000.0, -4000.0),
        MinEta = cms.untracked.vdouble(-4.5, -4.5),
        MinPt = cms.untracked.vdouble(5.0, 5.0),
        ParticleID = cms.untracked.vint32(13, -13),
        Status = cms.untracked.vint32(1, 1),
        moduleLabel = cms.untracked.InputTag("generatorSmeared","","SIM")
    )


    ###
    ### single filters and producers
    ###

    process.hltPFPuppiCentralJetQuad30MaxEta4p5 = cms.EDFilter( "HLT1PFJet",
        saveTags = cms.bool( True ),
        MinPt = cms.double( 30.0 ),
        # MinPt = cms.double( 10.0 ),
        MinN = cms.int32( 4 ),
        # MinN = cms.int32( 1 ),
        MaxEta = cms.double( 4.5 ),
        MinEta = cms.double( -4.5 ),
        MinMass = cms.double( -1.0 ),
        inputTag = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
        MinE = cms.double( -1.0 ),
        triggerType = cms.int32( 86 ),
        MaxMass = cms.double( -1.0 )
    )
    process.hltPFPuppiCentralJetQuad30MaxEta2p4 = process.hltPFPuppiCentralJetQuad30MaxEta4p5.clone(
        MaxEta = cms.double( 2.4 ),
        MinEta = cms.double( -2.4 )
    )

    process.hlt1PFPuppiCentralJet75MaxEta4p5 = cms.EDFilter( "HLT1PFJet",
        saveTags = cms.bool( True ),
        MinPt = cms.double( 75.0 ),
        # MinPt = cms.double( 10.0 ),
        MinN = cms.int32( 1 ),
        MaxEta = cms.double( 4.5 ),
        MinEta = cms.double( -4.5 ),
        MinMass = cms.double( -1.0 ),
        inputTag = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
        MinE = cms.double( -1.0 ),
        triggerType = cms.int32( 0 ),
        MaxMass = cms.double( -1.0 )
    )
    process.hlt1PFPuppiCentralJet75MaxEta2p4 = process.hlt1PFPuppiCentralJet75MaxEta4p5.clone(
        MaxEta = cms.double( 2.4 ),
        MinEta = cms.double( -2.4 )
    )

    process.hlt2PFPuppiCentralJet60MaxEta4p5 = cms.EDFilter( "HLT1PFJet",
        saveTags = cms.bool( True ),
        MinPt = cms.double( 60.0 ),
        # MinPt = cms.double( 10.0 ),
        MinN = cms.int32( 2 ),
        MaxEta = cms.double( 4.5 ),
        MinEta = cms.double( -4.5 ),
        MinMass = cms.double( -1.0 ),
        inputTag = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
        MinE = cms.double( -1.0 ),
        triggerType = cms.int32( 0 ),
        MaxMass = cms.double( -1.0 )
    )
    process.hlt2PFPuppiCentralJet60MaxEta2p4 = process.hlt2PFPuppiCentralJet60MaxEta4p5.clone(
        MaxEta = cms.double( 2.4 ),
        MinEta = cms.double( -2.4 )
    )

    process.hlt3PFPuppiCentralJet45MaxEta4p5 = cms.EDFilter( "HLT1PFJet",
        saveTags = cms.bool( True ),
        MinPt = cms.double( 45.0 ),
        # MinPt = cms.double( 10.0 ),
        MinN = cms.int32( 3 ),
        MaxEta = cms.double( 4.5 ),
        MinEta = cms.double( -4.5 ),
        MinMass = cms.double( -1.0 ),
        inputTag = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
        MinE = cms.double( -1.0 ),
        triggerType = cms.int32( 0 ),
        MaxMass = cms.double( -1.0 )
    )
    process.hlt3PFPuppiCentralJet45MaxEta2p4 = process.hlt3PFPuppiCentralJet45MaxEta4p5.clone(
        MaxEta = cms.double( 2.4 ),
        MinEta = cms.double( -2.4 )
    )

    process.hlt4PFPuppiCentralJet40MaxEta4p5 = cms.EDFilter( "HLT1PFJet",
        saveTags = cms.bool( True ),
        MinPt = cms.double( 40.0 ),
        # MinPt = cms.double( 10.0 ),
        MinN = cms.int32( 4 ),
        MaxEta = cms.double( 4.5 ),
        MinEta = cms.double( -4.5 ),
        MinMass = cms.double( -1.0 ),
        inputTag = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
        MinE = cms.double( -1.0 ),
        triggerType = cms.int32( 0 ),
        MaxMass = cms.double( -1.0 )
    )
    process.hlt4PFPuppiCentralJet40MaxEta2p4 = process.hlt4PFPuppiCentralJet40MaxEta4p5.clone(
        MaxEta = cms.double( 2.4 ),
        MinEta = cms.double( -2.4 )
    )

    # process.hltPFPuppiCentralJetQuad30forHtMaxEta4p5 = cms.EDProducer( "HLTPFJetCollectionProducer",
    #     TriggerTypes = cms.vint32( 86 ),
    #     HLTObject = cms.InputTag( "hltPFPuppiCentralJetQuad30MaxEta4p5" )
    # )
    # process.hltPFPuppiCentralJetQuad30forHtMaxEta2p4 = process.hltPFPuppiCentralJetQuad30forHtMaxEta4p5.clone(
    #     HLTObject = cms.InputTag( "hltPFPuppiCentralJetQuad30MaxEta2p4" )
    # )

    process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta4p5 = cms.EDProducer( "HLTHtMhtProducer",
        usePt = cms.bool( True ),
        minPtJetHt = cms.double( 30.0 ),
        maxEtaJetMht = cms.double( 4.5 ),
        minNJetMht = cms.int32( 0 ),
        # jetsLabel = cms.InputTag( "hltPFPuppiCentralJetQuad30forHtMaxEta4p5" ),
        jetsLabel = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
        maxEtaJetHt = cms.double( 4.5 ),
        minPtJetMht = cms.double( 0.0 ),
        minNJetHt = cms.int32( 4 ),
        # pfCandidatesLabel = cms.InputTag("particleFlowTmp"),
        pfCandidatesLabel = cms.InputTag(""),
        excludePFMuons = cms.bool( False )
    )
    process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4 = process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta4p5.clone(
        maxEtaJetHt = cms.double( 2.4 ),
        maxEtaJetMht = cms.double( 2.4 ),
    )


    process.hltPFPuppiCentralJetsQuad30HT330MaxEta4p5 = cms.EDFilter( "HLTHtMhtFilter",
        saveTags = cms.bool( True ),
        mhtLabels = cms.VInputTag( ['hltHtMhtPFPuppiCentralJetsQuadC30MaxEta4p5'] ),
        meffSlope = cms.vdouble( 1.0 ),
        minHt = cms.vdouble( 330.0 ),
        # minHt = cms.vdouble( 10.0 ),
        minMht = cms.vdouble( 0.0 ),
        htLabels = cms.VInputTag( ['hltHtMhtPFPuppiCentralJetsQuadC30MaxEta4p5'] ),
        minMeff = cms.vdouble( 0.0 )
    )
    process.hltPFPuppiCentralJetsQuad30HT330MaxEta2p4 = process.hltPFPuppiCentralJetsQuad30HT330MaxEta4p5.clone(
        mhtLabels = cms.VInputTag( ['hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4'] ),
        htLabels = cms.VInputTag( ['hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4'] ),
    )

    # modified sequence
    # process.hltDeepBLifetimeTagInfosPFPuppiMod = process.hltDeepBLifetimeTagInfosPFPuppi.clone(jets = "hltPFPuppiJetForBtag")
    # process.hltDeepBLifetimeTagInfosPFPuppiMod = process.hltDeepBLifetimeTagInfosPFPuppi.clone(jets = "hltAK4PFPuppiJets")
    # process.hltDeepSecondaryVertexTagInfosPFPuppiMod = process.hltDeepSecondaryVertexTagInfosPF.clone(trackIPTagInfos = "hltDeepBLifetimeTagInfosPFPuppiMod")
    # process.hltDeepCombinedSecondaryVertexBJetTagsInfosPuppiMod = process.hltDeepCombinedSecondaryVertexBJetTagsInfos.clone(svTagInfos = "hltDeepSecondaryVertexTagInfosPFPuppiMod")
    # process.hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod = process.hltDeepCombinedSecondaryVertexBJetTagsPF.clone(src = "hltDeepCombinedSecondaryVertexBJetTagsInfosPuppiMod")

    # process.HLTBtagDeepCSVSequencePFPuppiMod = cms.Sequence(
    #     # process.hltPFPuppiJetForBtagSelector
    #     # +process.hltPFPuppiJetForBtag
    #     process.hltDeepBLifetimeTagInfosPFPuppiMod
    #     +process.hltDeepInclusiveVertexFinderPF
    #     +process.hltDeepInclusiveSecondaryVerticesPF
    #     +process.hltDeepTrackVertexArbitratorPF
    #     +process.hltDeepInclusiveMergedVerticesPF
    #     +process.hltDeepSecondaryVertexTagInfosPFPuppiMod
    #     +process.hltDeepCombinedSecondaryVertexBJetTagsInfosPuppiMod
    #     +process.hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod)


    process.hltBTagPFPuppiDeepCSV0p5Eta4p5Triple = cms.EDFilter( "HLTPFJetTag",
        saveTags = cms.bool( True ),
        MinJets = cms.int32( 3 ),
        # MinJets = cms.int32( 1 ),
        # JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod','probb' ),
        JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppi','probb' ),
        TriggerType = cms.int32( 86 ),
        # Jets = cms.InputTag( "hltPFPuppiJetForBtag" ),
        Jets = cms.InputTag( "hltAK4PFPuppiJets" ),
        MinTag = cms.double( 0.5 ),
        # MinTag = cms.double( 0.01 ),
        MaxTag = cms.double( 999999.0 )
    )
    # process.hltBTagPFPuppiDeepCSV0p5Eta2p4Triple = cms.EDFilter( "HLTPFJetTag",
    #     saveTags = cms.bool( True ),
    #     MinJets = cms.int32( 3 ),
    #     # MinJets = cms.int32( 1 ),
    #     # JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod','probb' ),
    #     JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppi','probb' ),
    #     TriggerType = cms.int32( 86 ),
    #     # Jets = cms.InputTag( "hltPFPuppiJetForBtag" ),
    #     Jets = cms.InputTag( "hltAK4PFPuppiJets_" ),
    #     MinTag = cms.double( 0.5 ),
    #     # MinTag = cms.double( 0.01 ),
    #     MaxTag = cms.double( 999999.0 )
    # )
    process.hltBTagPFPuppiDeepCSV0p7Eta4p5Triple = cms.EDFilter( "HLTPFJetTag",
        saveTags = cms.bool( True ),
        MinJets = cms.int32( 3 ),
        # MinJets = cms.int32( 1 ),
        # JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod','probb' ),
        JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppi','probb' ),
        TriggerType = cms.int32( 86 ),
        # Jets = cms.InputTag( "hltPFPuppiJetForBtag" ),
        Jets = cms.InputTag( "hltAK4PFPuppiJets" ),
        MinTag = cms.double( 0.7 ),
        # MinTag = cms.double( 0.01 ),
        MaxTag = cms.double( 999999.0 )
    )
    process.hltBTagPFPuppiDeepCSV0p85Eta4p5Triple = cms.EDFilter( "HLTPFJetTag",
        saveTags = cms.bool( True ),
        MinJets = cms.int32( 3 ),
        # MinJets = cms.int32( 1 ),
        # JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod','probb' ),
        JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppi','probb' ),
        TriggerType = cms.int32( 86 ),
        # Jets = cms.InputTag( "hltPFPuppiJetForBtag" ),
        Jets = cms.InputTag( "hltAK4PFPuppiJets" ),
        MinTag = cms.double( 0.85 ),
        # MinTag = cms.double( 0.01 ),
        MaxTag = cms.double( 999999.0 )
    )
    process.hltBTagPFPuppiDeepFlavour0p5Eta4p5Triple = cms.EDFilter( "HLTPFJetTag",
        saveTags = cms.bool( True ),
        MinJets = cms.int32( 3 ),
        # MinJets = cms.int32( 1 ),
        # JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod','probb' ),
        JetTags = cms.InputTag( 'hltPfDeepFlavourJetTags','probb' ),
        TriggerType = cms.int32( 86 ),
        # Jets = cms.InputTag( "hltPFPuppiJetForBtag" ),
        Jets = cms.InputTag( "hltAK4PFPuppiJets" ),
        MinTag = cms.double( 0.5 ),
        # MinTag = cms.double( 0.01 ),
        MaxTag = cms.double( 999999.0 )
    )
    process.hltBTagPFPuppiDeepFlavour0p7Eta4p5Triple = cms.EDFilter( "HLTPFJetTag",
        saveTags = cms.bool( True ),
        MinJets = cms.int32( 3 ),
        # MinJets = cms.int32( 1 ),
        # JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod','probb' ),
        JetTags = cms.InputTag( 'hltPfDeepFlavourJetTags','probb' ),
        TriggerType = cms.int32( 86 ),
        # Jets = cms.InputTag( "hltPFPuppiJetForBtag" ),
        Jets = cms.InputTag( "hltAK4PFPuppiJets" ),
        MinTag = cms.double( 0.7 ),
        # MinTag = cms.double( 0.01 ),
        MaxTag = cms.double( 999999.0 )
    )
    process.hltBTagPFPuppiDeepFlavour0p85Eta4p5Triple = cms.EDFilter( "HLTPFJetTag",
        saveTags = cms.bool( True ),
        MinJets = cms.int32( 3 ),
        # MinJets = cms.int32( 1 ),
        # JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod','probb' ),
        JetTags = cms.InputTag( 'hltPfDeepFlavourJetTags','probb' ),
        TriggerType = cms.int32( 86 ),
        # Jets = cms.InputTag( "hltPFPuppiJetForBtag" ),
        Jets = cms.InputTag( "hltAK4PFPuppiJets" ),
        MinTag = cms.double( 0.85 ),
        # MinTag = cms.double( 0.01 ),
        MaxTag = cms.double( 999999.0 )
    )

    process.hltDoublePFPuppiJets128MaxEta4p5 = cms.EDFilter( "HLT1PFJet",
        saveTags = cms.bool( True ),
        # MinPt = cms.double( 128.0 ),
        MinPt = cms.double( 180.0 ),
        # MinPt = cms.double( 10.0 ),
        MinN = cms.int32( 2 ),
        MaxEta = cms.double( 4.5 ),
        MinEta = cms.double( -4.5 ),
        MinMass = cms.double( -1.0 ),
        inputTag = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
        MinE = cms.double( -1.0 ),
        triggerType = cms.int32( 85 ),
        MaxMass = cms.double( -1.0 )
    )
    process.hltDoublePFPuppiJets128MaxEta2p4 = process.hltDoublePFPuppiJets128MaxEta4p5.clone(
        MaxEta = cms.double( 2.4 ),
        MinEta = cms.double( -2.4 )
    )

    # process.hltDoublePFPuppiJets128Eta4p5MaxDeta1p6 =  cms.EDFilter( "HLT2PFJetPFJet",
    #     saveTags = cms.bool( True ),
    #     MinMinv = cms.double( 0.0 ),
    #     originTag2 = cms.VInputTag( 'hltAK4PFPuppiJetsCorrected' ),
    #     MinDelR = cms.double( 0.0 ),
    #     MinPt = cms.double( 0.0 ),
    #     MinN = cms.int32( 1 ),
    #     originTag1 = cms.VInputTag( 'hltAK4PFPuppiJetsCorrected' ),
    #     triggerType1 = cms.int32( 85 ),
    #     triggerType2 = cms.int32( 85 ),
    #     MaxMinv = cms.double( 1.0E7 ),
    #     MinDeta = cms.double( -1000.0 ),
    #     MaxDelR = cms.double( 1000.0 ),
    #     # inputTag1 = cms.InputTag( "hltDoublePFPuppiJets128MaxEta4p5" ),
    #     # inputTag2 = cms.InputTag( "hltDoublePFPuppiJets128MaxEta4p5" ),
    #     inputTag1 = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
    #     inputTag2 = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
    #     MaxDphi = cms.double( 1.0E7 ),
    #     MaxDeta = cms.double( 1.6 ),
    #     MaxPt = cms.double( 1.0E7 ),
    #     MinDphi = cms.double( 0.0 )
    # )
    # process.hltDoublePFPuppiJets128Eta2p4MaxDeta1p6 = process.hltDoublePFPuppiJets128Eta4p5MaxDeta1p6.clone(
    #     inputTag1 = cms.InputTag( "hltDoublePFPuppiJets128MaxEta2p4" ),
    #     inputTag2 = cms.InputTag( "hltDoublePFPuppiJets128MaxEta2p4" ),
    # )

    process.hltSelectorPFPuppiJets80L1FastJet = cms.EDFilter( "EtMinPFJetSelector",
        filter = cms.bool( False ),
        src = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
        etMin = cms.double( 80.0 )
        # etMin = cms.double( 10.0 )
    )
    process.hltSelector6PFPuppiCentralJetsL1FastJet = cms.EDFilter( "LargestEtPFJetSelector",
        maxNumber = cms.uint32( 6 ),
        filter = cms.bool( False ),
        src = cms.InputTag( "hltSelectorPFPuppiJets80L1FastJet" )
    )

    process.hltBTagPFPuppiDeepCSV0p5Double6Jets80 = cms.EDFilter( "HLTPFJetTagWithMatching",
        saveTags = cms.bool( True ),
        deltaR = cms.double( 0.1 ),
        MinJets = cms.int32( 2 ),
        # JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod','probb' ),
        JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppi','probb' ),
        TriggerType = cms.int32( 86 ),
        Jets = cms.InputTag( "hltSelector6PFPuppiCentralJetsL1FastJet" ),
        MinTag = cms.double( 0.5 ),
        # MinTag = cms.double( 0.01 ),
        MaxTag = cms.double( 999999.0 )
    )
    process.hltBTagPFPuppiDeepCSV0p7Double6Jets80 = cms.EDFilter( "HLTPFJetTagWithMatching",
        saveTags = cms.bool( True ),
        deltaR = cms.double( 0.1 ),
        MinJets = cms.int32( 2 ),
        # JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod','probb' ),
        JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppi','probb' ),
        TriggerType = cms.int32( 86 ),
        Jets = cms.InputTag( "hltSelector6PFPuppiCentralJetsL1FastJet" ),
        MinTag = cms.double( 0.7 ),
        # MinTag = cms.double( 0.01 ),
        MaxTag = cms.double( 999999.0 )
    )
    process.hltBTagPFPuppiDeepCSV0p85Double6Jets80 = cms.EDFilter( "HLTPFJetTagWithMatching",
        saveTags = cms.bool( True ),
        deltaR = cms.double( 0.1 ),
        MinJets = cms.int32( 2 ),
        # JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod','probb' ),
        JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppi','probb' ),
        TriggerType = cms.int32( 86 ),
        Jets = cms.InputTag( "hltSelector6PFPuppiCentralJetsL1FastJet" ),
        MinTag = cms.double( 0.85 ),
        # MinTag = cms.double( 0.01 ),
        MaxTag = cms.double( 999999.0 )
    )
    process.hltBTagPFPuppiDeepFlavour0p5Double6Jets80 = cms.EDFilter( "HLTPFJetTagWithMatching",
        saveTags = cms.bool( True ),
        deltaR = cms.double( 0.1 ),
        MinJets = cms.int32( 2 ),
        # JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod','probb' ),
        JetTags = cms.InputTag( 'hltPfDeepFlavourJetTags','probb' ),
        TriggerType = cms.int32( 86 ),
        Jets = cms.InputTag( "hltSelector6PFPuppiCentralJetsL1FastJet" ),
        MinTag = cms.double( 0.5 ),
        # MinTag = cms.double( 0.01 ),
        MaxTag = cms.double( 999999.0 )
    )
    process.hltBTagPFPuppiDeepFlavour0p7Double6Jets80 = cms.EDFilter( "HLTPFJetTagWithMatching",
        saveTags = cms.bool( True ),
        deltaR = cms.double( 0.1 ),
        MinJets = cms.int32( 2 ),
        # JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod','probb' ),
        JetTags = cms.InputTag( 'hltPfDeepFlavourJetTags','probb' ),
        TriggerType = cms.int32( 86 ),
        Jets = cms.InputTag( "hltSelector6PFPuppiCentralJetsL1FastJet" ),
        MinTag = cms.double( 0.7 ),
        # MinTag = cms.double( 0.01 ),
        MaxTag = cms.double( 999999.0 )
    )
    process.hltBTagPFPuppiDeepFlavour0p85Double6Jets80 = cms.EDFilter( "HLTPFJetTagWithMatching",
        saveTags = cms.bool( True ),
        deltaR = cms.double( 0.1 ),
        MinJets = cms.int32( 2 ),
        # JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppiMod','probb' ),
        JetTags = cms.InputTag( 'hltPfDeepFlavourJetTags','probb' ),
        TriggerType = cms.int32( 86 ),
        Jets = cms.InputTag( "hltSelector6PFPuppiCentralJetsL1FastJet" ),
        MinTag = cms.double( 0.85 ),
        # MinTag = cms.double( 0.01 ),
        MaxTag = cms.double( 999999.0 )
    )



    ## L1 sequences and filters  (from JME)

    process.l1tSinglePFPuppiJet200offMaxEta2p4 = cms.EDFilter('L1JetFilter',
      inputTag = cms.InputTag('l1tSlwPFPuppiJetsCorrected', 'Phase1L1TJetFromPfCandidates'),
      esScalingTag = cms.ESInputTag('L1TScalingESSource', 'L1PFPhase1JetScaling'),
      MinPt = cms.double(200.),
      MinEta = cms.double(-2.4),
      MaxEta = cms.double(2.4),
      MinN = cms.int32(1),
    )

    process.l1tDoublePFPuppiJet112offMaxEta2p4 = cms.EDFilter('L1JetFilter',
      inputTag = cms.InputTag('l1tSlwPFPuppiJetsCorrected', 'Phase1L1TJetFromPfCandidates'),
      esScalingTag = cms.ESInputTag('L1TScalingESSource', 'L1PFPhase1JetScaling'),
      MinPt = cms.double(112.),
      MinEta = cms.double(-2.4),
      MaxEta = cms.double(2.4),
      MinN = cms.int32(2),
    )

    process.l1t1PFPuppiJet70offMaxEta2p4 = cms.EDFilter('L1JetFilter',
      inputTag = cms.InputTag('l1tSlwPFPuppiJetsCorrected', 'Phase1L1TJetFromPfCandidates'),
      esScalingTag = cms.ESInputTag('L1TScalingESSource', 'L1PFPhase1JetScaling'),
      MinPt = cms.double(70.),
      MinEta = cms.double(-2.4),
      MaxEta = cms.double(2.4),
      MinN = cms.int32(1),
    )

    process.l1t2PFPuppiJet55offMaxEta2p4 = cms.EDFilter('L1JetFilter',
      inputTag = cms.InputTag('l1tSlwPFPuppiJetsCorrected', 'Phase1L1TJetFromPfCandidates'),
      esScalingTag = cms.ESInputTag('L1TScalingESSource', 'L1PFPhase1JetScaling'),
      MinPt = cms.double(55.),
      MinEta = cms.double(-2.4),
      MaxEta = cms.double(2.4),
      MinN = cms.int32(2),
    )

    process.l1t4PFPuppiJet40offMaxEta2p4 = cms.EDFilter('L1JetFilter',
      inputTag = cms.InputTag('l1tSlwPFPuppiJetsCorrected', 'Phase1L1TJetFromPfCandidates'),
      esScalingTag = cms.ESInputTag('L1TScalingESSource', 'L1PFPhase1JetScaling'),
      MinPt = cms.double(40.),
      MinEta = cms.double(-2.4),
      MaxEta = cms.double(2.4),
      MinN = cms.int32(4),
    )

    # L1T-HT
    process.l1tPFPuppiHTMaxEta2p4 = cms.EDProducer('HLTHtMhtProducer',
      jetsLabel = cms.InputTag('l1tSlwPFPuppiJetsCorrected', 'Phase1L1TJetFromPfCandidates'),
      minPtJetHt = cms.double(30.),
      maxEtaJetHt = cms.double(2.4)
    )

    process.l1tPFPuppiHT450offMaxEta2p4 = cms.EDFilter('L1EnergySumFilter',
      inputTag = cms.InputTag('l1tPFPuppiHTMaxEta2p4'),
      esScalingTag = cms.ESInputTag('L1TScalingESSource', 'L1PFPhase1HT090Scaling'),
      TypeOfSum = cms.string('HT'),
      MinPt = cms.double(450.),
    )

    process.l1tPFPuppiHT400offMaxEta2p4 = cms.EDFilter('L1EnergySumFilter',
      inputTag = cms.InputTag('l1tPFPuppiHTMaxEta2p4'),
      esScalingTag = cms.ESInputTag('L1TScalingESSource', 'L1PFPhase1HT090Scaling'),
      TypeOfSum = cms.string('HT'),
      MinPt = cms.double(400.),
    )




    ## paths
    # needed L1 seed
    # process.hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet = cms.EDFilter( "HLTL1TSeed",
    #     L1SeedsLogicalExpression = cms.string( "L1_QuadJet60er2p5 OR L1_HTT280er OR L1_HTT320er OR L1_HTT360er OR L1_ETT2000 OR L1_HTT400er OR L1_HTT450er OR L1_HTT280er_QuadJet_70_55_40_35_er2p4 OR L1_HTT320er_QuadJet_70_55_40_40_er2p4 OR L1_HTT320er_QuadJet_80_60_er2p1_45_40_er2p3 OR L1_HTT320er_QuadJet_80_60_er2p1_50_45_er2p3" ),

    process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV0p5_4p5_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta4p5
        +process.hlt1PFPuppiCentralJet75MaxEta4p5
        +process.hlt2PFPuppiCentralJet60MaxEta4p5
        +process.hlt3PFPuppiCentralJet45MaxEta4p5
        +process.hlt4PFPuppiCentralJet40MaxEta4p5
        # +process.hltPFPuppiCentralJetQuad30forHtMaxEta4p5
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta4p5
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta4p5
        # +process.HLTBtagDeepCSVSequencePFPuppiMod
        +process.HLTBtagDeepCSVSequencePFPuppi
        +process.hltBTagPFPuppiDeepCSV0p5Eta4p5Triple
    )
    process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV0p7_4p5_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta4p5
        +process.hlt1PFPuppiCentralJet75MaxEta4p5
        +process.hlt2PFPuppiCentralJet60MaxEta4p5
        +process.hlt3PFPuppiCentralJet45MaxEta4p5
        +process.hlt4PFPuppiCentralJet40MaxEta4p5
        # +process.hltPFPuppiCentralJetQuad30forHtMaxEta4p5
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta4p5
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta4p5
        # +process.HLTBtagDeepCSVSequencePFPuppiMod
        +process.HLTBtagDeepCSVSequencePFPuppi
        +process.hltBTagPFPuppiDeepCSV0p7Eta4p5Triple
    )
    process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV0p85_4p5_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta4p5
        +process.hlt1PFPuppiCentralJet75MaxEta4p5
        +process.hlt2PFPuppiCentralJet60MaxEta4p5
        +process.hlt3PFPuppiCentralJet45MaxEta4p5
        +process.hlt4PFPuppiCentralJet40MaxEta4p5
        # +process.hltPFPuppiCentralJetQuad30forHtMaxEta4p5
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta4p5
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta4p5
        # +process.HLTBtagDeepCSVSequencePFPuppiMod
        +process.HLTBtagDeepCSVSequencePFPuppi
        +process.hltBTagPFPuppiDeepCSV0p85Eta4p5Triple
    )
    process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV0p5_2p4_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta2p4
        +process.hlt1PFPuppiCentralJet75MaxEta2p4
        +process.hlt2PFPuppiCentralJet60MaxEta2p4
        +process.hlt3PFPuppiCentralJet45MaxEta2p4
        +process.hlt4PFPuppiCentralJet40MaxEta2p4
        # +process.hltPFPuppiCentralJetQuad30forHtMaxEta2p4
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta2p4
        # +process.HLTBtagDeepCSVSequencePFPuppiMod
        +process.HLTBtagDeepCSVSequencePFPuppi
        +process.hltBTagPFPuppiDeepCSV0p5Eta4p5Triple
    )
    process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV0p7_2p4_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta2p4
        +process.hlt1PFPuppiCentralJet75MaxEta2p4
        +process.hlt2PFPuppiCentralJet60MaxEta2p4
        +process.hlt3PFPuppiCentralJet45MaxEta2p4
        +process.hlt4PFPuppiCentralJet40MaxEta2p4
        # +process.hltPFPuppiCentralJetQuad30forHtMaxEta2p4
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta2p4
        # +process.HLTBtagDeepCSVSequencePFPuppiMod
        +process.HLTBtagDeepCSVSequencePFPuppi
        +process.hltBTagPFPuppiDeepCSV0p7Eta4p5Triple
    )
    process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV0p85_2p4_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta2p4
        +process.hlt1PFPuppiCentralJet75MaxEta2p4
        +process.hlt2PFPuppiCentralJet60MaxEta2p4
        +process.hlt3PFPuppiCentralJet45MaxEta2p4
        +process.hlt4PFPuppiCentralJet40MaxEta2p4
        # +process.hltPFPuppiCentralJetQuad30forHtMaxEta2p4
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta2p4
        # +process.HLTBtagDeepCSVSequencePFPuppiMod
        +process.HLTBtagDeepCSVSequencePFPuppi
        +process.hltBTagPFPuppiDeepCSV0p85Eta4p5Triple
    )
    process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepFlavour0p5_4p5_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta4p5
        +process.hlt1PFPuppiCentralJet75MaxEta4p5
        +process.hlt2PFPuppiCentralJet60MaxEta4p5
        +process.hlt3PFPuppiCentralJet45MaxEta4p5
        +process.hlt4PFPuppiCentralJet40MaxEta4p5
        # +process.hltPFPuppiCentralJetQuad30forHtMaxEta4p5
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta4p5
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta4p5
        +process.HLTBtagDeepFlavourSequencePFPuppi
        +process.hltBTagPFPuppiDeepFlavour0p5Eta4p5Triple
    )
    process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepFlavour0p7_4p5_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta4p5
        +process.hlt1PFPuppiCentralJet75MaxEta4p5
        +process.hlt2PFPuppiCentralJet60MaxEta4p5
        +process.hlt3PFPuppiCentralJet45MaxEta4p5
        +process.hlt4PFPuppiCentralJet40MaxEta4p5
        # +process.hltPFPuppiCentralJetQuad30forHtMaxEta4p5
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta4p5
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta4p5
        +process.HLTBtagDeepFlavourSequencePFPuppi
        +process.hltBTagPFPuppiDeepFlavour0p7Eta4p5Triple
    )
    process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepFlavour0p85_4p5_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta4p5
        +process.hlt1PFPuppiCentralJet75MaxEta4p5
        +process.hlt2PFPuppiCentralJet60MaxEta4p5
        +process.hlt3PFPuppiCentralJet45MaxEta4p5
        +process.hlt4PFPuppiCentralJet40MaxEta4p5
        # +process.hltPFPuppiCentralJetQuad30forHtMaxEta4p5
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta4p5
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta4p5
        +process.HLTBtagDeepFlavourSequencePFPuppi
        +process.hltBTagPFPuppiDeepFlavour0p85Eta4p5Triple
    )
    process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepFlavour0p5_2p4_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta2p4
        +process.hlt1PFPuppiCentralJet75MaxEta2p4
        +process.hlt2PFPuppiCentralJet60MaxEta2p4
        +process.hlt3PFPuppiCentralJet45MaxEta2p4
        +process.hlt4PFPuppiCentralJet40MaxEta2p4
        # +process.hltPFPuppiCentralJetQuad30forHtMaxEta2p4
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta2p4
        +process.HLTBtagDeepFlavourSequencePFPuppi
        +process.hltBTagPFPuppiDeepFlavour0p5Eta4p5Triple
    )
    process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepFlavour0p7_2p4_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta2p4
        +process.hlt1PFPuppiCentralJet75MaxEta2p4
        +process.hlt2PFPuppiCentralJet60MaxEta2p4
        +process.hlt3PFPuppiCentralJet45MaxEta2p4
        +process.hlt4PFPuppiCentralJet40MaxEta2p4
        # +process.hltPFPuppiCentralJetQuad30forHtMaxEta2p4
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta2p4
        +process.HLTBtagDeepFlavourSequencePFPuppi
        +process.hltBTagPFPuppiDeepFlavour0p7Eta4p5Triple
    )
    process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepFlavour0p85_2p4_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta2p4
        +process.hlt1PFPuppiCentralJet75MaxEta2p4
        +process.hlt2PFPuppiCentralJet60MaxEta2p4
        +process.hlt3PFPuppiCentralJet45MaxEta2p4
        +process.hlt4PFPuppiCentralJet40MaxEta2p4
        # +process.hltPFPuppiCentralJetQuad30forHtMaxEta2p4
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta2p4
        +process.HLTBtagDeepFlavourSequencePFPuppi
        +process.hltBTagPFPuppiDeepFlavour0p85Eta4p5Triple
    )

    process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_2p4_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta2p4
        +process.hlt1PFPuppiCentralJet75MaxEta2p4
        +process.hlt2PFPuppiCentralJet60MaxEta2p4
        +process.hlt3PFPuppiCentralJet45MaxEta2p4
        +process.hlt4PFPuppiCentralJet40MaxEta2p4
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta2p4
    )

    process.HLTNoL1_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_2p4_v1 = cms.Path(
        process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta2p4
        +process.hlt1PFPuppiCentralJet75MaxEta2p4
        +process.hlt2PFPuppiCentralJet60MaxEta2p4
        +process.hlt3PFPuppiCentralJet45MaxEta2p4
        +process.hlt4PFPuppiCentralJet40MaxEta2p4
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta2p4
    )

    process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_4p5_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta4p5
        +process.hlt1PFPuppiCentralJet75MaxEta4p5
        +process.hlt2PFPuppiCentralJet60MaxEta4p5
        +process.hlt3PFPuppiCentralJet45MaxEta4p5
        +process.hlt4PFPuppiCentralJet40MaxEta4p5
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta4p5
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta4p5
    )
    process.HLTNoL1_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_4p5_v1 = cms.Path(
        process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta4p5
        +process.hlt1PFPuppiCentralJet75MaxEta4p5
        +process.hlt2PFPuppiCentralJet60MaxEta4p5
        +process.hlt3PFPuppiCentralJet45MaxEta4p5
        +process.hlt4PFPuppiCentralJet40MaxEta4p5
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta4p5
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta4p5
    )

    process.HLT_QuadPFPuppiJet_75_60_45_40_2p4_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta2p4
        +process.hlt1PFPuppiCentralJet75MaxEta2p4
        +process.hlt2PFPuppiCentralJet60MaxEta2p4
        +process.hlt3PFPuppiCentralJet45MaxEta2p4
        +process.hlt4PFPuppiCentralJet40MaxEta2p4
    )
    process.HLTNoL1_QuadPFPuppiJet_75_60_45_40_2p4_v1 = cms.Path(
        process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta2p4
        +process.hlt1PFPuppiCentralJet75MaxEta2p4
        +process.hlt2PFPuppiCentralJet60MaxEta2p4
        +process.hlt3PFPuppiCentralJet45MaxEta2p4
        +process.hlt4PFPuppiCentralJet40MaxEta2p4
    )

    process.HLT_QuadPFPuppiJet_75_60_45_40_4p5_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta4p5
        +process.hlt1PFPuppiCentralJet75MaxEta4p5
        +process.hlt2PFPuppiCentralJet60MaxEta4p5
        +process.hlt3PFPuppiCentralJet45MaxEta4p5
        +process.hlt4PFPuppiCentralJet40MaxEta4p5
    )
    process.HLTNoL1_QuadPFPuppiJet_75_60_45_40_4p5_v1 = cms.Path(
        process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta4p5
        +process.hlt1PFPuppiCentralJet75MaxEta4p5
        +process.hlt2PFPuppiCentralJet60MaxEta4p5
        +process.hlt3PFPuppiCentralJet45MaxEta4p5
        +process.hlt4PFPuppiCentralJet40MaxEta4p5
    )

    process.L1_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV_2p4_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
    )
    process.QCDMuon = cms.Path(
        process.muGenFilter
    )


    # needed L1 seed
    # process.hltL1DoubleJet112er2p3dEtaMax1p6 = cms.EDFilter( "HLTL1TSeed",
    #     L1SeedsLogicalExpression = cms.string( "L1_DoubleJet100er2p3_dEta_Max1p6 OR L1_DoubleJet112er2p3_dEta_Max1p6 OR L1_DoubleJet150er2p5" ),

    process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepCSV_p5_4p5_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltSelectorPFPuppiJets80L1FastJet
        +process.hltSelector6PFPuppiCentralJetsL1FastJet
        +process.hltDoublePFPuppiJets128MaxEta4p5
        # +process.hltDoublePFPuppiJets128Eta4p5MaxDeta1p6
        # +process.HLTBtagDeepCSVSequencePFPuppiMod
        +process.HLTBtagDeepCSVSequencePFPuppi
        +process.hltBTagPFPuppiDeepCSV0p5Double6Jets80
    )
    process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepCSV_p7_4p5_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltSelectorPFPuppiJets80L1FastJet
        +process.hltSelector6PFPuppiCentralJetsL1FastJet
        +process.hltDoublePFPuppiJets128MaxEta4p5
        # +process.hltDoublePFPuppiJets128Eta4p5MaxDeta1p6
        # +process.HLTBtagDeepCSVSequencePFPuppiMod
        +process.HLTBtagDeepCSVSequencePFPuppi
        +process.hltBTagPFPuppiDeepCSV0p7Double6Jets80
    )
    process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepCSV_p85_4p5_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltSelectorPFPuppiJets80L1FastJet
        +process.hltSelector6PFPuppiCentralJetsL1FastJet
        +process.hltDoublePFPuppiJets128MaxEta4p5
        # +process.hltDoublePFPuppiJets128Eta4p5MaxDeta1p6
        # +process.HLTBtagDeepCSVSequencePFPuppiMod
        +process.HLTBtagDeepCSVSequencePFPuppi
        +process.hltBTagPFPuppiDeepCSV0p85Double6Jets80
    )
    process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepCSV_p5_2p4_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltSelectorPFPuppiJets80L1FastJet
        +process.hltSelector6PFPuppiCentralJetsL1FastJet
        +process.hltDoublePFPuppiJets128MaxEta2p4
        # +process.hltDoublePFPuppiJets128Eta2p4MaxDeta1p6
        # +process.HLTBtagDeepCSVSequencePFPuppiMod
        +process.HLTBtagDeepCSVSequencePFPuppi
        +process.hltBTagPFPuppiDeepCSV0p5Double6Jets80
    )
    process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepCSV_p7_2p4_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltSelectorPFPuppiJets80L1FastJet
        +process.hltSelector6PFPuppiCentralJetsL1FastJet
        +process.hltDoublePFPuppiJets128MaxEta2p4
        # +process.hltDoublePFPuppiJets128Eta2p4MaxDeta1p6
        # +process.HLTBtagDeepCSVSequencePFPuppiMod
        +process.HLTBtagDeepCSVSequencePFPuppi
        +process.hltBTagPFPuppiDeepCSV0p7Double6Jets80
    )
    process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepCSV_p85_2p4_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltSelectorPFPuppiJets80L1FastJet
        +process.hltSelector6PFPuppiCentralJetsL1FastJet
        +process.hltDoublePFPuppiJets128MaxEta2p4
        # +process.hltDoublePFPuppiJets128Eta2p4MaxDeta1p6
        # +process.HLTBtagDeepCSVSequencePFPuppiMod
        +process.HLTBtagDeepCSVSequencePFPuppi
        +process.hltBTagPFPuppiDeepCSV0p85Double6Jets80
    )
    process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepFlavour_p5_4p5_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltSelectorPFPuppiJets80L1FastJet
        +process.hltSelector6PFPuppiCentralJetsL1FastJet
        +process.hltDoublePFPuppiJets128MaxEta4p5
        # +process.hltDoublePFPuppiJets128Eta4p5MaxDeta1p6
        +process.HLTBtagDeepFlavourSequencePFPuppi
        +process.hltBTagPFPuppiDeepFlavour0p5Double6Jets80
    )
    process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepFlavour_p7_4p5_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltSelectorPFPuppiJets80L1FastJet
        +process.hltSelector6PFPuppiCentralJetsL1FastJet
        +process.hltDoublePFPuppiJets128MaxEta4p5
        # +process.hltDoublePFPuppiJets128Eta4p5MaxDeta1p6
        +process.HLTBtagDeepFlavourSequencePFPuppi
        +process.hltBTagPFPuppiDeepFlavour0p7Double6Jets80
    )
    process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepFlavour_p85_4p5_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltSelectorPFPuppiJets80L1FastJet
        +process.hltSelector6PFPuppiCentralJetsL1FastJet
        +process.hltDoublePFPuppiJets128MaxEta4p5
        # +process.hltDoublePFPuppiJets128Eta4p5MaxDeta1p6
        +process.HLTBtagDeepFlavourSequencePFPuppi
        +process.hltBTagPFPuppiDeepFlavour0p85Double6Jets80
    )
    process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepFlavour_p5_2p4_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltSelectorPFPuppiJets80L1FastJet
        +process.hltSelector6PFPuppiCentralJetsL1FastJet
        +process.hltDoublePFPuppiJets128MaxEta2p4
        # +process.hltDoublePFPuppiJets128Eta2p4MaxDeta1p6
        +process.HLTBtagDeepFlavourSequencePFPuppi
        +process.hltBTagPFPuppiDeepFlavour0p5Double6Jets80
    )
    process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepFlavour_p7_2p4_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltSelectorPFPuppiJets80L1FastJet
        +process.hltSelector6PFPuppiCentralJetsL1FastJet
        +process.hltDoublePFPuppiJets128MaxEta2p4
        # +process.hltDoublePFPuppiJets128Eta2p4MaxDeta1p6
        +process.HLTBtagDeepFlavourSequencePFPuppi
        +process.hltBTagPFPuppiDeepFlavour0p7Double6Jets80
    )
    process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepFlavour_p85_2p4_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltSelectorPFPuppiJets80L1FastJet
        +process.hltSelector6PFPuppiCentralJetsL1FastJet
        +process.hltDoublePFPuppiJets128MaxEta2p4
        # +process.hltDoublePFPuppiJets128Eta2p4MaxDeta1p6
        +process.HLTBtagDeepFlavourSequencePFPuppi
        +process.hltBTagPFPuppiDeepFlavour0p85Double6Jets80
    )

    process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppi_2p4_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltSelectorPFPuppiJets80L1FastJet
        +process.hltSelector6PFPuppiCentralJetsL1FastJet
        +process.hltDoublePFPuppiJets128MaxEta2p4
    )

    process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppi_4p5_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltSelectorPFPuppiJets80L1FastJet
        +process.hltSelector6PFPuppiCentralJetsL1FastJet
        +process.hltDoublePFPuppiJets128MaxEta4p5
    )

    process.HLTNoL1_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppi_2p4_v1 = cms.Path(
        process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltSelectorPFPuppiJets80L1FastJet
        +process.hltSelector6PFPuppiCentralJetsL1FastJet
        +process.hltDoublePFPuppiJets128MaxEta2p4
    )

    process.HLTNoL1_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppi_4p5_v1 = cms.Path(
        process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltSelectorPFPuppiJets80L1FastJet
        +process.hltSelector6PFPuppiCentralJetsL1FastJet
        +process.hltDoublePFPuppiJets128MaxEta4p5
    )

    process.L1_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepCSV_p71_2p4_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
    )

    process.noFilter_PFDeepCSVPuppi = cms.Path(
        process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.HLTBtagDeepCSVSequencePFPuppi
    )
    process.noFilter_PFDeepFlavourPuppi = cms.Path(
        process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.HLTBtagDeepFlavourSequencePFPuppi
    )

    process.L1Objects = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
    )
    process.HLTObjects = cms.Path(
        process.HLTParticleFlowSequence
        # +process.HLTPFPuppiJMEReconstruction
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiHT
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta4p5
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4
    )

    process.schedule_().extend([
      process.L1_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV_2p4_v1,
      process.L1_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepCSV_p71_2p4_v1,

      process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppi_2p4_v1,
      process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppi_4p5_v1,
      process.HLTNoL1_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppi_2p4_v1,
      process.HLTNoL1_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppi_4p5_v1,

      process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_2p4_v1,
      process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_4p5_v1,
      process.HLT_QuadPFPuppiJet_75_60_45_40_2p4_v1,
      process.HLT_QuadPFPuppiJet_75_60_45_40_4p5_v1,
      process.HLTNoL1_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_2p4_v1,
      process.HLTNoL1_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_4p5_v1,
      process.HLTNoL1_QuadPFPuppiJet_75_60_45_40_2p4_v1,
      process.HLTNoL1_QuadPFPuppiJet_75_60_45_40_4p5_v1,

      process.L1Objects,
      process.HLTObjects,
      process.QCDMuon,
      process.noFilter_PFDeepCSVPuppi,
      process.noFilter_PFDeepFlavourPuppi,

      process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV0p5_4p5_v1,
      process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepCSV_p5_4p5_v1,
      process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepFlavour0p5_4p5_v1,
      process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepFlavour_p5_4p5_v1,
      process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV0p7_4p5_v1,
      process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepCSV_p7_4p5_v1,
      process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepFlavour0p7_4p5_v1,
      process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepFlavour_p7_4p5_v1,
      process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV0p85_4p5_v1,
      process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepCSV_p85_4p5_v1,
      process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepFlavour0p85_4p5_v1,
      process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepFlavour_p85_4p5_v1,

      process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV0p5_2p4_v1,
      process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepCSV_p5_2p4_v1,
      process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepFlavour0p5_2p4_v1,
      process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepFlavour_p5_2p4_v1,
      process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV0p7_2p4_v1,
      process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepCSV_p7_2p4_v1,
      process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepFlavour0p7_2p4_v1,
      process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepFlavour_p7_2p4_v1,
      process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV0p85_2p4_v1,
      process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepCSV_p85_2p4_v1,
      process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepFlavour0p85_2p4_v1,
      process.HLT_DoublePFPuppiJets128MaxDeta1p6_DoublePFPuppiBTagDeepFlavour_p85_2p4_v1,
    ])

    # EDM output
    # process.RECOoutput = cms.OutputModule('PoolOutputModule',
    #   dataset = cms.untracked.PSet(
    #     dataTier = cms.untracked.string('RECO'),
    #     filterName = cms.untracked.string('')
    #   ),
    #   fileName = cms.untracked.string(opts.output),
    #   outputCommands = cms.untracked.vstring((
    #     'drop *',
    #     'keep edmTriggerResults_*_*_*',
    #   )),
    #   splitLevel = cms.untracked.int32(0)
    # )

    # process.RECOoutput_step = cms.EndPath(process.RECOoutput)
    # process.schedule.append(process.RECOoutput_step)

    return process


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

opts.register('runTiming', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'run timing instead of rates')

opts.register('runRates', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'run rates')

opts.parseArguments()

###
### base configuration file
### (choice of reconstruction sequence)
###
if opts.runRates or opts.runTiming:
# flag: skim original collection of generalTracks (only tracks associated to first N pixel vertices)



    process = customize_hltPhase2_BTV_paths(opts.reco, opts.BTVreco)

    process.CondDB.connect = 'sqlite_fip:RecoBTag/PerformanceMeasurements/data/L1TObjScaling.db'
    process.L1TScalingESSource.connect = 'sqlite_fip:RecoBTag/PerformanceMeasurements/data/L1TObjScaling.db'


    # ES modules for thresholds of L1T seeds
    # if not hasattr(process, 'CondDB'):
    #   process.load('CondCore.CondDB.CondDB_cfi')

    # process.CondDB.connect = 'sqlite_file:/afs/cern.ch/user/t/tomei/public/L1TObjScaling.db'
    #
    # process.L1TScalingESSource = cms.ESSource('PoolDBESSource',
    #   process.CondDB,
    #   DumpStat = cms.untracked.bool(True),
    #   toGet = cms.VPSet(
    #     cms.PSet(
    #       record = cms.string('L1TObjScalingRcd'),
    #       tag = cms.string('L1TkMuonScaling'),
    #       label = cms.untracked.string('L1TkMuonScaling'),
    #     ),
    #     cms.PSet(
    #       record = cms.string('L1TObjScalingRcd'),
    #       tag = cms.string('L1PFJetScaling'),
    #       label = cms.untracked.string('L1PFPhase1JetScaling'),
    #     ),
    #     cms.PSet(
    #       record = cms.string('L1TObjScalingRcd'),
    #       tag = cms.string('L1TkElectronScaling'),
    #       label = cms.untracked.string('L1TkEleScaling'),
    #     ),
    #     cms.PSet(
    #       record = cms.string('L1TObjScalingRcd'),
    #       tag = cms.string('L1PuppiMETScaling'),
    #       label = cms.untracked.string('L1PuppiMETScaling'),
    #     ),
    #     cms.PSet(
    #       record = cms.string('L1TObjScalingRcd'),
    #       tag = cms.string('L1PFPhase1HT090Scaling'),
    #       label = cms.untracked.string('L1PFPhase1HT090Scaling'),
    #     ),
    #   ),
    # )
    #
    # process.es_prefer_l1tscaling = cms.ESPrefer('PoolDBESSource', 'L1TScalingESSource')


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

    if opts.runTiming:
        # multi-threading settings
        process.options.numberOfThreads = cms.untracked.uint32(opts.numThreads if (opts.numThreads > 1) else 1)
        process.options.numberOfStreams = cms.untracked.uint32(opts.numStreams if (opts.numStreams > 1) else 1)
        process.options.sizeOfStackForThreadsInKB = cms.untracked.uint32(10240)
    else:
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
         # 'file:/afs/cern.ch/work/s/sewuchte/private/BTag_Upgrade/april_CMSSW_11_1_0_pre6/TestL1/CMSSW_11_1_0_pre6/src/RecoBTag/PerformanceMeasurements/python/Configs/testGENSIM.root',
         # '/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/227B9AFA-2612-694B-A2E7-B566F92C4B55.root',
         '/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/250000/95FB2E3E-1DA2-FC4C-82D6-0BEB5C0195E3.root',
         '/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/04A2C9E2-531E-0144-A9D2-3CD1AF1B717B.root',
         '/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/056EE608-658E-B746-85A1-E189887D91BB.root',
         '/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/36259A74-FA1A-4544-8F98-75EB06B95502.root',
         '/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/4B764BEA-EF4A-8D4C-8219-B67879262C7A.root',
         '/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/4D651B4A-055A-5E4B-8A04-6FA9F02993CD.root',
         '/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/59DF47B9-C055-184B-8498-8FBAA598122A.root',
         '/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/6F8F0DA8-D538-D34B-9481-94629FC22F13.root',
         '/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/7B25764B-ABD1-8048-8FA9-85AA44CFEDAF.root',
         '/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/854AB663-F7EA-1A45-A946-AC706C06FCF3.root',
         '/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/9A2AE12D-F77F-EB43-A5A7-AE1F98DE88AE.root',
         '/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/9C935A67-56EF-DC4D-B027-55EDD163AB4B.root',
         '/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/BB01CD1E-C25E-AD48-931F-2F24E2CAC8C7.root',
         '/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/BF8056B5-7F83-F34C-A463-706664DCF18C.root',
       ]
    # process.MessageLogger = cms.Service("MessageLogger",
    #        destinations   = cms.untracked.vstring('detailedInfo','debugInfo', 'critical','cerr'),
    #        critical       = cms.untracked.PSet(threshold = cms.untracked.string('ERROR')),
    #        detailedInfo   = cms.untracked.PSet(threshold = cms.untracked.string('INFO')),
    #        debugInfo   = cms.untracked.PSet(threshold = cms.untracked.string('DEBUG')),
    #        cerr           = cms.untracked.PSet(threshold  = cms.untracked.string('WARNING'))
    # )


    # if opts.runRates:
    #     # EDM output
    #     process.RECOoutput = cms.OutputModule('PoolOutputModule',
    #       dataset = cms.untracked.PSet(
    #         dataTier = cms.untracked.string('RECO'),
    #         filterName = cms.untracked.string('')
    #       ),
    #       fileName = cms.untracked.string(opts.output),
    #       outputCommands = cms.untracked.vstring((
    #         'drop *',
    #         'keep edmTriggerResults_*_*_*',
    #       )),
    #       splitLevel = cms.untracked.int32(0)
    #     )

    if opts.runTiming:
        #timing test
        from HLTrigger.Timer.FastTimer import customise_timer_service_print,customise_timer_service,customise_timer_service_singlejob
        process = customise_timer_service_print(process)
        process = customise_timer_service(process)
        # process = customise_timer_service_singlejob(process)
        process.FastTimerService.dqmTimeRange            = 20000.
        process.FastTimerService.dqmTimeResolution       =    10.
        process.FastTimerService.dqmPathTimeRange        = 10000.
        process.FastTimerService.dqmPathTimeResolution   =     5.
        process.FastTimerService.dqmModuleTimeRange      =  1000.
        process.FastTimerService.dqmModuleTimeResolution =     1.
        # process.dqmOutput.fileName = cms.untracked.string(opts.output)

    # if opts.runRates:


    if opts.runRates:
        # dump content of cms.Process to python file
        if opts.dumpPython is not None:
           open(opts.dumpPython, 'w').write(process.dumpPython())

        print 'process.GlobalTag.globaltag =', process.GlobalTag.globaltag
        print 'dumpPython =', opts.dumpPython
        print 'option: reco =', opt_reco, '(skimTracks = '+str(opt_skimTracks)+')'
        print 'option: BTVreco =', opt_BTVreco
