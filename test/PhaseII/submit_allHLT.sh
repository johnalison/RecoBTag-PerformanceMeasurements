#!/bin/bash

echo "!!!! WARNING: Submitting for MC!!!"
# ==========================cutsv2===================
python submit_allHLT.py \
  runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv00 BTVreco=cutsV2 \
  -v crab_projects_SeptemberL1_TrackingV0_cutsV2_v3 \
  -t 2750 \
  -m 4500

python submit_allHLT.py \
  runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv06_TICL BTVreco=cutsV2 \
  -v crab_projects_SeptemberL1_TrackingV6_TICL_cutsV2_v3 \
  -t 2750 \
  -m 4500

python submit_allHLT.py \
  runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv06p1_TICL BTVreco=cutsV2 \
  -v crab_projects_SeptemberL1_TrackingV6p1_TICL_cutsV2_v3 \
  -t 2750 \
  -m 4500

python submit_allHLT.py \
  runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv07p2_TICL BTVreco=cutsV2 \
  -v crab_projects_SeptemberL1_TrackingV7p2_TICL_cutsV2_v3 \
  -t 2750 \
  -m 4500
  # ==========================cutsv1===================
python submit_allHLT.py \
  runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv00 BTVreco=cutsV1 \
  -v crab_projects_SeptemberL1_TrackingV0_cutsV1_v3 \
  -t 2750 \
  -m 4500

python submit_allHLT.py \
  runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv06_TICL BTVreco=cutsV1 \
  -v crab_projects_SeptemberL1_TrackingV6_TICL_cutsV1_v3 \
  -t 2750 \
  -m 4500

python submit_allHLT.py \
  runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv06p1_TICL BTVreco=cutsV1 \
  -v crab_projects_SeptemberL1_TrackingV6p1_TICL_cutsV1_v3 \
  -t 2750 \
  -m 4500

python submit_allHLT.py \
    runHLTBTagAnalyzer_PhaseII_cfg.py \
    -f CRAB/tosubmit.txt \
    -s T2_DE_DESY \
    -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
    -p reco=HLT_TRKv07p2_TICL BTVreco=cutsV1 \
    -v crab_projects_SeptemberL1_TrackingV7p2_TICL_cutsV1_v3 \
    -t 2750 \
    -m 4500
# ==========================default===================
python submit_allHLT.py \
  runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv00 BTVreco=default \
  -v crab_projects_SeptemberL1_TrackingV0_default_v3 \
  -t 2750 \
  -m 4500

python submit_allHLT.py \
  runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv06_TICL BTVreco=default \
  -v crab_projects_SeptemberL1_TrackingV6_TICL_default_v3 \
  -t 2750 \
  -m 4500

python submit_allHLT.py \
  runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv06p1_TICL BTVreco=default \
  -v crab_projects_SeptemberL1_TrackingV6p1_TICL_default_v3 \
  -t 2750 \
  -m 4500

python submit_allHLT.py \
  runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv07p2_TICL BTVreco=default \
  -v crab_projects_SeptemberL1_TrackingV7p2_TICL_default_v3 \
  -t 2750 \
  -m 4500
