# RecoBTag-PerformanceMeasurements

## Software setup for CMSSW_11_1_2_patch3/CMSSW_11_1_2
* **Step #1** : create local CMSSW area and add the relevant packages.
```
cmsrel CMSSW_11_1_2_patch3
cd CMSSW_11_1_2_patch3/src
cmsenv

git cms-init

# [optional; required only for PF-Hadron calibrations]
# workaround for PFSimParticle::trackerSurfaceMomentum
# ref: hatakeyamak:FBaseSimEvent_ProtectAgainstMissingTrackerSurfaceMomentum
git cms-addpkg FastSimulation/Event
git remote add hatakeyamak https://github.com/hatakeyamak/cmssw.git
git fetch hatakeyamak
git diff 0cf67551731c80dc85130e4b8ec73c8f44d53cb0^ 0cf67551731c80dc85130e4b8ec73c8f44d53cb0 | git apply

# updates to use l1t::PFJet with HLT plugins
git cms-addpkg DataFormats/HLTReco
git cms-addpkg DataFormats/L1TParticleFlow
git cms-addpkg HLTrigger/HLTcore
git cms-addpkg HLTrigger/HLTfilters
git cms-addpkg HLTrigger/JetMET
git remote add SWuchterl https://github.com/SWuchterl/cmssw.git
git fetch SWuchterl

git cherry-pick 5747777c3a8d88ac190bf52a00a941654de6d14c
git cherry-pick d6cde53061f932f81f0b97605e60defabdc25860
git cherry-pick 979fc95a010ee06a597a757d95b50092490dc798


# updates to Puppi (required only for TRK-vX, with X>=7.2)
git cms-merge-topic missirol:devel_hltPhase2_puppi_usePUProxyValue_1112pa3 -u

#For BTV:

git cms-addpkg RecoBTag
git cms-addpkg RecoBTag/TensorFlow
git cms-addpkg RecoBTag/Combined

git cms-merge-topic emilbols:BTV_CMSSW_11_1_X -u
git clone -b PhaseIIOnline --depth 1 https://github.com/johnalison/RecoBTag-PerformanceMeasurements.git RecoBTag/PerformanceMeasurements

#For basic JME objects/PF etc
git clone https://github.com/missirol/JMETriggerAnalysis.git -o missirol -b phase2

scram b -j8

```



* **Step #2** : Run `cmsRun` with bTagHLTAnalyzer in `/test/python/PhaseII/runHLTBTagAnalyzer_PhaseII_cfg.py`
