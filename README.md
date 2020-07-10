# RecoBTag-PerformanceMeasurements

## Software setup for CMSSW_11_1_0_pre6
* **Step #1** : create local CMSSW area and add the relevant packages.
```
cmsrel CMSSW_11_1_0_pre6
cd CMSSW_11_1_0_pre6/src
cmsenv

git cms-init

# [HGCal] fix to PID+EnergyRegression in TICL
git cms-merge-topic cms-sw:29799

# temporary workaround for PFSimParticle::trackerSurfaceMomentum
# ref: hatakeyamak:FBaseSimEvent_ProtectAgainstMissingTrackerSurfaceMomentum
git cms-addpkg FastSimulation/Event
git remote add hatakeyamak https://github.com/hatakeyamak/cmssw.git
git fetch hatakeyamak
git cherry-pick 0cf67551731c80dc85130e4b8ec73c8f44d53cb0

# [L1T]
git cms-merge-topic -u cms-L1TK:L1TK-integration-CMSSW_11_1_0_pre4
git cms-merge-topic -u cms-l1t-offline:l1t-phase2-v3.0.2

git cms-addpkg RecoBTag
git cms-addpkg RecoBTag/TensorFlow
git cms-addpkg RecoBTag/Combined

git clone -b PrunedTraining_NoPuppi https://github.com/emilbols/RecoBTag-Combined RecoBTag/Combined/data
wget https://raw.githubusercontent.com/cms-data/RecoBTag-Combined/master/DeepCSV_PhaseII.json -P RecoBTag/Combined/data/
git clone -b PhaseIIOnline --depth 1 https://github.com/johnalison/RecoBTag-PerformanceMeasurements.git RecoBTag/PerformanceMeasurements

git clone https://github.com/missirol/JMETriggerAnalysis.git -o missirol -b phase2

scram b -j8

```


* **Step #2a** : generate customized configuration file to run TRK(v00/v02/v06)+PF+JME(incl TICL?)+BTV HLT-like reconstruction on RAW.
Already done in `RecoBTag/PerformanceMeasurements/python/hltPhase2_TRKv*_cfg`
For example with TrackingV6 and TICL:
```
cmsDriver.py step3 \
  --geometry Extended2026D49 --era Phase2C9 \
  --conditions auto:phase2_realistic_T15 \
  --processName RECO2 \
  --step RAW2DIGI,RECO \
  --eventcontent RECO \
  --datatier RECO \
  --filein /store/mc/Phase2HLTTDRWinter20DIGI/QCD_Pt-15to3000_TuneCP5_Flat_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_castor_110X_mcRun4_realistic_v3-v2/10000/05BFAD3E-3F91-1843-ABA2-2040324C7567.root \
  --mc \
  --nThreads 4 \
  --nStreams 4 \
  --python_filename hltPhase2_TRKv06_cfg.py \
  --no_exec \
  -n 10 \
  --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring \
  --customise JMETriggerAnalysis/Common/hltPhase2_TRKv06.customize_hltPhase2_TRKv06 \
  --customise JMETriggerAnalysis/Common/hltPhase2_JME.customize_hltPhase2_JME \
  --customise JMETriggerAnalysis/Common/hltPhase2_JME.customize_hltPhase2_TICL \
  --customise RecoBTag/PerformanceMeasurements/hltPhase2_BTV.customize_hltPhase2_BTV \
  --customise_commands 'process.schedule.remove(process.RECOoutput_step)\ndel process.RECOoutput\ndel process.RECOoutput_step\n'
```

* **Step #3** : Run `cmsRun` with bTagHLTAnalyzer in `/test/python/PhaseII/runHLTBTagAnalyzer_PhaseII_cfg.py`
