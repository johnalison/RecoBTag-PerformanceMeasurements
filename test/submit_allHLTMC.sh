#!/bin/bash

cmsenv
#voms-proxy-init -rfc -voms cms -valid 192:00
source /cvmfs/cms.cern.ch/crab3/crab.sh

echo "!!!! WARNING: Submitting for MC!!!"
python submit_allHLT.py \
  runHLTBTagAnalyzer_cfg.py \
  -f CRAB/tosubmit_MC.txt \
  -s T3_US_FNALLPC \
  -p groups="HLTEventInfo,HLTJetInfo,HLTTagVar,HLTJetTrack,HLTJetSV,HLTCSVTagVar" runOnData=False globalTag="110X_mcRun3_2021_realistic_v6" trackPtSeed=0.4 trigNames="HLT_ZeroBias_Beamspot_v*"\
  -o /store/user/wterrill/BTagNTuples/Run3/ \
  -v crab_projects_run3_trackPt0p4_trigChange

#echo "!!!! WARNING: Submitting for MC!!!"
#python submit_allHLT.py \
#  runHLTBTagAnalyzer_cfg.py \
#  -f CRAB/tosubmit_MC.txt \
#  -s T3_US_FNALLPC \
#  -p groups="HLTEventInfo,HLTJetInfo,HLTTagVar,HLTJetTrack,HLTJetSV,HLTCSVTagVar" runOnData=False globalTag="110X_mcRun3_2021_realistic_v6" trackPtSeed=0.9 trigNames="HLT_ZeroBias_Beamspot_v*"\
#  -o /store/user/wterrill/BTagNTuples/Run3/ \
#  -v crab_projects_run3_trackPt0p9_trigChange
#
#echo "!!!! WARNING: Submitting for MC!!!"
#python submit_allHLT.py \
#  runHLTBTagAnalyzer_cfg.py \
#  -f CRAB/tosubmit_MC.txt \
#  -s T3_US_FNALLPC \
#  -p groups="HLTEventInfo,HLTJetInfo,HLTTagVar,HLTJetTrack,HLTJetSV,HLTCSVTagVar" runOnData=False globalTag="110X_mcRun3_2021_realistic_v6" trackPtSeed=1.5 trigNames="HLT_ZeroBias_Beamspot_v*"\
#  -o /store/user/wterrill/BTagNTuples/Run3/ \
#  -v crab_projects_run3_trackPt1p5_trigChange
#
#echo "!!!! WARNING: Submitting for MC!!!"
#python submit_allHLT.py \
#  runHLTBTagAnalyzer_cfg.py \
#  -f CRAB/tosubmit_MC.txt \
#  -s T3_US_FNALLPC \
#  -p groups="HLTEventInfo,HLTJetInfo,HLTTagVar,HLTJetTrack,HLTJetSV,HLTCSVTagVar" runOnData=False globalTag="110X_mcRun3_2021_realistic_v6" trackPtSeed=2.0 trigNames="HLT_ZeroBias_Beamspot_v*"\
#  -o /store/user/wterrill/BTagNTuples/Run3/ \
#  -v crab_projects_run3_trackPt2p0_trigChange
#
#echo "!!!! WARNING: Submitting for MC!!!"
#python submit_allHLT.py \
#  runHLTBTagAnalyzer_cfg.py \
#  -f CRAB/tosubmit_MC.txt \
#  -s T3_US_FNALLPC \
#  -p groups="HLTEventInfo,HLTJetInfo,HLTTagVar,HLTJetTrack,HLTJetSV,HLTCSVTagVar" runOnData=False globalTag="110X_mcRun3_2021_realistic_v6" trackPtSeed=2.5 trigNames="HLT_ZeroBias_Beamspot_v*"\
#  -o /store/user/wterrill/BTagNTuples/Run3/ \
#  -v crab_projects_run3_trackPt2p5_trigChange
#
#echo "!!!! WARNING: Submitting for MC!!!"
#python submit_allHLT.py \
#  runHLTBTagAnalyzer_cfg.py \
#  -f CRAB/tosubmit_MC.txt \
#  -s T3_US_FNALLPC \
#  -p groups="HLTEventInfo,HLTJetInfo,HLTTagVar,HLTJetTrack,HLTJetSV,HLTCSVTagVar" runOnData=False globalTag="110X_mcRun3_2021_realistic_v6" trackPtSeed=5.0 trigNames="HLT_ZeroBias_Beamspot_v*"\
#  -o /store/user/wterrill/BTagNTuples/Run3/ \
#  -v crab_projects_run3_trackPt5p0_trigChange
#
#echo "!!!! WARNING: Submitting for MC!!!"
#python submit_allHLT.py \
#  runHLTBTagAnalyzer_cfg.py \
#  -f CRAB/tosubmit_MC.txt \
#  -s T3_US_FNALLPC \
#  -p groups="HLTEventInfo,HLTJetInfo,HLTTagVar,HLTJetTrack,HLTJetSV,HLTCSVTagVar" runOnData=False globalTag="110X_mcRun3_2021_realistic_v6" trackPtSeed=7.5 trigNames="HLT_ZeroBias_Beamspot_v*"\
#  -o /store/user/wterrill/BTagNTuples/Run3/ \
#  -v crab_projects_run3_trackPt7p5_trigChange
#
#echo "!!!! WARNING: Submitting for MC!!!"
#python submit_allHLT.py \
#  runHLTBTagAnalyzer_cfg.py \
#  -f CRAB/tosubmit_MC.txt \
#  -s T3_US_FNALLPC \
#  -p groups="HLTEventInfo,HLTJetInfo,HLTTagVar,HLTJetTrack,HLTJetSV,HLTCSVTagVar" runOnData=False globalTag="110X_mcRun3_2021_realistic_v6" trackPtSeed=10.0 trigNames="HLT_ZeroBias_Beamspot_v*"\
#  -o /store/user/wterrill/BTagNTuples/Run3/ \
#  -v crab_projects_run3_trackPt10p0_trigChange
#
#echo "!!!! WARNING: Submitting for MC!!!"
#python submit_allHLT.py \
#  runHLTBTagAnalyzer_cfg.py \
#  -f CRAB/tosubmit_MC.txt \
#  -s T3_US_FNALLPC \
#  -p groups="HLTEventInfo,HLTJetInfo,HLTTagVar,HLTJetTrack,HLTJetSV,HLTCSVTagVar" runOnData=False globalTag="110X_mcRun3_2021_realistic_v6" trackPtSeed=20.0 trigNames="HLT_ZeroBias_Beamspot_v*"\
#  -o /store/user/wterrill/BTagNTuples/Run3/ \
#  -v crab_projects_run3_trackPt20p0_trigChange
#
