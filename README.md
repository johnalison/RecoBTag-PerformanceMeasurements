# RecoBTag-PerformanceMeasurements

## Software setup for CMSSW_11_1_2
* **Step #1** : create local CMSSW area and add the relevant packages.
```
cmsrel CMSSW_11_1_2_patch3
cd CMSSW_11_1_2_patch3/src
cmsenv

git cms-init

# [temporarily comment out fix for PF-Hadron calibrations]
# # workaround for PFSimParticle::trackerSurfaceMomentum
# # ref: hatakeyamak:FBaseSimEvent_ProtectAgainstMissingTrackerSurfaceMomentum
# git cms-addpkg FastSimulation/Event
# git remote add hatakeyamak https://github.com/hatakeyamak/cmssw.git
# git fetch hatakeyamak
# git cherry-pick 0cf67551731c80dc85130e4b8ec73c8f44d53cb0

# For running custom L1 Filters
git cms-addpkg DataFormats/HLTReco
git cms-addpkg HLTrigger/HLTcore
git cms-addpkg HLTrigger/HLTfilters
git remote add missirol https://github.com/missirol/cmssw.git
git fetch missirol

git cherry-pick 892eac81715c88d13c465ffc08e5d86c6ca87a7e
git cherry-pick 66d114ff75480e72e59dec1101ff4bb51e623523

git cms-addpkg RecoBTag
git cms-addpkg RecoBTag/TensorFlow
git cms-addpkg RecoBTag/Combined

git clone -b PrunedTraining_NoPuppi https://github.com/emilbols/RecoBTag-Combined RecoBTag/Combined/data
wget https://raw.githubusercontent.com/cms-data/RecoBTag-Combined/master/DeepCSV_PhaseII.json -P RecoBTag/Combined/data/
git clone -b PhaseIIOnline --depth 1 https://github.com/johnalison/RecoBTag-PerformanceMeasurements.git RecoBTag/PerformanceMeasurements

git clone https://github.com/missirol/JMETriggerAnalysis.git -o missirol -b phase2_devel_l1tSeed

scram b -j8

```



* **Step #2** : Run `cmsRun` with bTagHLTAnalyzer in `/test/python/PhaseII/runHLTBTagAnalyzer_PhaseII_cfg.py`


#obsolete
* **Creating configuration files** : generate customized configuration file to run TRK(v00/v02/v06)+PF+JME(incl TICL?)+BTV HLT-like reconstruction on RAW.
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
