#!/bin/bash

echo "!!!! WARNING: Submitting for MC!!!"
python submit_allHLT.py \
  ../python/Configs/testTriggerPaths_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Rates/ \
  -p reco=HLT_TRKv06_TICL BTVreco=cutsV2 \
  -v crab_projects_Rates_TRKv06_TICL_cutsV2_v1 \
  -t 2750 \
  -m 4500
