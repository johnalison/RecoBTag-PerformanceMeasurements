#!/bin/bash

echo "!!!! WARNING: Submitting for MC!!!"
python submit_allHLT.py \
  runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv00 BTVreco=cutsV1 \
  -v crab_projects_Workshop_TrackingV0_cutsV1_v3 \
  -t 2750 \
  -m 5000

# python submit_allHLT.py \
#   runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f CRAB/tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=HLT_TRKv02 \
#   -v crab_projects_Workshop_TrackingV2_v1 \
#   -t 2750 \
#   -m 3500

# python submit_allHLT.py \
#   runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f CRAB/tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=HLT_TRKv06 \
#   -v crab_projects_Workshop_TrackingV6_v1 \
#   -t 2750 \
#   -m 3500

# python submit_allHLT.py \
#   runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f CRAB/tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=HLT_TRKv06_skimmedTracks \
#   -v crab_projects_Workshop_TrackingV6_skimmedTracks_v1 \
#   -t 2750 \
#   -m 3500

# python submit_allHLT.py \
#   runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f CRAB/tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=HLT_TRKv00_TICL \
#   -v crab_projects_Workshop_TrackingV0TICL_v1 \
#   -t 2750 \
#   -m 4500
#
# python submit_allHLT.py \
#   runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f CRAB/tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=HLT_TRKv02_TICL \
#   -v crab_projects_Workshop_TrackingV2TICL_v1 \
#   -t 2750 \
#   -m 4500
#
python submit_allHLT.py \
  runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv06_TICL BTVreco=cutsV1 \
  -v crab_projects_Workshop_TrackingV6TICL_cutsV1_v3 \
  -t 2750 \
  -m 5000

# python submit_allHLT.py \
#   runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f CRAB/tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=HLT_TRKv06_TICL_skimmedTracks \
#   -v crab_projects_Workshop_TrackingV6TICL_skimmedTracks_v1 \
#   -t 2750 \
#   -m 4500
