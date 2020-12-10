# RecoBTag-PerformanceMeasurements

## Software setup for CMSSW_11_1_4
* **Step #1** : create local CMSSW area and add the relevant packages.
```
scramv1 project CMSSW CMSSW_11_1_3_Patatrack
cd CMSSW_11_1_3_Patatrack/src
eval `scramv1 runtime -sh`

git cms-init

# L1T
git cms-merge-topic cms-l1t-offline:l1t-phase2-v3.1.9

# HLT: interface for L1T seeds
git cms-merge-topic trtomei:Phase2-L1T-HLT-Interface

# TRK
git cms-merge-topic AdrianoDee:patatrack_hlt_phase2

# HGCal
git cms-merge-topic rovere:TICLv2_11_1_X
cp -r ${CMSSW_DATA_PATH}/data-RecoHGCal-TICL/V00-01-00/RecoHGCal/TICL/data/ ${CMSSW_BASE}/src/RecoHGCal/TICL
wget https://github.com/rovere/RecoHGCal-TICL/raw/9d2c6f72c86233fa5573e93d5535b32e90c835ee/tf_models/energy_id_v0.pb -O ${CMSSW_BASE}/src/RecoHGCal/TICL/data/tf_models/energy_id_v0.pb

# JME: updates to Puppi (required only for TRK-vX, with X>=7.2)
git cms-merge-topic missirol:devel_hltPhase2_puppi_usePUProxyValue_1114

# fix for GenFilters
git cms-merge-topic Sam-Harper:MCStartFilterInputCollFix_1110pre6

git cms-addpkg RecoBTag
git cms-addpkg RecoBTag/TensorFlow
git cms-addpkg RecoBTag/Combined

git cms-merge-topic emilbols:BTV_CMSSW_11_1_X

# workaround for PFSimParticle::trackerSurfaceMomentum
# ref: hatakeyamak:FBaseSimEvent_ProtectAgainstMissingTrackerSurfaceMomentum
git cms-addpkg FastSimulation/Event
git remote add hatakeyamak https://github.com/hatakeyamak/cmssw.git
git fetch hatakeyamak
git diff 0cf67551731c80dc85130e4b8ec73c8f44d53cb0^ 0cf67551731c80dc85130e4b8ec73c8f44d53cb0 | git apply

# selected manual backport of BadPFMuonDz MET-filter
# https://github.com/cms-sw/cmssw/pull/30015
git cms-addpkg RecoMET/METFilters
git diff 442ae0775276f4388f8d51742ea915c1b91e1506 bb38311862c83068b2434f35850c9a17e29dd2f7 RecoMET/METFilters/python | git apply
git checkout bb38311862c83068b2434f35850c9a17e29dd2f7 RecoMET/METFilters/plugins/BadParticleFilter.cc

# analyzer for primary vertices (courtesy of W. Erdmann)
git clone https://github.com/missirol/PVAnalysis.git usercode -o missirol -b phase2

# MinBias/QCD Stitching
mkdir -p HLTrigger
git clone https://github.com/veelken/mcStitching.git HLTrigger/mcStitching

# basic JME setup including customizers
git clone https://github.com/missirol/JMETriggerAnalysis.git -o missirol -b phase2

# BTV setup
git clone -b PhaseIIOnline --depth 1 https://github.com/johnalison/RecoBTag-PerformanceMeasurements.git RecoBTag/PerformanceMeasurements

# Get the latest training files. not pretty, but works:
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
