import FWCore.ParameterSet.Config as cms

def customizePFPatLikeJetsROI(process, type = "AK4PFCHS"):

    # set some default collection variables
    pfjets =                "hltAK4PFJetsForBTag" 
    PFDeepCSVTags =         "hltDeepCombinedSecondaryVertexBPFPatJetTagsROI"   #original pfDeepCSVJetTags
    #PFDeepFlavourTags =     "hltPFDeepFlavourJetTagsROI"                       #original pfDeepFlavourJetTagsSlimmedDeepFlavour
    payload =               "AK4PFHLT"                                      #original AK4PFchs
    hltVertices =           "hltVerticesPFFilterForBTag"                           #original offlinePrimaryVertices
    rho =                   "hltFixedGridRhoFastjetAllForBTag"                     #original fixedGridRhoFastjetAll

    siPixelClusters =       "hltSiPixelClusters"                            #original siPixelClusters
    ecalRecHit =            "hltEcalRecHit"                                 #original ecalRecHit
    hbhereco =              "hltHbhereco"                                   #original hbhereco
    hfreco =                "hltHfreco"                                     #original hfreco
    horeco =                "hltHoreco"                                     #original horeco
    rpcRecHits =            "hltRpcRecHits"                                 #original rpcRecHits
    tracks =                "hltMergedTracksForBTag"                               #original generalTracks

    puppi =                 "hltPFPuppi"                                    #original puppi

    particleFlow =          "hltParticleFlowForBTag"                               #original particleFlow
    beamSpot =              "hltOnlineBeamSpot"                             #original offlineBeamSpot

    # clone and modify the HLT BTV sequence/producers to remove the jet pt and eta selections from "jetsForBtag" and replace with pfjets
    process.hltDeepBLifetimePFPatTagInfosROI = process.hltDeepBLifetimeTagInfosPFROI.clone(
        jets = cms.InputTag( pfjets )
    )

    process.hltDeepSecondaryVertexPFPatTagInfosROI = process.hltDeepSecondaryVertexTagInfosPFROI.clone(
        trackIPTagInfos = cms.InputTag( "hltDeepBLifetimePFPatTagInfosROI" )
    )

    process.hltDeepCombinedSecondaryVertexBJetPatTagInfosROI = process.hltDeepCombinedSecondaryVertexBJetTagsInfosROI.clone(
        svTagInfos = cms.InputTag( "hltDeepSecondaryVertexPFPatTagInfosROI" )
    )

    process.hltDeepCombinedSecondaryVertexBPFPatJetTagsROI = process.hltDeepCombinedSecondaryVertexBJetTagsPFROI.clone(
        src = cms.InputTag( "hltDeepCombinedSecondaryVertexBJetPatTagInfosROI" )
    )

    process.HLTBtagDeepCSVSequencePFPatROI = cms.Sequence(
        process.hltVerticesPFForBTag
        + process.hltVerticesPFSelectorForBTag
        + process.hltVerticesPFFilterForBTag
        + process.hltDeepBLifetimePFPatTagInfosROI
        + process.hltDeepInclusiveVertexFinderPFROI
        + process.hltDeepInclusiveSecondaryVerticesPFROI
        + process.hltDeepTrackVertexArbitratorPFROI
        + process.hltDeepInclusiveMergedVerticesPFROI
        + process.hltDeepSecondaryVertexPFPatTagInfosROI
        + process.hltDeepCombinedSecondaryVertexBJetPatTagInfosROI
        + process.hltDeepCombinedSecondaryVertexBPFPatJetTagsROI
    )



    # create patJets  for ak4pfchs and all necessary missing inputs
    from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets
    process.hltPatJetsROI = patJets.clone(
        JetFlavourInfoSource = cms.InputTag("hltPatJetFlavourAssociationROI"),
        JetPartonMapSource = cms.InputTag("hltPatJetFlavourAssociationLegacyROI"),
        addJetID = cms.bool(False),
        addTagInfos = cms.bool(True),
        discriminatorSources = cms.VInputTag(
            cms.InputTag(PFDeepCSVTags,"probb"),cms.InputTag(PFDeepCSVTags,"probc"),cms.InputTag(PFDeepCSVTags,"probudsg"),
            # cms.InputTag(PFDeepCSVTags,"probbb"), # hltDeepCSV: probb = probb +probbb
            #cms.InputTag(PFDeepFlavourTags,"probb"), cms.InputTag(PFDeepFlavourTags,"probc"), cms.InputTag(PFDeepFlavourTags,"probg"),
            #cms.InputTag(PFDeepFlavourTags,"problepb"), cms.InputTag(PFDeepFlavourTags,"probbb"), cms.InputTag(PFDeepFlavourTags,"probuds"),
        ),
        embedGenPartonMatch = cms.bool(False),
        genJetMatch = cms.InputTag("hltPatJetGenJetMatchROI"),
        genPartonMatch = cms.InputTag("hltPatJetPartonMatchROI"),
        jetChargeSource = cms.InputTag("hltPatJetChargeROI"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("hltPatJetCorrFactorsROI")),
        jetIDMap = cms.InputTag("hltAk4JetIDROI"),
        jetSource = cms.InputTag(pfjets),
        tagInfoSources = cms.VInputTag(
            cms.InputTag("hltDeepBLifetimePFPatTagInfosROI"),
            cms.InputTag("hltDeepCombinedSecondaryVertexBJetPatTagInfosROI"),
            cms.InputTag("hltDeepSecondaryVertexPFPatTagInfosROI"),
            #cms.InputTag("hltPFDeepFlavourTagInfosROI"),
        ),
        trackAssociationSource = cms.InputTag("hltAk4JetTracksAssociatorAtVertexPFROI"),
    )


    # for patJets
    from PhysicsTools.PatAlgos.mcMatchLayer0.jetFlavourId_cff import patJetFlavourAssociation,patJetPartons,patJetFlavourAssociationLegacy,patJetPartonAssociationLegacy,patJetPartonsLegacy
    process.hltPatJetFlavourAssociationROI = patJetFlavourAssociation.clone(
        bHadrons = cms.InputTag("hltPatJetPartons","bHadrons"),
        cHadrons = cms.InputTag("hltPatJetPartons","cHadrons"),
        jets = cms.InputTag(pfjets),
        leptons = cms.InputTag("hltPatJetPartons","leptons"),
        partons = cms.InputTag("hltPatJetPartons","physicsPartons"),
    )
    process.hltPatJetPartonsROI = patJetPartons.clone()

    process.hltPatJetFlavourAssociationLegacyROI = patJetFlavourAssociationLegacy.clone(
        srcByReference = cms.InputTag("hltPatJetPartonAssociationLegacyROI")
    )

    process.hltPatJetPartonAssociationLegacyROI = patJetPartonAssociationLegacy.clone(
        jets = cms.InputTag(pfjets),
        partons = cms.InputTag("hltPatJetPartonsLegacyROI")
    )

    process.hltPatJetPartonsLegacyROI = patJetPartonsLegacy.clone(
        src = cms.InputTag("genParticles"),
    )

    from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch
    process.hltPatJetGenJetMatchROI = patJetGenJetMatch.clone(
        matched = cms.InputTag("hltSlimmedGenJets"),
        src = cms.InputTag(pfjets)
    )

    from PhysicsTools.PatAlgos.slimming.slimmedGenJets_cfi import slimmedGenJets
    process.hltSlimmedGenJets = slimmedGenJets.clone(
        packedGenParticles = cms.InputTag("hltPackedGenParticles"),
        src = cms.InputTag("ak4GenJetsNoNu")
    )

    from PhysicsTools.PatAlgos.slimming.packedGenParticles_cfi import packedGenParticles
    process.hltPackedGenParticles = packedGenParticles.clone(
        inputCollection = cms.InputTag("hltPrunedGenParticlesWithStatusOne"),
        inputOriginal = cms.InputTag("genParticles"),
        map = cms.InputTag("hltPrunedGenParticles"),
    )

    from PhysicsTools.PatAlgos.slimming.genParticles_cff import prunedGenParticlesWithStatusOne
    from PhysicsTools.PatAlgos.slimming.prunedGenParticles_cfi import prunedGenParticles
    process.hltPrunedGenParticlesWithStatusOne = prunedGenParticlesWithStatusOne.clone(
        src = cms.InputTag("genParticles")
    )

    process.hltPrunedGenParticles = prunedGenParticles.clone(
        src = cms.InputTag("hltPrunedGenParticlesWithStatusOne")
    )

    from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetPartonMatch
    process.hltPatJetPartonMatchROI = patJetPartonMatch.clone(
        matched = cms.InputTag("hltPrunedGenParticles"),
        src = cms.InputTag(pfjets)
    )

    from PhysicsTools.PatAlgos.recoLayer0.jetTracksCharge_cff import patJetCharge
    process.hltPatJetChargeROI = patJetCharge.clone(
        src = cms.InputTag("hltAk4JetTracksAssociatorAtVertexPFROI"),
    )

    from RecoJets.JetAssociationProducers.ak4JTA_cff import ak4JetTracksAssociatorAtVertexPF
    process.hltAk4JetTracksAssociatorAtVertexPFROI = ak4JetTracksAssociatorAtVertexPF.clone(
        jets = cms.InputTag(pfjets),
        pvSrc = cms.InputTag(hltVertices),
        tracks = cms.InputTag(tracks),
    )

    from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi  import patJetCorrFactors
    process.hltPatJetCorrFactorsROI = patJetCorrFactors.clone(
        payload = cms.string(payload),
        primaryVertices = cms.InputTag(hltVertices),
        rho = cms.InputTag(rho),
        src = cms.InputTag(pfjets),
    )

    from RecoJets.JetProducers.ak4JetID_cfi import ak4JetID
    process.hltAk4JetIDROI = ak4JetID.clone(
        ebRecHitsColl = cms.InputTag(ecalRecHit,"EcalRecHitsEB"),
        eeRecHitsColl = cms.InputTag(ecalRecHit,"EcalRecHitsEE"),
        hbheRecHitsColl = cms.InputTag(hbhereco),
        hfRecHitsColl = cms.InputTag(hfreco),
        hoRecHitsColl = cms.InputTag(horeco),
        rpcRecHits = cms.InputTag(rpcRecHits),
        src = cms.InputTag("hltAK4CaloJets"),
    )



    #### TAGGERS
    # run DeepFlavour for HLT
    from RecoBTag.ONNXRuntime.pfDeepFlavourJetTags_cfi import pfDeepFlavourJetTags
    #process.hltPFDeepFlavourJetTagsROI = pfDeepFlavourJetTags.clone(
    #    src = cms.InputTag("hltPFDeepFlavourTagInfosROI")
    #)

    #from RecoBTag.FeatureTools.pfDeepFlavourTagInfos_cfi import pfDeepFlavourTagInfos
    #process.hltPFDeepFlavourTagInfosROI = pfDeepFlavourTagInfos.clone(
    #    candidates = cms.InputTag(particleFlow),
    #    jets = cms.InputTag(pfjets),
    #    puppi_value_map = cms.InputTag(puppi),
    #    secondary_vertices = cms.InputTag("hltDeepInclusiveSecondaryVerticesPFROI"),
    #    shallow_tag_infos = cms.InputTag("hltDeepCombinedSecondaryVertexBJetPatTagInfosROI"),
    #    vertex_associator = cms.InputTag("hltPrimaryVertexAssociationROI","original"),
    #    vertices = cms.InputTag(hltVertices)
    #)

    from RecoBTag.SecondaryVertex.candidateCombinedSecondaryVertexV2Computer_cfi import candidateCombinedSecondaryVertexV2Computer
    process.candidateCombinedSecondaryVertexV2Computer = candidateCombinedSecondaryVertexV2Computer.clone()

    from PhysicsTools.PatAlgos.slimming.primaryVertexAssociation_cfi import primaryVertexAssociation
    process.hltPrimaryVertexAssociationROI = primaryVertexAssociation.clone(
        jets = cms.InputTag(pfjets),
        particles = cms.InputTag(particleFlow),
        vertices = cms.InputTag(hltVertices),
    )

    #from RecoParticleFlow.PFProducer.chargedHadronPFTrackIsolation_cfi import chargedHadronPFTrackIsolation
    #process.hltChargedHadronPFTrackIsolationROI = chargedHadronPFTrackIsolation.clone(
    #    src = cms.InputTag(particleFlow)
    #)


    # create the final path
    process.MC_JetsMatchingPathROI = cms.Path(
        process.HLTAK4PFJetsSequenceForBTag
        *process.HLTBtagDeepCSVSequencePFPatROI
        *process.hltPrunedGenParticlesWithStatusOne
        *process.hltPrunedGenParticles
        *process.hltPackedGenParticles
        *process.hltPatJetPartonMatchROI
        *process.hltSlimmedGenJets
        *process.hltAk4JetIDROI
        *process.hltPatJetGenJetMatchROI
        *process.hltPatJetPartonsLegacyROI
        *process.hltPatJetPartonAssociationLegacyROI
        *process.hltPatJetFlavourAssociationLegacyROI
        *process.hltPatJetPartonsROI
        *process.hltPatJetFlavourAssociationROI
        *process.hltAk4JetTracksAssociatorAtVertexPFROI
        *process.hltPatJetChargeROI
        *process.hltPatJetCorrFactorsROI

        *process.hltPrimaryVertexAssociationROI
        # *process.hltChargedHadronPFTrackIsolationROI
        #*process.hltPFDeepFlavourTagInfosROI
        #*process.hltPFDeepFlavourJetTagsROI

        *process.hltPatJetsROI
        )


    if process.schedule_():
        process.schedule.extend([process.MC_JetsMatchingPathROI])

    return process




