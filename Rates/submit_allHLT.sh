#!/bin/bash

echo "!!!! WARNING: Submitting for MC!!!"
python submit_allHLT.py \
  ../python/Configs/testTriggerPaths_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Rates/ \
  -p reco=HLT_TRKv06p1 BTVreco=cutsV2 \
  -v crab_projects_Rates_Workshop_TRKv06p1_cutsV2_v2 \
  -t 2750 \
  -m 4500

python submit_allHLT.py \
  ../python/Configs/testTriggerPaths_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Rates/ \
  -p reco=HLT_TRKv07p2 BTVreco=cutsV2 \
  -v crab_projects_Rates_Workshop_TRKv07p2_cutsV2_v2 \
  -t 2750 \
  -m 4500

python submit_allHLT.py \
  ../python/Configs/testTriggerPaths_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Rates/ \
  -p reco=HLT_TRKv06p1_TICL BTVreco=cutsV2 \
  -v crab_projects_Rates_Workshop_TRKv06p1_TICL_cutsV2_v2 \
  -t 2750 \
  -m 4500

python submit_allHLT.py \
  ../python/Configs/testTriggerPaths_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Rates/ \
  -p reco=HLT_TRKv07p2_TICL BTVreco=cutsV2 \
  -v crab_projects_Rates_Workshop_TRKv07p2_TICL_cutsV2_v2 \
  -t 2750 \
  -m 4500
