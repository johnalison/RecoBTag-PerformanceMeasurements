import FWCore.ParameterSet.Config as cms
from RecoBTag.PerformanceMeasurements.bTagAnalyzerCommon_cff import *
from RecoBTag.PerformanceMeasurements.variables_cfi import *
from RecoBTag.PerformanceMeasurements.varGroups_cfi import *

def bTagAnalyzer_func(trigPaths=[]):
    bTagHLTAnalyzer = cms.EDAnalyzer("BTagHLTAnalyzer",
                                     bTagAnalyzerCommon,
                                     variableSet,
                                     groupSet,
                                     HLTprimaryVertexColl = cms.InputTag('hltVerticesPFFilter'),
                                     CaloJets             = cms.InputTag('hltAK4CaloJetsCorrectedIDPassed'),
                                     CaloJetTags          = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsInfosCalo'),
                                     CaloSVs              = cms.InputTag('hltInclusiveSecondaryVertexFinderTagInfos'),
                                     CaloJetCSVTags       = cms.InputTag('hltCombinedSecondaryVertexBJetTagsCalo'),
                                     CaloJetDeepCSVTags   = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsCalo:probb'),
                                     PFJets               = cms.InputTag('hltAK4PFJetsLooseIDCorrected'),
                                     PFJetTags            = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsInfos'),
                                     PFSVs                = cms.InputTag('hltDeepSecondaryVertexTagInfosPF'),
                                     PFJetCSVTags         = cms.InputTag('hltCombinedSecondaryVertexBJetTagsPF'),
                                     PFJetDeepCSVTags     = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsPF:probb'),
                                     HLTTriggerPathNames  = cms.vstring(trigPaths),
    )
    print(trigPaths)

    return bTagHLTAnalyzer
