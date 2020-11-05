import FWCore.ParameterSet.Config as cms

def customize_HLT_trkIter2GlobalPtSeedXX(process,ptVal=0.9):

  ptStr = str(ptVal).replace(".","p")

  setattr(process,"hltIter2PFlowPixelTrackingRegionsGlobalPtSeed"+ptStr,
          cms.EDProducer( 'GlobalTrackingRegionWithVerticesEDProducer',
                          RegionPSet = cms.PSet( 
                            useFixedError = cms.bool( True ),
                            nSigmaZ = cms.double( 4.0 ),
                            VertexCollection = cms.InputTag( 'hltTrimmedPixelVertices' ),
                            beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
                            useFoundVertices = cms.bool( True ),
                            fixedError = cms.double( 0.2 ),
                            sigmaZVertex = cms.double( 3.0 ),
                            useFakeVertices = cms.bool( False ),
                            ptMin = cms.double( ptVal ),
                            originRadius = cms.double( 0.05 ),
                            precise = cms.bool( True ),
                            useMultipleScattering = cms.bool( False )
                          )
                        )
        )
          
  process.hltIter2PFlowPixelHitDoublets.trackingRegions = 'hltIter2PFlowPixelTrackingRegionsGlobalPtSeed'+ptStr

  process.HLTIterativeTrackingIteration2.replace(
    process.hltIter2PFlowPixelTrackingRegions,
    getattr(process,"hltIter2PFlowPixelTrackingRegionsGlobalPtSeed"+ptStr)
  )

  return process


def customize_HLT_trkIter2GlobalPtSeedXXForBTag(process,ptVal=0.9):

  ptStr = str(ptVal).replace(".","p")
  
  setattr(process,"hltIter2PFlowPixelTrackingRegionsGlobalPtSeed"+ptStr+"ForBTag",
          cms.EDProducer( 'GlobalTrackingRegionWithVerticesEDProducer',
                          RegionPSet = cms.PSet( 
                            useFixedError = cms.bool( True ),
                            nSigmaZ = cms.double( 0.0 ),
                            VertexCollection = cms.InputTag( 'hltFastPVPixelVertices' ),
                            beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
                            useFoundVertices = cms.bool( True ),
                            fixedError = cms.double( 0.2 ),
                            sigmaZVertex = cms.double( 3.0 ),
                            useFakeVertices = cms.bool( False ),
                            ptMin = cms.double( ptVal ),
                            originRadius = cms.double( 0.3 ),
                            precise = cms.bool( True ),
                            useMultipleScattering = cms.bool( False )
                          )
                        )
        )

  process.hltIter2PFlowPixelHitDoubletsForBTag.trackingRegions = 'hltIter2PFlowPixelTrackingRegionsGlobalPtSeed'+ptStr+'ForBTag'

  process.HLTIterativeTrackingIteration2ForBTag.replace(
    process.hltIter2PFlowPixelTrackingRegionsForBTag,
    getattr(process,"hltIter2PFlowPixelTrackingRegionsGlobalPtSeed"+ptStr+"ForBTag")
  )

  return process


def customize_HLTDeepCSVPF(process,ptVal=0.9):

  ptStr = str(ptVal).replace(".","p")

  setattr(process,"hltDeepBLifetimeTagInfosPFPtCut"+ptStr,
          cms.EDProducer("CandIPProducer",
                         candidates = cms.InputTag("hltParticleFlow"),
                         computeGhostTrack = cms.bool(True),
                         computeProbabilities = cms.bool(True),
                         ghostTrackPriorDeltaR = cms.double(0.03),
                         jetDirectionUsingGhostTrack = cms.bool(False),
                         jetDirectionUsingTracks = cms.bool(False),
                         jets = cms.InputTag("hltPFJetForBtag"),
                         maxDeltaR = cms.double(0.4),
                         maximumChiSquared = cms.double(5.0),
                         maximumLongitudinalImpactParameter = cms.double(17.0),
                         maximumTransverseImpactParameter = cms.double(0.2),
                         minimumNumberOfHits = cms.int32(3),
                         minimumNumberOfPixelHits = cms.int32(2),
                         minimumTransverseMomentum = cms.double(ptVal),
                         primaryVertex = cms.InputTag("hltVerticesPFFilter"),
                         useTrackQuality = cms.bool(False)
                       )
        )

  process.hltDeepSecondaryVertexTagInfosPF.trackIPTagInfos = "hltDeepBLifetimeTagInfosPFPtCut"+ptStr 

  process.HLTBtagDeepCSVSequencePF.replace(
    process.hltDeepBLifetimeTagInfosPF,
    getattr(process,"hltDeepBLifetimeTagInfosPFPtCut"+ptStr)
  )


  setattr(process,"hltDeepInclusiveVertexFinderPFPtCut"+ptStr,    
          cms.EDProducer("InclusiveCandidateVertexFinder",
                         beamSpot = cms.InputTag("hltOnlineBeamSpot"),
                         clusterizer = cms.PSet(
                           clusterMaxDistance = cms.double(0.05),
                           clusterMaxSignificance = cms.double(4.5),
                           clusterMinAngleCosine = cms.double(0.5),
                           distanceRatio = cms.double(20.0),
                           seedMax3DIPSignificance = cms.double(9999.0),
                           seedMax3DIPValue = cms.double(9999.0),
                           seedMin3DIPSignificance = cms.double(1.2),
                           seedMin3DIPValue = cms.double(0.005)
                         ),
                         fitterRatio = cms.double(0.25),
                         fitterSigmacut = cms.double(3.0),
                         fitterTini = cms.double(256.0),
                         maxNTracks = cms.uint32(30),
                         maximumLongitudinalImpactParameter = cms.double(0.3),
                         maximumTimeSignificance = cms.double(3.0),
                         minHits = cms.uint32(8),
                         minPt = cms.double( ptVal ),
                         primaryVertices = cms.InputTag("hltVerticesPFFilter"),
                         tracks = cms.InputTag("hltParticleFlow"),
                         useDirectVertexFitter = cms.bool(True),
                         useVertexReco = cms.bool(True),
                         vertexMinAngleCosine = cms.double(0.95),
                         vertexMinDLen2DSig = cms.double(2.5),
                         vertexMinDLenSig = cms.double(0.5),
                         vertexReco = cms.PSet(
                           finder = cms.string('avr'),
                           primcut = cms.double(1.0),
                           seccut = cms.double(3.0),
                           smoothing = cms.bool(True)
                         )
                       )
  )

  process.hltDeepInclusiveSecondaryVerticesPF.secondaryVertices = "hltDeepInclusiveVertexFinderPFPtCut"+ptStr

  process.HLTBtagDeepCSVSequencePF.replace(
    process.hltDeepInclusiveVertexFinderPF,
    getattr(process,"hltDeepInclusiveVertexFinderPFPtCut"+ptStr)
  )


  return process

#Hello world!
def customize_CaloJet(process,ptVal=0.9):

  ptStr = str(ptVal).replace(".","p")

  setattr(process, "hltImpactParameterTagInfosPtCut" + ptStr,
          cms.EDProducer("TrackIPProducer", 
                computeGhostTrack = cms.bool(True),
                computeProbabilities = cms.bool(True),
                ghostTrackPriorDeltaR = cms.double(0.03),
                jetDirectionUsingGhostTrack = cms.bool(False),
                jetDirectionUsingTracks = cms.bool(False),
                jetTracks = cms.InputTag("hltFastPixelBLifetimeL3Associator"), 
                maximumChiSquared = cms.double(5.0),
                maximumLongitudinalImpactParameter = cms.double(17.0),
                maximumTransverseImpactParameter = cms.double(0.2),
                minimumNumberOfHits = cms.int32(3), 
                minimumNumberOfPixelHits = cms.int32(2),
                minimumTransverseMomentum = cms.double(ptVal),    
                primaryVertex = cms.InputTag("hltVerticesL3","WithBS"), 
                useTrackQuality = cms.bool(False)
          )
  )
    
  process.hltInclusiveSecondaryVertexFinderTagInfos.trackIPTagInfos = "hltImpactParameterTagInfosPtCut" + ptStr 

  process.HLTBtagDeepCSVSequenceL3.replace(
    process.hltImpactParameterTagInfos,
    getattr(process, "hltImpactParameterTagInfosPtCut" + ptStr)
    )

  setattr(process, "hltInclusiveVertexFinderPtCut" + ptStr,
          cms.EDProducer("InclusiveVertexFinder",
                         beamSpot = cms.InputTag("hltOnlineBeamSpot"),
                         clusterizer = cms.PSet(
                                        clusterMaxDistance = cms.double(0.05),
                                        clusterMaxSignificance = cms.double(4.5),
                                        clusterMinAngleCosine = cms.double(0.5),
                                        distanceRatio = cms.double(20.0),
                                        seedMax3DIPSignificance = cms.double(9999.0),
                                        seedMax3DIPValue = cms.double(9999.0),
                                        seedMin3DIPSignificance = cms.double(1.2),
                                        seedMin3DIPValue = cms.double(0.005)
                                        ),
                         fitterRatio = cms.double(0.25),
                         fitterSigmacut = cms.double(3.0),
                         fitterTini = cms.double(256.0),
                         maxNTracks = cms.uint32(30),
                         maximumLongitudinalImpactParameter = cms.double(0.3),
                         maximumTimeSignificance = cms.double(3.0),
                         minHits = cms.uint32(8),
                         minPt = cms.double(ptVal), #original 0.8
                         primaryVertices = cms.InputTag("hltVerticesL3"),
                         tracks = cms.InputTag("hltMergedTracksForBTag"),
                         useDirectVertexFitter = cms.bool(True),
                         useVertexReco = cms.bool(True),
                         vertexMinAngleCosine = cms.double(0.95),
                         vertexMinDLen2DSig = cms.double(2.5),
                         vertexMinDLenSig = cms.double(0.5),
                         vertexReco = cms.PSet(
                             finder = cms.string('avr'),
                             primcut = cms.double(1.0),
                             seccut = cms.double(3.0),
                             smoothing = cms.bool(True)
                         )
          )
  )

  process.hltInclusiveSecondaryVertices.secondaryVertices = "hltInclusiveVertexFinderPtCut" + ptStr

  process.HLTBtagDeepCSVSequenceL3.replace(
    process.hltInclusiveVertexFinder,
    getattr(process,"hltInclusiveVertexFinderPtCut"+ptStr)
  )
   

  return process


                                                                                                    
