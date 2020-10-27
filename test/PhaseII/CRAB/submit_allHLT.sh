#!/bin/bash

echo "!!!! WARNING: Submitting for MC!!!"
# ==========================cutsv2===================
# python ../submit_allHLT.py \
#   ../runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=HLT_TRKv00 BTVreco=cutsV2 \
#   -v crab_projects_OctoberWorkshop_TrackingV0_cutsV2_v1 \
#   -t 2750 \
#   -m 4500

python ../submit_allHLT.py \
  ../runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv06p1_TICL BTVreco=cutsV2 \
  -v crab_projects_OctoberWorkshop_TrackingV6p1_TICLV2_cutsV2_v1 \
  -t 2750 \
  -m 4500

python ../submit_allHLT.py \
  ../runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv07p2_TICL BTVreco=cutsV2 \
  -v crab_projects_OctoberWorkshop_TrackingV7p2_TICLV2_cutsV2_v1 \
  -t 2750 \
  -m 4500

# python ../submit_allHLT.py \
#   ../runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=HLT_TRKv06p1 BTVreco=cutsV2 \
#   -v crab_projects_OctoberWorkshop_TrackingV6p1_cutsV2_v1 \
#   -t 2750 \
#   -m 4500
#
# python ../submit_allHLT.py \
#   ../runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=HLT_TRKv07p2 BTVreco=cutsV2 \
#   -v crab_projects_OctoberWorkshop_TrackingV7p2_cutsV2_v1 \
#   -t 2750 \
#   -m 4500
  # ==========================cutsv1===================
# python ../submit_allHLT.py \
#   ../runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=HLT_TRKv00 BTVreco=cutsV1 \
#   -v crab_projects_OctoberWorkshop_TrackingV0_cutsV1_v1 \
#   -t 2750 \
#   -m 4500

python ../submit_allHLT.py \
  ../runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv06p1_TICL BTVreco=cutsV1 \
  -v crab_projects_OctoberWorkshop_TrackingV6p1_TICLV2_cutsV1_v1 \
  -t 2750 \
  -m 4500

python ../submit_allHLT.py \
    ../runHLTBTagAnalyzer_PhaseII_cfg.py \
    -f tosubmit.txt \
    -s T2_DE_DESY \
    -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
    -p reco=HLT_TRKv07p2_TICL BTVreco=cutsV1 \
    -v crab_projects_OctoberWorkshop_TrackingV7p2_TICLV2_cutsV1_v1 \
    -t 2750 \
    -m 4500

# python ../submit_allHLT.py \
#   ../runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=HLT_TRKv06p1 BTVreco=cutsV1 \
#   -v crab_projects_OctoberWorkshop_TrackingV6p1_cutsV1_v1 \
#   -t 2750 \
#   -m 4500

# python ../submit_allHLT.py \
#     ../runHLTBTagAnalyzer_PhaseII_cfg.py \
#     -f tosubmit.txt \
#     -s T2_DE_DESY \
#     -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#     -p reco=HLT_TRKv07p2 BTVreco=cutsV1 \
#     -v crab_projects_OctoberWorkshop_TrackingV7p2_cutsV1_v1 \
#     -t 2750 \
#     -m 4500
# ==========================default===================
# python ../submit_allHLT.py \
#   ../runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=HLT_TRKv00 BTVreco=default \
#   -v crab_projects_OctoberWorkshop_TrackingV0_default_v1 \
#   -t 2750 \
#   -m 4500

python ../submit_allHLT.py \
  ../runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv06p1_TICL BTVreco=default \
  -v crab_projects_OctoberWorkshop_TrackingV6p1_TICLV2_default_v1 \
  -t 2750 \
  -m 4500

python ../submit_allHLT.py \
  ../runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv07p2_TICL BTVreco=default \
  -v crab_projects_OctoberWorkshop_TrackingV7p2_TICLV2_default_v1 \
  -t 2750 \
  -m 4500

# python ../submit_allHLT.py \
#   ../runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=HLT_TRKv06p1 BTVreco=default \
#   -v crab_projects_OctoberWorkshop_TrackingV6p1_default_v1 \
#   -t 2750 \
#   -m 4500
#
# python ../submit_allHLT.py \
#   ../runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=HLT_TRKv07p2 BTVreco=default \
#   -v crab_projects_OctoberWorkshop_TrackingV7p2_default_v1 \
#   -t 2750 \
#   -m 4500
