#!/bin/bash

echo "!!!! WARNING: Submitting for MC!!!"
python submit_allHLT.py \
  testTriggerPaths_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Rates/ \
  -p reco=HLT_TRKv06_TICL BTVreco=cutsV1 \
  -v crab_projects_Workshop_TrackingV6_TICL_cutsV1_v1 \
  -t 2750 \
  -m 2500
