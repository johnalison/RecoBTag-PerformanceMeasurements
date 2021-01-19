# RecoBTag-PerformanceMeasurements

## Software setup for CMSSW_11_1_6
* **Step #1** : create local CMSSW area and add the relevant packages.
```
scramv1 project CMSSW scramv1 project CMSSW CMSSW_11_1_6
cd scramv1 project CMSSW CMSSW_11_1_6/src
eval `scramv1 runtime -sh`

git cms-init

# L1T + JME (cms-sw#31607 by L1T accidentaly includes cms-sw#32434 by JME)
git cms-merge-topic cms-sw:31607

# HLT
git cms-merge-topic cms-sw:32474

# HGCal
git cms-merge-topic cms-sw:32527
cp -r ${CMSSW_DATA_PATH}/data-RecoHGCal-TICL/V00-01-00/RecoHGCal/TICL/data/ ${CMSSW_BASE}/src/RecoHGCal/TICL
wget https://github.com/rovere/RecoHGCal-TICL/raw/9d2c6f72c86233fa5573e93d5535b32e90c835ee/tf_models/energy_id_v0.pb -O ${CMSSW_BASE}/src/RecoHGCal/TICL/data/tf_models/energy_id_v0.pb

# fix for GenFilters
git cms-merge-topic Sam-Harper:MCStartFilterInputCollFix_1110pre6

git cms-addpkg RecoBTag
git cms-addpkg RecoBTag/TensorFlow
git cms-addpkg RecoBTag/Combined

git cms-merge-topic emilbols:BTV_CMSSW_11_1_X

# [optional; required only for PF-Hadron calibrations]
# workaround for PFSimParticle::trackerSurfaceMomentum
# ref: hatakeyamak:FBaseSimEvent_ProtectAgainstMissingTrackerSurfaceMomentum
git cms-addpkg FastSimulation/Event
git remote add hatakeyamak https://github.com/hatakeyamak/cmssw.git
git fetch hatakeyamak
git diff 0cf67551731c80dc85130e4b8ec73c8f44d53cb0^ 0cf67551731c80dc85130e4b8ec73c8f44d53cb0 | git apply

[optional; required only for  NTuple workflow with 'pvdqm > 1']
# analyzer for primary vertices (courtesy of W. Erdmann)
git clone https://github.com/missirol/PVAnalysis.git usercode -o missirol -b phase2

# [optional; MinBias/QCD Stitching required only for NTuples]
mkdir -p HLTrigger
git clone https://github.com/veelken/mcStitching.git HLTrigger/mcStitching

# basic JME setup including customizers
git clone https://github.com/missirol/JMETriggerAnalysis.git -o missirol -b phase2

# BTV setup
git clone -b PhaseIIOnline --depth 1 https://github.com/johnalison/RecoBTag-PerformanceMeasurements.git RecoBTag/PerformanceMeasurements

# Get the latest DeepCSV and DeepJet training files. not pretty, but works:
cd RecoBTag/Combined/data/DeepFlavour_Phase2/
wget -O DeepJet_pv3d_nt.onnx https://github.com/mneukum/cmssw/blob/BTV_CMSSW_11_1_2_with_timing/RecoBTag/Combined/data/DeepFlavour_Phase2/DeepJet_pv3d_nt.onnx?raw=true
mv model.onnx model.onnx.ori
mv DeepJet_pv3d_nt.onnx model.onnx
cd ..
wget -O DeepCSV_pv3d_nt.onnx https://raw.githubusercontent.com/mneukum/cmssw/BTV_CMSSW_11_1_2_with_timing/RecoBTag/Combined/data/DeepCSV_Phase2_pv3d_no_timing.json
mv DeepCSV_PhaseII.json DeepCSV_PhaseII.json.ori
mv DeepCSV_pv3d_nt.onnx DeepCSV_PhaseII.json

cd ../../..

# It is possible that you have to try to compile twice because of the TRK merge topic.
scram b -j10

```



* **Step #2** : Run `cmsRun` with bTagHLTAnalyzer in `/test/python/PhaseII/runHLTBTagAnalyzer_PhaseII_cfg.py`
e.g.:
`cmsRun runHLTBTagAnalyzer_PhaseII_cfg.py maxEvents=5 reco=HLT_TRKv06p1_TICL BTVreco=cutsV2`
