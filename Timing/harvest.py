import FWCore.ParameterSet.Config as cms

process = cms.Process('HARVESTING')

# read all the DQMIO files produced by the previous jobs
process.source = cms.Source("DQMRootSource",
    fileNames = cms.untracked.vstring(
        # "file:DQMIO.root"
        # "file:/afs/cern.ch/work/s/sewuchte/private/BTag_Upgrade/August_11_1_2/CMSSW_11_1_2/src/Timing/HLT_TRKv06_TICL/DQM_NoPU.root"
        # "file:/afs/cern.ch/work/s/sewuchte/private/BTag_Upgrade/August_11_1_2/CMSSW_11_1_2/src/Timing/HLT_TRKv06_TICL/PU200/DQM.root"
        # "file:/afs/cern.ch/work/s/sewuchte/private/BTag_Upgrade/August_11_1_2/CMSSW_11_1_2/src/Timing/HLT_TRKv06_TICL_skimmedTracks/NoPU/DQM.root"
        "file:/afs/cern.ch/work/s/sewuchte/private/BTag_Upgrade/August_11_1_2/CMSSW_11_1_2/src/Timing/HLT_TRKv00/PU200/DQM.root"
        # "file:/afs/cern.ch/work/s/sewuchte/private/BTag_Upgrade/August_11_1_2/CMSSW_11_1_2/src/Timing/DQM.root"
        )
)

# DQMStore service
process.load('DQMServices.Core.DQMStore_cfi')

# FastTimerService client
process.load('HLTrigger.Timer.fastTimerServiceClient_cfi')
process.fastTimerServiceClient.dqmPath = "HLT/TimerService"

process.load("HLTrigger.Timer.FastTimerService_cfi") #ms
process.FastTimerService.dqmTimeRange            = 20000.
process.FastTimerService.dqmTimeResolution       =    10.
process.FastTimerService.dqmPathTimeRange        = 10000.
process.FastTimerService.dqmPathTimeResolution   =     5.
process.FastTimerService.dqmModuleTimeRange      =  1000.
process.FastTimerService.dqmModuleTimeResolution =     1.

# DQM file saver
process.load('DQMServices.Components.DQMFileSaver_cfi')
process.dqmSaver.workflow = "/HLT/FastTimerService/All"

process.DQMFileSaverOutput = cms.EndPath( process.fastTimerServiceClient + process.dqmSaver )
