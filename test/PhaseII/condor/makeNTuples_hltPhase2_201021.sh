# #!/bin/bash

# set -e

if [ $# -lt 1 ]; then
  printf "\n%s\n\n" ">> argument missing - specify path to output directory"
  exit 1
fi

NEVT=-1

ODIR=$1

if [ -d ${ODIR} ]; then
  printf "%s\n" "output directory already exists: ${ODIR}"
  exit 1
fi

declare -A samplesMap
samplesMap["Phase2HLTTDR_MinBias_14TeV_PU200"]="/MinBias_TuneCP5_14TeV-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/FEVT"
samplesMap["Phase2HLTTDR_MinBias_14TeV_PU200_ext1"]="/MinBias_TuneCP5_14TeV-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_withNewMB_111X_mcRun4_realistic_T15_v1_ext1-v2/FEVT"
samplesMap["Phase2HLTTDR_QCD_Pt020to030_14TeV_PU200"]="/QCD_Pt_20to30_TuneCP5_14TeV_pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_withNewMB_111X_mcRun4_realistic_T15_v1-v2/GEN-SIM-DIGI-RAW-MINIAOD"
samplesMap["Phase2HLTTDR_QCD_Pt030to050_14TeV_PU200"]="/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/GEN-SIM-DIGI-RAW-MINIAOD"
samplesMap["Phase2HLTTDR_QCD_Pt030to050_14TeV_PU200_ext1"]="/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_withNewMB_111X_mcRun4_realistic_T15_v1_ext1-v2/GEN-SIM-DIGI-RAW-MINIAOD"
samplesMap["Phase2HLTTDR_QCD_Pt050to080_14TeV_PU200"]="/QCD_Pt_50to80_TuneCP5_14TeV_pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/GEN-SIM-DIGI-RAW-MINIAOD"
samplesMap["Phase2HLTTDR_QCD_Pt050to080_14TeV_PU200_ext1"]="/QCD_Pt_50to80_TuneCP5_14TeV_pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_withNewMB_111X_mcRun4_realistic_T15_v1_ext1-v3/GEN-SIM-DIGI-RAW-MINIAOD"
samplesMap["Phase2HLTTDR_QCD_Pt080to120_14TeV_PU200"]="/QCD_Pt_80to120_TuneCP5_14TeV_pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/GEN-SIM-DIGI-RAW-MINIAOD"
samplesMap["Phase2HLTTDR_QCD_Pt120to170_14TeV_PU200"]="/QCD_Pt_120to170_TuneCP5_14TeV_pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/GEN-SIM-DIGI-RAW-MINIAOD"
samplesMap["Phase2HLTTDR_QCD_Pt170to300_14TeV_PU200"]="/QCD_Pt_170to300_TuneCP5_14TeV_pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/GEN-SIM-DIGI-RAW-MINIAOD"
samplesMap["Phase2HLTTDR_QCD_Pt300to470_14TeV_PU200"]="/QCD_Pt_300to470_TuneCP5_14TeV_pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/GEN-SIM-DIGI-RAW-MINIAOD"
samplesMap["Phase2HLTTDR_QCD_Pt470to600_14TeV_PU200"]="/QCD_Pt_470to600_TuneCP5_14TeV_pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/GEN-SIM-DIGI-RAW-MINIAOD"
samplesMap["Phase2HLTTDR_QCD_Pt600toInf_14TeV_PU200"]="/QCD_Pt_600oInf_TuneCP5_14TeV_pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/GEN-SIM-DIGI-RAW-MINIAOD"
samplesMap["Phase2HLTTDR_WJetsToLNu_14TeV_PU200"]="/WJetsToLNu_TuneCP5_14TeV-amcatnloFXFX-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/GEN-SIM-DIGI-RAW-MINIAOD"
samplesMap["Phase2HLTTDR_DYJetsToLL_M010to050_14TeV_PU200"]="/DYJetsToLL_M-10to50_TuneCP5_14TeV-madgraphMLM-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/GEN-SIM-DIGI-RAW-MINIAOD"
samplesMap["Phase2HLTTDR_DYJetsToLL_M050toInf_14TeV_PU200"]="/DYToLL_M-50_TuneCP5_14TeV-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_pilot_111X_mcRun4_realistic_T15_v1-v1/FEVT"
samplesMap["Phase2HLTTDR_HH4b_14TeV_PU200"]="/GluGluToHHTo4B_node_SM_TuneCP5_14TeV-madgraph_pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/FEVT"
# samplesMap["Phase2HLTTDR_TTbar_14TeV_NoPU"]="/TT_TuneCP5_14TeV-powheg-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v2/FEVT"
# samplesMap["Phase2HLTTDR_TTbar_14TeV_PU200"]="/TT_TuneCP5_14TeV-powheg-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v2/FEVT"
samplesMap["Phase2HLTTDR_TTbar2L_14TeV_PU200"]="/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/FEVT"
samplesMap["Phase2HLTTDR_TTbar1L_14TeV_PU200"]="/TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/FEVT"

recoKeys=(
#  HLT_TRKv00
#  HLT_TRKv00_TICL
#  HLT_TRKv02
#  HLT_TRKv02_TICL
#  HLT_TRKv06
#  HLT_TRKv06_TICL
#  HLT_TRKv06_TICL2
  # HLT_TRKv06p1
  HLT_TRKv06p1_TICL
  # HLT_TRKv06p3
  # HLT_TRKv06p3_TICL
#  HLT_TRKv06p1_TICL2
  # HLT_TRKv07p2
  # HLT_TRKv07p2_TICL
#  HLT_TRKv07p2_TICL2
)

btvRecoKeys=(
  # default
  cutsV2
)

for sampleKey in ${!samplesMap[@]}; do
  nEvents=${NEVT}


  sampleName=${samplesMap[${sampleKey}]}

  # lxplus: specify JobFlavour and AccountingGroup
  # [[ ${HOSTNAME} != lxplus* ]] || opts="--JobFlavour longlunch --AccountingGroup group_u_CMS.CAF.PHYS --no-export-LD-LIBRARY-PATH"
  [[ ${HOSTNAME} != lxplus* ]] || opts="--JobFlavour longlunch --AccountingGroup group_u_CMS.CAF.PHYS"

  for recoKey in "${recoKeys[@]}"; do
    for btvRecoKey in "${btvRecoKeys[@]}"; do
      python ../runHLTBTagAnalyzer_PhaseII_cfg.py dumpPython=/tmp/${USER}/${recoKey}_${btvRecoKey}_cfg.py numThreads=1 reco=${recoKey} BTVreco=${btvRecoKey} globalTag=111X_mcRun4_realistic_T15_v2

      htc_driver -c /tmp/${USER}/${recoKey}_${btvRecoKey}_cfg.py --customize-cfg -m ${nEvents} -n 200 --cpus 1 --memory 2000 --runtime 10800 ${opts} \
        -d ${sampleName} -p 0 -o ${ODIR}/${recoKey}_${btvRecoKey}/${sampleKey}
    done
  done
  unset recoKey sampleName nEvents btvRecoKey
done
unset sampleKey NEVT ODIR recoKeys samplesMap btvRecoKeys
