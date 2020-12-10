#ifndef EVENTINFOBRANCHES_H
#define EVENTINFOBRANCHES_H

#include <TTree.h>
#include "RecoBTag/PerformanceMeasurements/interface/VariableParser.h"

const UInt_t nMaxPVs_= 1000;
const UInt_t nMaxPUs_= 1000;
const UInt_t nMaxTrkAll_ = 100000;
const UInt_t nMaxQuarks = 1000;
const UInt_t nMaxHadrons = 100;
const UInt_t nMaxGenLeps = 100;
const UInt_t nMaxGenQuarks = 100;
const UInt_t nMaxGenJets = 100;
const UInt_t nMaxGenV0 = 100;
const UInt_t nMaxGenPruned = 100;
const UInt_t nMaxPatMuon = 1000;
const UInt_t nMaxPatElec = 1000;
const UInt_t nMaxL1Vertices_ = 10000;
const UInt_t nMaxL1Tracks_ = 10000;
const UInt_t nMaxL1Jets_ = 10000;

class EventInfoBranches {

  public :

    int   nBitTrigger;
    int   BitTrigger[100];
    int   Run;
    int   Evt;
    int   LumiBlock;
    float PVz;
    float PVez;
    float GenPVz;
    float pthat;
    float mcweight;
    float rho;

    float qcdWeightPU140;
    float qcdWeightPU200;

    float HepMCGenEvent_scale;
    float GenEventInfo_qScale;
    float pileupInfo_BX0_numPUInteractions;
    float pileupInfo_BX0_numTrueInteractions;
    float pileupInfo_BX0_max_pT_hats;
    float pileupInfo_BX0_n_pThat000to020;
    float pileupInfo_BX0_n_pThat020to030;
    float pileupInfo_BX0_n_pThat030to050;
    float pileupInfo_BX0_n_pThat050to080;
    float pileupInfo_BX0_n_pThat080to120;
    float pileupInfo_BX0_n_pThat120to170;
    float pileupInfo_BX0_n_pThat170to300;
    float pileupInfo_BX0_n_pThat300to470;
    float pileupInfo_BX0_n_pThat470to600;
    float pileupInfo_BX0_n_pThat600toInf;

    int   nPV;
    int   BX;
    float PV_x[nMaxPVs_];
    float PV_y[nMaxPVs_];
    float PV_z[nMaxPVs_];
    float PV_ex[nMaxPVs_];
    float PV_ey[nMaxPVs_];
    float PV_ez[nMaxPVs_];
    float PV_chi2[nMaxPVs_];
    float PV_ndf[nMaxPVs_];
    int   PV_isgood[nMaxPVs_];
    int   PV_isfake[nMaxPVs_];

    float nPUtrue;
    int   nPU;

    int   PU_bunch[nMaxPUs_];
    float PU_z[nMaxPUs_];
    float PU_sumpT_low[nMaxPUs_];
    float PU_sumpT_high[nMaxPUs_];
    int   PU_ntrks_low[nMaxPUs_];
    int   PU_ntrks_high[nMaxPUs_];

    int   ncQuarks;
    float cQuark_pT[nMaxQuarks];
    float cQuark_eta[nMaxQuarks];
    float cQuark_phi[nMaxQuarks];
    int   cQuark_pdgID[nMaxQuarks];
    int   cQuark_status[nMaxQuarks];
    int   cQuark_fromGSP[nMaxQuarks];

    int   nbQuarks;
    float bQuark_pT[nMaxQuarks];
    float bQuark_eta[nMaxQuarks];
    float bQuark_phi[nMaxQuarks];
    int   bQuark_pdgID[nMaxQuarks];
    int   bQuark_status[nMaxQuarks];
    int   bQuark_fromGSP[nMaxQuarks];

    int   nBHadrons;
    float BHadron_pT[nMaxHadrons];
    float BHadron_eta[nMaxHadrons];
    float BHadron_phi[nMaxHadrons];
    float BHadron_mass[nMaxHadrons];
    int   BHadron_pdgID[nMaxHadrons];
    int   BHadron_mother[nMaxHadrons];
    int   BHadron_hasBdaughter[nMaxHadrons];
    float BHadron_SVx[nMaxHadrons];
    float BHadron_SVy[nMaxHadrons];
    float BHadron_SVz[nMaxHadrons];
    int   BHadron_nCharged[nMaxHadrons];
    int   BHadron_DHadron1[nMaxHadrons];
    int   BHadron_DHadron2[nMaxHadrons];

    int   nDHadrons;
    int   nDaughters;
    float DHadron_pT[nMaxHadrons];
    float DHadron_eta[nMaxHadrons];
    float DHadron_phi[nMaxHadrons];
    float DHadron_mass[nMaxHadrons];
    float DHadron_SVx[nMaxHadrons];
    float DHadron_SVy[nMaxHadrons];
    float DHadron_SVz[nMaxHadrons];
    int   DHadron_pdgID[nMaxHadrons];
    int   DHadron_nDaughters[nMaxHadrons];
    int   DHadron_DaughtersPdgID[nMaxHadrons*15]; //
    int   DHadron_nChargedDaughters[nMaxHadrons];
    int   DHadron_nCharged[nMaxHadrons];

    int   nGenlep;
    float Genlep_pT[nMaxGenLeps];
    float Genlep_eta[nMaxGenLeps];
    float Genlep_phi[nMaxGenLeps];
    int   Genlep_pdgID[nMaxGenLeps];
    int   Genlep_status[nMaxGenLeps];
    int   Genlep_mother[nMaxGenLeps];

    int   nGenquark;
    float Genquark_pT[nMaxGenQuarks];
    float Genquark_eta[nMaxGenQuarks];
    float Genquark_phi[nMaxGenQuarks];
    int   Genquark_pdgID[nMaxGenQuarks];
    int   Genquark_mother[nMaxGenQuarks];

    int   nGenJets;
    float GenJet_pT[nMaxGenJets];
    float GenJet_eta[nMaxGenJets];
    float GenJet_phi[nMaxGenJets];
    float GenJet_mass[nMaxGenJets];

    int   nGenV0;
    float GenV0_pT[nMaxGenV0];
    float GenV0_eta[nMaxGenV0];
    float GenV0_phi[nMaxGenV0];
    int   GenV0_pdgID[nMaxGenV0];
    float GenV0_SVx[nMaxGenV0];
    float GenV0_SVy[nMaxGenV0];
    float GenV0_SVz[nMaxGenV0];
    int   GenV0_nCharged[nMaxGenV0];

    // HP means hard process
    int   nGenPruned;
    float GenPruned_pT[nMaxGenPruned];
    float GenPruned_eta[nMaxGenPruned];
    float GenPruned_phi[nMaxGenPruned];
    float GenPruned_mass[nMaxGenPruned];
    int   GenPruned_status[nMaxGenPruned];
    int   GenPruned_pdgID[nMaxGenPruned];
    int   GenPruned_mother[nMaxGenPruned];

    int   nTrkAll;
    float TrkAll_d0[nMaxTrk_];
    float TrkAll_dz[nMaxTrk_];
    float TrkAll_p[nMaxTrk_];
    float TrkAll_pt[nMaxTrk_];
    float TrkAll_eta[nMaxTrk_];
    float TrkAll_phi[nMaxTrk_];
    float TrkAll_chi2[nMaxTrk_];
    int   TrkAll_charge[nMaxTrk_];
    int   TrkAll_nHitAll[nMaxTrk_];
    int   TrkAll_nHitPixel[nMaxTrk_];
    int   TrkAll_nHitStrip[nMaxTrk_];
    int   TrkAll_nHitTIB[nMaxTrk_];
    int   TrkAll_nHitTID[nMaxTrk_];
    int   TrkAll_nHitTOB[nMaxTrk_];
    int   TrkAll_nHitTEC[nMaxTrk_];
    int   TrkAll_nHitPXB[nMaxTrk_];
    int   TrkAll_nHitPXF[nMaxTrk_];
    int   TrkAll_isHitL1[nMaxTrk_];
    int   TrkAll_nSiLayers[nMaxTrk_];
    int   TrkAll_nPxLayers[nMaxTrk_];
    int   TrkAll_PV[nMaxTrk_];
    float TrkAll_PVweight[nMaxTrk_];

    //if storePatMuons
    //run2 id: https://twiki.cern.ch/CMS/SWGuideMuonIdRun2
    int nPatMuon;
    float PatMuon_pt[nMaxPatMuon];
    float PatMuon_eta[nMaxPatMuon];
    float PatMuon_phi[nMaxPatMuon];
    int PatMuon_isSoftMuon[nMaxPatMuon];
    bool PatMuon_isMediumMuon[nMaxPatMuon];
    int PatMuon_isTightMuon[nMaxPatMuon];
    float PatMuon_iso[nMaxPatMuon];
    float PatMuon_isoTrackerOnly[nMaxPatMuon];
    float PatMuon_IP[nMaxPatMuon];
    float PatMuon_IPsig[nMaxPatMuon];
    float PatMuon_IP2D[nMaxPatMuon];
    float PatMuon_IP2Dsig[nMaxPatMuon];

    //if storePatMuons
    //run2 id: https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2
    int nPatElec;
    float PatElec_pt[nMaxPatElec];
    float PatElec_eta[nMaxPatElec];
    float PatElec_superClusterEta[nMaxPatElec];
    float PatElec_phi[nMaxPatElec];
    int  PatElec_isLooseElec[nMaxPatElec];
    int  PatElec_isMediumElec[nMaxPatElec];
    int  PatElec_isTightElec[nMaxPatElec];
    float PatElec_sumChargedHadronPt[nMaxPatElec];
    float PatElec_sumNeutralHadronEt[nMaxPatElec];
    float PatElec_sumPhotonEt[nMaxPatElec];
    float PatElec_sumPUPt[nMaxPatElec];

    //float PatMuon_iso[nMaxPatMuon];
    //float PatMuon_isoTrackerOnly[nMaxPatMuon];
    //float PatMuon_IP[nMaxPatMuon];
    //float PatMuon_IPsig[nMaxPatMuon];
    //float PatMuon_IP2D[nMaxPatMuon];
    //float PatMuon_IP2Dsig[nMaxPatMuon];

    int nL1_Vertices;
    float L1_Vertex_z[nMaxL1Vertices_];
    float L1_Vertex_sum[nMaxL1Vertices_];
    int nL1_BarrelTracks;
    float L1_BarrelTrack_pt[nMaxL1Tracks_];
    float L1_BarrelTrack_eta[nMaxL1Tracks_];
    float L1_BarrelTrack_phi[nMaxL1Tracks_];
    float L1_BarrelTrack_m[nMaxL1Tracks_];
    float L1_BarrelTrack_dxy[nMaxL1Tracks_];
    float L1_BarrelTrack_dz[nMaxL1Tracks_];
    int nL1_HGCalTracks;
    float L1_HGCalTrack_pt[nMaxL1Tracks_];
    float L1_HGCalTrack_eta[nMaxL1Tracks_];
    float L1_HGCalTrack_phi[nMaxL1Tracks_];
    float L1_HGCalTrack_m[nMaxL1Tracks_];
    float L1_HGCalTrack_dxy[nMaxL1Tracks_];
    float L1_HGCalTrack_dz[nMaxL1Tracks_];
    int nL1_Tracks;
    float L1_Track_pt[nMaxL1Tracks_];
    float L1_Track_eta[nMaxL1Tracks_];
    float L1_Track_phi[nMaxL1Tracks_];
    float L1_Track_m[nMaxL1Tracks_];
    float L1_Track_dxy[nMaxL1Tracks_];
    float L1_Track_dz[nMaxL1Tracks_];
    int nL1_ExtendedTracks;
    float L1_ExtendedTrack_pt[nMaxL1Tracks_];
    float L1_ExtendedTrack_eta[nMaxL1Tracks_];
    float L1_ExtendedTrack_phi[nMaxL1Tracks_];
    float L1_ExtendedTrack_m[nMaxL1Tracks_];
    float L1_ExtendedTrack_dxy[nMaxL1Tracks_];
    float L1_ExtendedTrack_dz[nMaxL1Tracks_];
    int nL1_PFJets;
    float L1_PFJets_pt[nMaxL1Jets_];
    float L1_PFJets_eta[nMaxL1Jets_];
    float L1_PFJets_phi[nMaxL1Jets_];
    float L1_PFJets_m[nMaxL1Jets_];
    float L1_PFJets_dxy[nMaxL1Jets_];
    float L1_PFJets_dz[nMaxL1Jets_];
    int nL1_PuppiJets;
    float L1_PuppiJets_pt[nMaxL1Jets_];
    float L1_PuppiJets_eta[nMaxL1Jets_];
    float L1_PuppiJets_phi[nMaxL1Jets_];
    float L1_PuppiJets_m[nMaxL1Jets_];
    float L1_PuppiJets_dxy[nMaxL1Jets_];
    float L1_PuppiJets_dz[nMaxL1Jets_];

    float L1_HT_pt;
    float L1_HT_phi;
    float L1_HT_sumEt;

    float HLT_HT_2p4_pt;
    float HLT_HT_2p4_phi;
    float HLT_HT_2p4_sumEt;
    float HLT_HT_4p0_pt;
    float HLT_HT_4p0_phi;
    float HLT_HT_4p0_sumEt;
    float HLT_HT_jme_pt;
    float HLT_HT_jme_phi;
    float HLT_HT_jme_sumEt;

    int   ttbar_chan, ttbar_trigWord, ttbar_metfilterWord, ttbar_allmepartons, ttbar_matchmepartons;
    int   ttbar_ng,ttbar_gid[25];
    int   ttbar_nl, ttbar_lid[10], ttbar_lgid[10], ttbar_lch[10];
    int   ttbar_nw;
    float ttbar_gpt[25],ttbar_geta[25],ttbar_gphi[25],ttbar_gm[25];
    float ttbar_lpt[10], ttbar_leta[10], ttbar_lphi[10], ttbar_lm[10];
    float ttbar_metpt,ttbar_metphi;
    float ttbar_w[1200];
    float ttbar_ptweight;


    void RegisterBranches(TTree *tree, VariableParser variableParser){
      if(variableParser.isToBeStored("nBitTrigger")) tree->Branch("nBitTrigger", &nBitTrigger,  "nBitTrigger/I");
      if(variableParser.isToBeStored("BitTrigger")) tree->Branch("BitTrigger" , BitTrigger  ,  "BitTrigger[nBitTrigger]/I");
      if(variableParser.isToBeStored("Run")) tree->Branch("Run"        , &Run        ,  "Run/I");
      if(variableParser.isToBeStored("Evt")) tree->Branch("Evt"        , &Evt        ,  "Evt/I");
      if(variableParser.isToBeStored("LumiBlock")) tree->Branch("LumiBlock"  , &LumiBlock  ,  "LumiBlock/I");
      if(variableParser.isToBeStored("pthat")) tree->Branch("pthat"      , &pthat      ,  "pthat/F");
      if(variableParser.isToBeStored("mcweight")) tree->Branch("mcweight"   , &mcweight   ,  "mcweight/F");
      if(variableParser.isToBeStored("qcdWeightPU140")) tree->Branch("qcdWeightPU140"   , &qcdWeightPU140   ,  "qcdWeightPU140/F");
      if(variableParser.isToBeStored("qcdWeightPU200")) tree->Branch("qcdWeightPU200"   , &qcdWeightPU200   ,  "qcdWeightPU200/F");
      if(variableParser.isToBeStored("HepMCGenEvent_scale")) tree->Branch("HepMCGenEvent_scale"   , &HepMCGenEvent_scale   ,  "HepMCGenEvent_scale/F");
      if(variableParser.isToBeStored("GenEventInfo_qScale")) tree->Branch("GenEventInfo_qScale"   , &GenEventInfo_qScale   ,  "GenEventInfo_qScale/F");
      if(variableParser.isToBeStored("pileupInfo_BX0_numPUInteractions")) tree->Branch("pileupInfo_BX0_numPUInteractions"   , &pileupInfo_BX0_numPUInteractions   ,  "pileupInfo_BX0_numPUInteractions/F");
      if(variableParser.isToBeStored("pileupInfo_BX0_numTrueInteractions")) tree->Branch("pileupInfo_BX0_numTrueInteractions"   , &pileupInfo_BX0_numTrueInteractions   ,  "pileupInfo_BX0_numTrueInteractions/F");
      if(variableParser.isToBeStored("pileupInfo_BX0_max_pT_hats")) tree->Branch("pileupInfo_BX0_max_pT_hats"   , &pileupInfo_BX0_max_pT_hats   ,  "pileupInfo_BX0_max_pT_hats/F");
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat000to020")) tree->Branch("pileupInfo_BX0_n_pThat000to020"   , &pileupInfo_BX0_n_pThat000to020   ,  "pileupInfo_BX0_n_pThat000to020/F");
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat020to030")) tree->Branch("pileupInfo_BX0_n_pThat020to030"   , &pileupInfo_BX0_n_pThat020to030   ,  "pileupInfo_BX0_n_pThat020to030/F");
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat030to050")) tree->Branch("pileupInfo_BX0_n_pThat030to050"   , &pileupInfo_BX0_n_pThat030to050   ,  "pileupInfo_BX0_n_pThat030to050/F");
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat050to080")) tree->Branch("pileupInfo_BX0_n_pThat050to080"   , &pileupInfo_BX0_n_pThat050to080   ,  "pileupInfo_BX0_n_pThat050to080/F");
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat080to120")) tree->Branch("pileupInfo_BX0_n_pThat080to120"   , &pileupInfo_BX0_n_pThat080to120   ,  "pileupInfo_BX0_n_pThat080to120/F");
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat120to170")) tree->Branch("pileupInfo_BX0_n_pThat120to170"   , &pileupInfo_BX0_n_pThat120to170   ,  "pileupInfo_BX0_n_pThat120to170/F");
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat170to300")) tree->Branch("pileupInfo_BX0_n_pThat170to300"   , &pileupInfo_BX0_n_pThat170to300   ,  "pileupInfo_BX0_n_pThat170to300/F");
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat300to470")) tree->Branch("pileupInfo_BX0_n_pThat300to470"   , &pileupInfo_BX0_n_pThat300to470   ,  "pileupInfo_BX0_n_pThat300to470/F");
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat470to600")) tree->Branch("pileupInfo_BX0_n_pThat470to600"   , &pileupInfo_BX0_n_pThat470to600   ,  "pileupInfo_BX0_n_pThat470to600/F");
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat600toInf")) tree->Branch("pileupInfo_BX0_n_pThat600toInf"   , &pileupInfo_BX0_n_pThat600toInf   ,  "pileupInfo_BX0_n_pThat600toInf/F");

      if(variableParser.isToBeStored("BX")) tree->Branch("BX"         , &BX         ,  "BX/I");
      if(variableParser.isToBeStored("nPV")) tree->Branch("nPV"        , &nPV        ,  "nPV/I");
      if(variableParser.isToBeStored("PVz")) tree->Branch("PVz"        , &PVz        ,  "PVz/F");
      if(variableParser.isToBeStored("PVez")) tree->Branch("PVez"       , &PVez       ,  "PVez/F");
      if(variableParser.isToBeStored("GenPVz")) tree->Branch("GenPVz"     , &GenPVz     ,  "GenPVz/F");
      if(variableParser.isToBeStored("rho")) tree->Branch("rho"        , &rho        ,  "rho/F");
      if(variableParser.isToBeStored("nPUtrue")) tree->Branch("nPUtrue"      , &nPUtrue     , "nPUtrue/F");
      if(variableParser.isToBeStored("nPU")) tree->Branch("nPU"          , &nPU         , "nPU/I"    );
      if(variableParser.isToBeStored("PU_bunch")) tree->Branch("PU_bunch"     , PU_bunch     , "PU_bunch[nPU]/I");
      if(variableParser.isToBeStored("PU_z")) tree->Branch("PU_z"         , PU_z         , "PU_z[nPU]/F");
      if(variableParser.isToBeStored("PU_sumpT_low")) tree->Branch("PU_sumpT_low" , PU_sumpT_low , "PU_sumpT_low[nPU]/F");
      if(variableParser.isToBeStored("PU_sumpT_high")) tree->Branch("PU_sumpT_high", PU_sumpT_high, "PU_sumpT_high[nPU]/F");
      if(variableParser.isToBeStored("PU_ntrks_low")) tree->Branch("PU_ntrks_low" , PU_ntrks_low , "PU_ntrks_low[nPU]/I");
      if(variableParser.isToBeStored("PU_ntrks_high")) tree->Branch("PU_ntrks_high", PU_ntrks_high, "PU_ntrks_high[nPU]/I");

      if(variableParser.isToBeStored("ncQuarks")) tree->Branch("ncQuarks"      , &ncQuarks     , "ncQuarks/I");
      if(variableParser.isToBeStored("cQuark_pT")) tree->Branch("cQuark_pT"     , cQuark_pT     , "cQuark_pT[ncQuarks]/F");
      if(variableParser.isToBeStored("cQuark_eta")) tree->Branch("cQuark_eta"    , cQuark_eta    , "cQuark_eta[ncQuarks]/F");
      if(variableParser.isToBeStored("cQuark_phi")) tree->Branch("cQuark_phi"    , cQuark_phi    , "cQuark_phi[ncQuarks]/F");
      if(variableParser.isToBeStored("cQuark_pdgID")) tree->Branch("cQuark_pdgID"  , cQuark_pdgID  , "cQuark_pdgID[ncQuarks]/I");
      if(variableParser.isToBeStored("cQuark_status")) tree->Branch("cQuark_status" , cQuark_status , "cQuark_status[ncQuarks]/I");
      if(variableParser.isToBeStored("cQuark_fromGSP")) tree->Branch("cQuark_fromGSP", cQuark_fromGSP, "cQuark_fromGSP[ncQuarks]/I");

      if(variableParser.isToBeStored("nbQuarks")) tree->Branch("nbQuarks",          &nbQuarks     , "nbQuarks/I");
      if(variableParser.isToBeStored("bQuark_pT")) tree->Branch("bQuark_pT",         bQuark_pT     , "bQuark_pT[nbQuarks]/F");
      if(variableParser.isToBeStored("bQuark_eta")) tree->Branch("bQuark_eta",        bQuark_eta    , "bQuark_eta[nbQuarks]/F");
      if(variableParser.isToBeStored("bQuark_phi")) tree->Branch("bQuark_phi",        bQuark_phi    , "bQuark_phi[nbQuarks]/F");
      if(variableParser.isToBeStored("bQuark_pdgID")) tree->Branch("bQuark_pdgID",      bQuark_pdgID  , "bQuark_pdgID[nbQuarks]/I");
      if(variableParser.isToBeStored("bQuark_status")) tree->Branch("bQuark_status",     bQuark_status , "bQuark_status[nbQuarks]/I");
      if(variableParser.isToBeStored("bQuark_fromGSP")) tree->Branch("bQuark_fromGSP",    bQuark_fromGSP, "bQuark_fromGSP[nbQuarks]/I");

      if(variableParser.isToBeStored("nBHadrons")) tree->Branch("nBHadrons",          &nBHadrons            ,"nBHadrons/I");
      if(variableParser.isToBeStored("BHadron_pT")) tree->Branch("BHadron_pT",           BHadron_pT          , "BHadron_pT[nBHadrons]/F");
      if(variableParser.isToBeStored("BHadron_eta")) tree->Branch("BHadron_eta",          BHadron_eta         , "BHadron_eta[nBHadrons]/F");
      if(variableParser.isToBeStored("BHadron_phi")) tree->Branch("BHadron_phi",          BHadron_phi         , "BHadron_phi[nBHadrons]/F");
      if(variableParser.isToBeStored("BHadron_mass")) tree->Branch("BHadron_mass",         BHadron_mass        , "BHadron_mass[nBHadrons]/F");
      if(variableParser.isToBeStored("BHadron_pdgID")) tree->Branch("BHadron_pdgID",        BHadron_pdgID       , "BHadron_pdgID[nBHadrons]/I");
      if(variableParser.isToBeStored("BHadron_mother")) tree->Branch("BHadron_mother",       BHadron_mother      , "BHadron_mother[nBHadrons]/I");
      if(variableParser.isToBeStored("BHadron_hasBdaughter")) tree->Branch("BHadron_hasBdaughter", BHadron_hasBdaughter, "BHadron_hasBdaughter[nBHadrons]/I");
      if(variableParser.isToBeStored("BHadron_SVx")) tree->Branch("BHadron_SVx",          BHadron_SVx         ,"BHadron_SVx[nBHadrons]/F");
      if(variableParser.isToBeStored("BHadron_SVy")) tree->Branch("BHadron_SVy",          BHadron_SVy         ,"BHadron_SVy[nBHadrons]/F");
      if(variableParser.isToBeStored("BHadron_SVz")) tree->Branch("BHadron_SVz",          BHadron_SVz         ,"BHadron_SVz[nBHadrons]/F");
      if(variableParser.isToBeStored("BHadron_nCharged")) tree->Branch("BHadron_nCharged",     BHadron_nCharged    ,"BHadron_nCharged[nBHadrons]/I");
      if(variableParser.isToBeStored("BHadron_DHadron1")) tree->Branch("BHadron_DHadron1",     BHadron_DHadron1    ,"BHadron_DHadron1[nBHadrons]/I");
      if(variableParser.isToBeStored("BHadron_DHadron2")) tree->Branch("BHadron_DHadron2",     BHadron_DHadron2    ,"BHadron_DHadron2[nBHadrons]/I");

      if(variableParser.isToBeStored("nDHadrons")) tree->Branch("nDHadrons",    &nDHadrons    ,"nDHadrons/I");
      if(variableParser.isToBeStored("nDaughters")) tree->Branch("nDaughters",   &nDaughters   ,"nDaughters/I");
      if(variableParser.isToBeStored("DHadron_pT")) tree->Branch("DHadron_pT",    DHadron_pT    ,"DHadron_pT[nDHadrons]/F");
      if(variableParser.isToBeStored("DHadron_eta")) tree->Branch("DHadron_eta",   DHadron_eta   ,"DHadron_eta[nDHadrons]/F");
      if(variableParser.isToBeStored("DHadron_phi")) tree->Branch("DHadron_phi",   DHadron_phi   ,"DHadron_phi[nDHadrons]/F");
      if(variableParser.isToBeStored("DHadron_pdgID")) tree->Branch("DHadron_pdgID", DHadron_pdgID ,"DHadron_pdgID[nDHadrons]/I");
      if(variableParser.isToBeStored("DHadron_mass")) tree->Branch("DHadron_mass",  DHadron_mass  ,"DHadron_mass[nDHadrons]/F");
      if(variableParser.isToBeStored("DHadron_SVx")) tree->Branch("DHadron_SVx",   DHadron_SVx   ,"DHadron_SVx[nDHadrons]/F");
      if(variableParser.isToBeStored("DHadron_SVy")) tree->Branch("DHadron_SVy",   DHadron_SVy   ,"DHadron_SVy[nDHadrons]/F");
      if(variableParser.isToBeStored("DHadron_SVz")) tree->Branch("DHadron_SVz",   DHadron_SVz   ,"DHadron_SVz[nDHadrons]/F");
      if(variableParser.isToBeStored("DHadron_nDaughters")) tree->Branch("DHadron_nDaughters",         DHadron_nDaughters        ,"DHadron_nDaughters[nDHadrons]/I");
      if(variableParser.isToBeStored("DHadron_DaughtersPdgID")) tree->Branch("DHadron_DaughtersPdgID",     DHadron_DaughtersPdgID    ,"DHadron_DaughtersPdgID[nDaughters]/I");
      if(variableParser.isToBeStored("DHadron_nChargedDaughters")) tree->Branch("DHadron_nChargedDaughters",  DHadron_nChargedDaughters ,"DHadron_nChargedDaughters[nDHadrons]/I");
      if(variableParser.isToBeStored("DHadron_nCharged")) tree->Branch("DHadron_nCharged", DHadron_nCharged ,"DHadron_nCharged[nDHadrons]/I");

      if(variableParser.isToBeStored("nGenlep")) tree->Branch("nGenlep",     &nGenlep       ,"nGenlep/I");
      if(variableParser.isToBeStored("Genlep_pT")) tree->Branch("Genlep_pT",     Genlep_pT    , "Genlep_pT[nGenlep]/F");
      if(variableParser.isToBeStored("Genlep_eta")) tree->Branch("Genlep_eta",    Genlep_eta   , "Genlep_eta[nGenlep]/F");
      if(variableParser.isToBeStored("Genlep_phi")) tree->Branch("Genlep_phi",    Genlep_phi   , "Genlep_phi[nGenlep]/F");
      if(variableParser.isToBeStored("Genlep_pdgID")) tree->Branch("Genlep_pdgID",  Genlep_pdgID , "Genlep_pdgID[nGenlep]/I");
      if(variableParser.isToBeStored("Genlep_status")) tree->Branch("Genlep_status", Genlep_status, "Genlep_status[nGenlep]/I");
      if(variableParser.isToBeStored("Genlep_mother")) tree->Branch("Genlep_mother", Genlep_mother, "Genlep_mother[nGenlep]/I");

      if(variableParser.isToBeStored("nGenquark")) tree->Branch("nGenquark",     &nGenquark       ,"nGenquark/I");
      if(variableParser.isToBeStored("Genquark_pT")) tree->Branch("Genquark_pT",     Genquark_pT    , "Genquark_pT[nGenquark]/F");
      if(variableParser.isToBeStored("Genquark_eta")) tree->Branch("Genquark_eta",    Genquark_eta   , "Genquark_eta[nGenquark]/F");
      if(variableParser.isToBeStored("Genquark_phi")) tree->Branch("Genquark_phi",    Genquark_phi   , "Genquark_phi[nGenquark]/F");
      if(variableParser.isToBeStored("Genquark_pdgID")) tree->Branch("Genquark_pdgID",  Genquark_pdgID , "Genquark_pdgID[nGenquark]/I");
      if(variableParser.isToBeStored("Genquark_mother")) tree->Branch("Genquark_mother", Genquark_mother, "Genquark_mother[nGenquark]/I");

      if(variableParser.isToBeStored("nGenJets")) tree->Branch("nGenJets",     &nGenJets       ,"nGenJets/I");
      if(variableParser.isToBeStored("GenJet_pT")) tree->Branch("GenJet_pT",     GenJet_pT    , "GenJet_pT[nGenJets]/F");
      if(variableParser.isToBeStored("GenJet_eta")) tree->Branch("GenJet_eta",    GenJet_eta   , "GenJet_eta[nGenJets]/F");
      if(variableParser.isToBeStored("GenJet_phi")) tree->Branch("GenJet_phi",    GenJet_phi   , "GenJet_phi[nGenJets]/F");
      if(variableParser.isToBeStored("GenJet_mass")) tree->Branch("GenJet_mass",  GenJet_mass , "GenJet_mass[nGenJets]/F");

      if(variableParser.isToBeStored("nGenPruned")) tree->Branch("nGenPruned",     &nGenPruned       ,"nGenPruned/I");
      if(variableParser.isToBeStored("GenPruned_pT")) tree->Branch("GenPruned_pT",     GenPruned_pT    , "GenPruned_pT[nGenPruned]/F");
      if(variableParser.isToBeStored("GenPruned_eta")) tree->Branch("GenPruned_eta",    GenPruned_eta   , "GenPruned_eta[nGenPruned]/F");
      if(variableParser.isToBeStored("GenPruned_phi")) tree->Branch("GenPruned_phi",    GenPruned_phi   , "GenPruned_phi[nGenPruned]/F");
      if(variableParser.isToBeStored("GenPruned_mass")) tree->Branch("GenPruned_mass",    GenPruned_mass   , "GenPruned_mass[nGenPruned]/F");
      if(variableParser.isToBeStored("GenPruned_pdgID")) tree->Branch("GenPruned_pdgID",  GenPruned_pdgID , "GenPruned_pdgID[nGenPruned]/I");
      if(variableParser.isToBeStored("GenPruned_status")) tree->Branch("GenPruned_status", GenPruned_status, "GenPruned_status[nGenPruned]/I");
      if(variableParser.isToBeStored("GenPruned_mother")) tree->Branch("GenPruned_mother", GenPruned_mother, "GenPruned_mother[nGenPruned]/I");

      if(variableParser.isToBeStored("nGenV0")) tree->Branch("nGenV0",        &nGenV0         ,"nGenV0/I");
      if(variableParser.isToBeStored("GenV0_pT")) tree->Branch("GenV0_pT",        GenV0_pT       ,"GenV0_pT[nGenV0]/F");
      if(variableParser.isToBeStored("GenV0_eta")) tree->Branch("GenV0_eta",       GenV0_eta      ,"GenV0_eta[nGenV0]/F");
      if(variableParser.isToBeStored("GenV0_phi")) tree->Branch("GenV0_phi",       GenV0_phi      ,"GenV0_phi[nGenV0]/F");
      if(variableParser.isToBeStored("GenV0_pdgID")) tree->Branch("GenV0_pdgID",     GenV0_pdgID    ,"GenV0_pdgID[nGenV0]/I");
      if(variableParser.isToBeStored("GenV0_SVx")) tree->Branch("GenV0_SVx",       GenV0_SVx      ,"GenV0_SVx[nGenV0]/F");
      if(variableParser.isToBeStored("GenV0_SVy")) tree->Branch("GenV0_SVy",       GenV0_SVy      ,"GenV0_SVy[nGenV0]/F");
      if(variableParser.isToBeStored("GenV0_SVz")) tree->Branch("GenV0_SVz",       GenV0_SVz      ,"GenV0_SVz[nGenV0]/F");
      if(variableParser.isToBeStored("GenV0_nCharged")) tree->Branch("GenV0_nCharged",  GenV0_nCharged ,"GenV0_nCharged[nGenV0]/I");

      if(variableParser.isToBeStored("PV_x")) tree->Branch("PV_x"     , PV_x     , "PV_x[nPV]/F");
      if(variableParser.isToBeStored("PV_y")) tree->Branch("PV_y"     , PV_y     , "PV_y[nPV]/F");
      if(variableParser.isToBeStored("PV_z")) tree->Branch("PV_z"     , PV_z     , "PV_z[nPV]/F");
      if(variableParser.isToBeStored("PV_ex")) tree->Branch("PV_ex"    , PV_ex    , "PV_ex[nPV]/F");
      if(variableParser.isToBeStored("PV_ey")) tree->Branch("PV_ey"    , PV_ey    , "PV_ey[nPV]/F");
      if(variableParser.isToBeStored("PV_ez")) tree->Branch("PV_ez"    , PV_ez    , "PV_ez[nPV]/F");
      if(variableParser.isToBeStored("PV_chi2")) tree->Branch("PV_chi2"  , PV_chi2  , "PV_chi2[nPV]/F");
      if(variableParser.isToBeStored("PV_ndf")) tree->Branch("PV_ndf"   , PV_ndf   , "PV_ndf[nPV]/F");
      if(variableParser.isToBeStored("PV_isgood")) tree->Branch("PV_isgood", PV_isgood, "PV_isgood[nPV]/I");
      if(variableParser.isToBeStored("PV_isfake")) tree->Branch("PV_isfake", PV_isfake, "PV_isfake[nPV]/I");

      if(variableParser.isToBeStored("nTrkAll")) tree->Branch("nTrkAll",          &nTrkAll,         "nTrkAll/I"                  );
      if(variableParser.isToBeStored("TrkAll_d0")) tree->Branch("TrkAll_d0",        TrkAll_d0,        "TrkAll_d0[nTrkAll]/F"       );
      if(variableParser.isToBeStored("TrkAll_dz")) tree->Branch("TrkAll_dz",        TrkAll_dz,        "TrkAll_dz[nTrkAll]/F"       );
      if(variableParser.isToBeStored("TrkAll_p")) tree->Branch("TrkAll_p",         TrkAll_p,         "TrkAll_p[nTrkAll]/F"        );
      if(variableParser.isToBeStored("TrkAll_pt")) tree->Branch("TrkAll_pt",        TrkAll_pt,        "TrkAll_pt[nTrkAll]/F"       );
      if(variableParser.isToBeStored("TrkAll_eta")) tree->Branch("TrkAll_eta",       TrkAll_eta,       "TrkAll_eta[nTrkAll]/F"      );
      if(variableParser.isToBeStored("TrkAll_phi")) tree->Branch("TrkAll_phi",       TrkAll_phi,       "TrkAll_phi[nTrkAll]/F"      );
      if(variableParser.isToBeStored("TrkAll_chi2")) tree->Branch("TrkAll_chi2",      TrkAll_chi2,      "TrkAll_chi2[nTrkAll]/F"     );
      if(variableParser.isToBeStored("TrkAll_charge")) tree->Branch("TrkAll_charge",    TrkAll_charge,    "TrkAll_charge[nTrkAll]/I"   );
      if(variableParser.isToBeStored("TrkAll_nHitAll")) tree->Branch("TrkAll_nHitAll",   TrkAll_nHitAll,   "TrkAll_nHitAll[nTrkAll]/I"  );
      if(variableParser.isToBeStored("TrkAll_nHitPixel")) tree->Branch("TrkAll_nHitPixel", TrkAll_nHitPixel, "TrkAll_nHitPixel[nTrkAll]/I");
      if(variableParser.isToBeStored("TrkAll_nHitStrip")) tree->Branch("TrkAll_nHitStrip", TrkAll_nHitStrip, "TrkAll_nHitStrip[nTrkAll]/I");
      if(variableParser.isToBeStored("TrkAll_nHitTIB")) tree->Branch("TrkAll_nHitTIB",   TrkAll_nHitTIB,   "TrkAll_nHitTIB[nTrkAll]/I"  );
      if(variableParser.isToBeStored("TrkAll_nHitTID")) tree->Branch("TrkAll_nHitTID",   TrkAll_nHitTID,   "TrkAll_nHitTID[nTrkAll]/I"  );
      if(variableParser.isToBeStored("TrkAll_nHitTOB")) tree->Branch("TrkAll_nHitTOB",   TrkAll_nHitTOB,   "TrkAll_nHitTOB[nTrkAll]/I"  );
      if(variableParser.isToBeStored("TrkAll_nHitTEC")) tree->Branch("TrkAll_nHitTEC",   TrkAll_nHitTEC,   "TrkAll_nHitTEC[nTrkAll]/I"  );
      if(variableParser.isToBeStored("TrkAll_nHitPXB")) tree->Branch("TrkAll_nHitPXB",   TrkAll_nHitPXB,   "TrkAll_nHitPXB[nTrkAll]/I"  );
      if(variableParser.isToBeStored("TrkAll_nHitPXF")) tree->Branch("TrkAll_nHitPXF",   TrkAll_nHitPXF,   "TrkAll_nHitPXF[nTrkAll]/I"  );
      if(variableParser.isToBeStored("TrkAll_isHitL1")) tree->Branch("TrkAll_isHitL1",   TrkAll_isHitL1,   "TrkAll_isHitL1[nTrkAll]/I"  );
      if(variableParser.isToBeStored("TrkAll_nSiLayers")) tree->Branch("TrkAll_nSiLayers", TrkAll_nSiLayers, "TrkAll_nSiLayers[nTrkAll]/I");
      if(variableParser.isToBeStored("TrkAll_nPxLayers")) tree->Branch("TrkAll_nPxLayers", TrkAll_nPxLayers, "TrkAll_nPxLayers[nTrkAll]/I");
      if(variableParser.isToBeStored("TrkAll_PV")) tree->Branch("TrkAll_PV",        TrkAll_PV,        "TrkAll_PV[nTrkAll]/I"       );
      if(variableParser.isToBeStored("TrkAll_PVweight")) tree->Branch("TrkAll_PVweight",  TrkAll_PVweight,  "TrkAll_PVweight[nTrkAll]/F" );

      if(variableParser.isToBeStored("ttbar_chan")) tree->Branch("ttbar_chan" , &ttbar_chan  , "ttbar_chan/I");
      if(variableParser.isToBeStored("ttbar_trigWord")) tree->Branch("ttbar_trigWord" , &ttbar_trigWord, "ttbar_trigWord/I");
      if(variableParser.isToBeStored("ttbar_metfilterWord")) tree->Branch("ttbar_metfilterWord" , &ttbar_metfilterWord, "ttbar_metfilterWord/I");
      if(variableParser.isToBeStored("ttbar_allmepartons")) tree->Branch("ttbar_allmepartons" , &ttbar_allmepartons, "ttbar_allmepartons/I");
      if(variableParser.isToBeStored("ttbar_matchmepartons")) tree->Branch("ttbar_matchmepartons" , &ttbar_matchmepartons, "ttbar_matchmepartons/I");
      if(variableParser.isToBeStored("ttbar_ng")) tree->Branch("ttbar_ng"   , &ttbar_ng    , "ttbar_ng/I");
      if(variableParser.isToBeStored("ttbar_gpt")) tree->Branch("ttbar_gpt"  ,  ttbar_gpt   , "ttbar_gpt[ttbar_ng]/F");
      if(variableParser.isToBeStored("ttbar_geta")) tree->Branch("ttbar_geta" ,  ttbar_geta  , "ttbar_geta[ttbar_ng]/F");
      if(variableParser.isToBeStored("ttbar_gphi")) tree->Branch("ttbar_gphi" ,  ttbar_gphi  , "ttbar_gphi[ttbar_ng]/F");
      if(variableParser.isToBeStored("ttbar_gm")) tree->Branch("ttbar_gm"   ,  ttbar_gm    , "ttbar_gm[ttbar_ng]/F");
      if(variableParser.isToBeStored("ttbar_gid")) tree->Branch("ttbar_gid"  ,  ttbar_gid   , "ttbar_gid[ttbar_ng]/I");
      if(variableParser.isToBeStored("ttbar_nl")) tree->Branch("ttbar_nl"   , &ttbar_nl    , "ttbar_nl/I");
      if(variableParser.isToBeStored("ttbar_lpt")) tree->Branch("ttbar_lpt"  ,  ttbar_lpt   , "ttbar_lpt[ttbar_nl]/F");
      if(variableParser.isToBeStored("ttbar_leta")) tree->Branch("ttbar_leta" ,  ttbar_leta  , "ttbar_leta[ttbar_nl]/F");
      if(variableParser.isToBeStored("ttbar_lphi")) tree->Branch("ttbar_lphi" ,  ttbar_lphi  , "ttbar_lphi[ttbar_nl]/F");
      if(variableParser.isToBeStored("ttbar_lm")) tree->Branch("ttbar_lm"   ,  ttbar_lm    , "ttbar_lm[ttbar_nl]/F");
      if(variableParser.isToBeStored("ttbar_lid")) tree->Branch("ttbar_lid"  ,  ttbar_lid   , "ttbar_lid[ttbar_nl]/I");
      if(variableParser.isToBeStored("ttbar_lgid")) tree->Branch("ttbar_lgid" ,  ttbar_lgid  , "ttbar_lgid[ttbar_nl]/I");
      if(variableParser.isToBeStored("ttbar_lch")) tree->Branch("ttbar_lch"  ,  ttbar_lch   , "ttbar_lch[ttbar_nl]/I");
      if(variableParser.isToBeStored("ttbar_metpt")) tree->Branch("ttbar_metpt",  &ttbar_metpt,  "ttbar_metpt/F");
      if(variableParser.isToBeStored("ttbar_metphi")) tree->Branch("ttbar_metphi", &ttbar_metphi, "ttbar_metphi/F");
      if(variableParser.isToBeStored("ttbar_nw")) tree->Branch("ttbar_nw"  ,  &ttbar_nw    , "ttbar_nw/I");
      if(variableParser.isToBeStored("ttbar_w")) tree->Branch("ttbar_w"    ,  ttbar_w     , "ttbar_w[ttbar_nw]/F");
      if(variableParser.isToBeStored("ttbar_ptweight")) tree->Branch("ttbar_ptweight", &ttbar_ptweight, "ttbar_ptweight/F");

      if(variableParser.isToBeStored("nPatMuon")) tree->Branch("nPatMuon", &nPatMuon, "nPatMuon/I");
      if(variableParser.isToBeStored("PatMuon_pt")) tree->Branch("PatMuon_pt", PatMuon_pt, "PatMuon_pt[nPatMuon]/F");
      if(variableParser.isToBeStored("PatMuon_eta")) tree->Branch("PatMuon_eta", PatMuon_eta, "PatMuon_eta[nPatMuon]/F");
      if(variableParser.isToBeStored("PatMuon_phi")) tree->Branch("PatMuon_phi", PatMuon_phi, "PatMuon_phi[nPatMuon]/F");
      if(variableParser.isToBeStored("PatMuon_isSoftMuon")) tree->Branch("PatMuon_isSoftMuon", PatMuon_isSoftMuon, "PatMuon_isSoftMuon[nPatMuon]/I");
      if(variableParser.isToBeStored("PatMuon_isMediumMuon")) tree->Branch("PatMuon_isMediumMuon", PatMuon_isMediumMuon, "PatMuon_isMediumMuon[nPatMuon]/O");
      if(variableParser.isToBeStored("PatMuon_isTightMuon")) tree->Branch("PatMuon_isTightMuon", PatMuon_isTightMuon, "PatMuon_isTightMuon[nPatMuon]/I");
      if(variableParser.isToBeStored("PatMuon_iso")) tree->Branch("PatMuon_iso", PatMuon_iso, "PatMuon_iso[nPatMuon]/F");
      if(variableParser.isToBeStored("PatMuon_isoTrackerOnly")) tree->Branch("PatMuon_isoTrackerOnly", PatMuon_isoTrackerOnly, "PatMuon_isoTrackerOnly[nPatMuon]/F");
      if(variableParser.isToBeStored("PatMuon_IP")) tree->Branch("PatMuon_IP", PatMuon_IP, "PatMuon_IP[nPatMuon]/F");
      if(variableParser.isToBeStored("PatMuon_IPsig")) tree->Branch("PatMuon_IPsig", PatMuon_IPsig, "PatMuon_IPsig[nPatMuon]/F");
      if(variableParser.isToBeStored("PatMuon_IP2D")) tree->Branch("PatMuon_IP2D", PatMuon_IP2D, "PatMuon_IP2D[nPatMuon]/F");
      if(variableParser.isToBeStored("PatMuon_IP2Dsig")) tree->Branch("PatMuon_IP2Dsig", PatMuon_IP2Dsig, "PatMuon_IP2Dsig[nPatMuon]/F");


      if(variableParser.isToBeStored("nPatElec")) tree->Branch("nPatElec", &nPatElec, "nPatElec/I");
      if(variableParser.isToBeStored("PatElec_pt")) tree->Branch("PatElec_pt", PatElec_pt, "PatElec_pt[nPatElec]/F");
      if(variableParser.isToBeStored("PatElec_eta")) tree->Branch("PatElec_eta", PatElec_eta, "PatElec_eta[nPatElec]/F");
      if(variableParser.isToBeStored("PatElec_superClusterEta")) tree->Branch("PatElec_superClusterEta", PatElec_superClusterEta, "PatElec_superClusterEta[nPatElec]/F");
      if(variableParser.isToBeStored("PatElec_phi")) tree->Branch("PatElec_phi", PatElec_phi, "PatElec_phi[nPatElec]/F");
      if(variableParser.isToBeStored("PatElec_isLooseElec")) tree->Branch("PatElec_isLooseElec", PatElec_isLooseElec, "PatElec_isLooseElec[nPatElec]/I");
      if(variableParser.isToBeStored("PatElec_isMediumElec")) tree->Branch("PatElec_isMediumElec", PatElec_isMediumElec, "PatElec_isMediumElec[nPatElec]/I");
      if(variableParser.isToBeStored("PatElec_isTightElec")) tree->Branch("PatElec_isTightElec", PatElec_isTightElec, "PatElec_isTightElec[nPatElec]/I");

       if(variableParser.isToBeStored("PatElec_sumChargedHadronPt")) tree->Branch("PatElec_sumChargedHadronPt", PatElec_sumChargedHadronPt ,  "PatElec_sumChargedHadronPt[nPatElec]/F");
       if(variableParser.isToBeStored("PatElec_sumNeutralHadronEt")) tree->Branch("PatElec_sumNeutralHadronEt",	PatElec_sumNeutralHadronEt ,  "PatElec_sumNeutralHadronEt[nPatElec]/F");
       if(variableParser.isToBeStored("PatElec_sumPhotonEt"       )) tree->Branch("PatElec_sumPhotonEt"       ,	PatElec_sumPhotonEt        ,  "PatElec_sumPhotonEt[nPatElec]/F"       );
       if(variableParser.isToBeStored("PatElec_sumPUPt"           )) tree->Branch("PatElec_sumPUPt"           ,	PatElec_sumPUPt            ,  "PatElec_sumPUPt[nPatElec]/F"           );

       if(variableParser.isToBeStored("nL1_BarrelTracks")) tree->Branch(("nL1_BarrelTracks")           ,&nL1_BarrelTracks          ,("nL1_BarrelTracks/I"));
       if(variableParser.isToBeStored("L1_BarrelTrack_pt")) tree->Branch(("L1_BarrelTrack_pt")           ,&L1_BarrelTrack_pt          ,("L1_BarrelTrack_pt[nL1_BarrelTracks]/F"));
       if(variableParser.isToBeStored("L1_BarrelTrack_eta")) tree->Branch(("L1_BarrelTrack_eta")           ,&L1_BarrelTrack_eta          ,("L1_BarrelTrack_eta[nL1_BarrelTracks]/F"));
       if(variableParser.isToBeStored("L1_BarrelTrack_phi")) tree->Branch(("L1_BarrelTrack_phi")           ,&L1_BarrelTrack_phi          ,("L1_BarrelTrack_phi[nL1_BarrelTracks]/F"));
       if(variableParser.isToBeStored("L1_BarrelTrack_m")) tree->Branch(("L1_BarrelTrack_m")           ,&L1_BarrelTrack_m          ,("L1_BarrelTrack_m[nL1_BarrelTracks]/F"));
       if(variableParser.isToBeStored("L1_BarrelTrack_dz")) tree->Branch(("L1_BarrelTrack_dz")           ,&L1_BarrelTrack_dz          ,("L1_BarrelTrack_dz[nL1_BarrelTracks]/F"));
       if(variableParser.isToBeStored("L1_BarrelTrack_dxy")) tree->Branch(("L1_BarrelTrack_dxy")           ,&L1_BarrelTrack_dxy          ,("L1_BarrelTrack_dxy[nL1_BarrelTracks]/F"));
       if(variableParser.isToBeStored("nL1_HGCalTracks")) tree->Branch(("nL1_HGCalTracks")           ,&nL1_HGCalTracks          ,("nL1_HGCalTracks/I"));
       if(variableParser.isToBeStored("L1_HGCalTrack_pt")) tree->Branch(("L1_HGCalTrack_pt")           ,&L1_HGCalTrack_pt          ,("L1_HGCalTrack_pt[nL1_HGCalTracks]/F"));
       if(variableParser.isToBeStored("L1_HGCalTrack_eta")) tree->Branch(("L1_HGCalTrack_eta")           ,&L1_HGCalTrack_eta          ,("L1_HGCalTrack_eta[nL1_HGCalTracks]/F"));
       if(variableParser.isToBeStored("L1_HGCalTrack_phi")) tree->Branch(("L1_HGCalTrack_phi")           ,&L1_HGCalTrack_phi          ,("L1_HGCalTrack_phi[nL1_HGCalTracks]/F"));
       if(variableParser.isToBeStored("L1_HGCalTrack_m")) tree->Branch(("L1_HGCalTrack_m")           ,&L1_HGCalTrack_m          ,("L1_HGCalTrack_m[nL1_HGCalTracks]/F"));
       if(variableParser.isToBeStored("L1_HGCalTrack_dz")) tree->Branch(("L1_HGCalTrack_dz")           ,&L1_HGCalTrack_dz          ,("L1_HGCalTrack_dz[nL1_HGCalTracks]/F"));
       if(variableParser.isToBeStored("L1_HGCalTrack_dxy")) tree->Branch(("L1_HGCalTrack_dxy")           ,&L1_HGCalTrack_dxy          ,("L1_HGCalTrack_dxy[nL1_HGCalTracks]/F"));
       if(variableParser.isToBeStored("nL1_Tracks")) tree->Branch(("nL1_Tracks")           ,&nL1_Tracks          ,("nL1_Tracks/I"));
       if(variableParser.isToBeStored("L1_Track_pt")) tree->Branch(("L1_Track_pt")           ,&L1_Track_pt          ,("L1_Track_pt[nL1_Tracks]/F"));
       if(variableParser.isToBeStored("L1_Track_eta")) tree->Branch(("L1_Track_eta")           ,&L1_Track_eta          ,("L1_Track_eta[nL1_Tracks]/F"));
       if(variableParser.isToBeStored("L1_Track_phi")) tree->Branch(("L1_Track_phi")           ,&L1_Track_phi          ,("L1_Track_phi[nL1_Tracks]/F"));
       if(variableParser.isToBeStored("L1_Track_m")) tree->Branch(("L1_Track_m")           ,&L1_Track_m          ,("L1_Track_m[nL1_Tracks]/F"));
       if(variableParser.isToBeStored("L1_Track_dz")) tree->Branch(("L1_Track_dz")           ,&L1_Track_dz          ,("L1_Track_dz[nL1_Tracks]/F"));
       if(variableParser.isToBeStored("L1_Track_dxy")) tree->Branch(("L1_Track_dxy")           ,&L1_Track_dxy          ,("L1_Track_dxy[nL1_Tracks]/F"));
       if(variableParser.isToBeStored("nL1_ExtendedTracks")) tree->Branch(("nL1_ExtendedTracks")           ,&nL1_ExtendedTracks          ,("nL1_ExtendedTracks/I"));
       if(variableParser.isToBeStored("L1_ExtendedTrack_pt")) tree->Branch(("L1_ExtendedTrack_pt")           ,&L1_ExtendedTrack_pt          ,("L1_ExtendedTrack_pt[nL1_ExtendedTracks]/F"));
       if(variableParser.isToBeStored("L1_ExtendedTrack_eta")) tree->Branch(("L1_ExtendedTrack_eta")           ,&L1_ExtendedTrack_eta          ,("L1_ExtendedTrack_eta[nL1_ExtendedTracks]/F"));
       if(variableParser.isToBeStored("L1_ExtendedTrack_phi")) tree->Branch(("L1_ExtendedTrack_phi")           ,&L1_ExtendedTrack_phi          ,("L1_ExtendedTrack_phi[nL1_ExtendedTracks]/F"));
       if(variableParser.isToBeStored("L1_ExtendedTrack_m")) tree->Branch(("L1_ExtendedTrack_m")           ,&L1_ExtendedTrack_m          ,("L1_ExtendedTrack_m[nL1_ExtendedTracks]/F"));
       if(variableParser.isToBeStored("L1_ExtendedTrack_dz")) tree->Branch(("L1_ExtendedTrack_dz")           ,&L1_ExtendedTrack_dz          ,("L1_ExtendedTrack_dz[nL1_ExtendedTracks]/F"));
       if(variableParser.isToBeStored("L1_ExtendedTrack_dxy")) tree->Branch(("L1_ExtendedTrack_dxy")           ,&L1_ExtendedTrack_dxy          ,("L1_ExtendedTrack_dxy[nL1_ExtendedTracks]/F"));

       if(variableParser.isToBeStored("nL1_Vertices")) tree->Branch(("nL1_Vertices")           ,&nL1_Vertices          ,("nL1_Vertices/I"));
       if(variableParser.isToBeStored("L1_Vertex_z")) tree->Branch(("L1_Vertex_z")           ,&L1_Vertex_z          ,("L1_Vertex_z[nL1_Vertices]/F"));
       if(variableParser.isToBeStored("L1_Vertex_sum")) tree->Branch(("L1_Vertex_sum")           ,&L1_Vertex_sum          ,("L1_Vertex_sum[nL1_Vertices]/F"));

       if(variableParser.isToBeStored("nL1_PFJets")) tree->Branch(("nL1_PFJets")           ,&nL1_PFJets          ,("nL1_PFJets/I"));
       if(variableParser.isToBeStored("L1_PFJets_pt")) tree->Branch(("L1_PFJets_pt")           ,&L1_PFJets_pt          ,("L1_PFJets_pt[nL1_PFJets]/F"));
       if(variableParser.isToBeStored("L1_PFJets_eta")) tree->Branch(("L1_PFJets_eta")           ,&L1_PFJets_eta          ,("L1_PFJets_eta[nL1_PFJets]/F"));
       if(variableParser.isToBeStored("L1_PFJets_phi")) tree->Branch(("L1_PFJets_phi")           ,&L1_PFJets_phi          ,("L1_PFJets_phi[nL1_PFJets]/F"));
       if(variableParser.isToBeStored("L1_PFJets_m")) tree->Branch(("L1_PFJets_m")           ,&L1_PFJets_m          ,("L1_PFJets_m[nL1_PFJets]/F"));
       if(variableParser.isToBeStored("L1_PFJets_dxy")) tree->Branch(("L1_PFJets_dxy")           ,&L1_PFJets_dxy          ,("L1_PFJets_dxy[nL1_PFJets]/F"));
       if(variableParser.isToBeStored("L1_PFJets_dz")) tree->Branch(("L1_PFJets_dz")           ,&L1_PFJets_dz          ,("L1_PFJets_dz[nL1_PFJets]/F"));
       if(variableParser.isToBeStored("nL1_PuppiJets")) tree->Branch(("nL1_PuppiJets")           ,&nL1_PuppiJets          ,("nL1_PuppiJets/I"));
       if(variableParser.isToBeStored("L1_PuppiJets_pt")) tree->Branch(("L1_PuppiJets_pt")           ,&L1_PuppiJets_pt          ,("L1_PuppiJets_pt[nL1_PuppiJets]/F"));
       if(variableParser.isToBeStored("L1_PuppiJets_eta")) tree->Branch(("L1_PuppiJets_eta")           ,&L1_PuppiJets_eta          ,("L1_PuppiJets_eta[nL1_PuppiJets]/F"));
       if(variableParser.isToBeStored("L1_PuppiJets_phi")) tree->Branch(("L1_PuppiJets_phi")           ,&L1_PuppiJets_phi          ,("L1_PuppiJets_phi[nL1_PuppiJets]/F"));
       if(variableParser.isToBeStored("L1_PuppiJets_m")) tree->Branch(("L1_PuppiJets_m")           ,&L1_PuppiJets_m          ,("L1_PuppiJets_m[nL1_PuppiJets]/F"));
       if(variableParser.isToBeStored("L1_PuppiJets_dxy")) tree->Branch(("L1_PuppiJets_dxy")           ,&L1_PuppiJets_dxy          ,("L1_PuppiJets_dxy[nL1_PuppiJets]/F"));
       if(variableParser.isToBeStored("L1_PuppiJets_dz")) tree->Branch(("L1_PuppiJets_dz")           ,&L1_PuppiJets_dz          ,("L1_PuppiJets_dz[nL1_PuppiJets]/F"));

       if(variableParser.isToBeStored("L1_HT_pt")) tree->Branch(("L1_HT_pt")           ,&L1_HT_pt          ,("L1_HT_pt/F"));
       if(variableParser.isToBeStored("L1_HT_phi")) tree->Branch(("L1_HT_phi")           ,&L1_HT_phi          ,("L1_HT_phi/F"));
       if(variableParser.isToBeStored("L1_HT_sumEt")) tree->Branch(("L1_HT_sumEt")           ,&L1_HT_sumEt          ,("L1_HT_sumEt/F"));

       if(variableParser.isToBeStored("HLT_HT_2p4_pt")) tree->Branch(("HLT_HT_2p4_pt")           ,&HLT_HT_2p4_pt          ,("HLT_HT_2p4_pt/F"));
       if(variableParser.isToBeStored("HLT_HT_2p4_phi")) tree->Branch(("HLT_HT_2p4_phi")           ,&HLT_HT_2p4_phi          ,("HLT_HT_2p4_phi/F"));
       if(variableParser.isToBeStored("HLT_HT_2p4_sumEt")) tree->Branch(("HLT_HT_2p4_sumEt")           ,&HLT_HT_2p4_sumEt          ,("HLT_HT_2p4_sumEt/F"));
       if(variableParser.isToBeStored("HLT_HT_4p0_pt")) tree->Branch(("HLT_HT_4p0_pt")           ,&HLT_HT_4p0_pt          ,("HLT_HT_4p0_pt/F"));
       if(variableParser.isToBeStored("HLT_HT_4p0_phi")) tree->Branch(("HLT_HT_4p0_phi")           ,&HLT_HT_4p0_phi          ,("HLT_HT_4p0_phi/F"));
       if(variableParser.isToBeStored("HLT_HT_4p0_sumEt")) tree->Branch(("HLT_HT_4p0_sumEt")           ,&HLT_HT_4p0_sumEt          ,("HLT_HT_4p0_sumEt/F"));
       if(variableParser.isToBeStored("HLT_HT_jme_pt")) tree->Branch(("HLT_HT_jme_pt")           ,&HLT_HT_jme_pt          ,("HLT_HT_jme_pt/F"));
       if(variableParser.isToBeStored("HLT_HT_jme_phi")) tree->Branch(("HLT_HT_jme_phi")           ,&HLT_HT_jme_phi          ,("HLT_HT_jme_phi/F"));
       if(variableParser.isToBeStored("HLT_HT_jme_sumEt")) tree->Branch(("HLT_HT_jme_sumEt")           ,&HLT_HT_jme_sumEt          ,("HLT_HT_jme_sumEt/F"));
    }

    void ReadBranches(TTree *tree, VariableParser variableParser){
      if(variableParser.isToBeStored("nBitTrigger")) tree->SetBranchAddress("nBitTrigger", &nBitTrigger);
      if(variableParser.isToBeStored("BitTrigger")) tree->SetBranchAddress("BitTrigger" , BitTrigger  );
      if(variableParser.isToBeStored("Run")) tree->SetBranchAddress("Run"        , &Run        );
      if(variableParser.isToBeStored("Evt")) tree->SetBranchAddress("Evt"        , &Evt        );
      if(variableParser.isToBeStored("LumiBlock")) tree->SetBranchAddress("LumiBlock"  , &LumiBlock  );
      if(variableParser.isToBeStored("pthat")) tree->SetBranchAddress("pthat"      , &pthat      );
      if(variableParser.isToBeStored("mcweight")) tree->SetBranchAddress("mcweight"   , &mcweight   );
      if(variableParser.isToBeStored("qcdWeightPU140")) tree->SetBranchAddress("qcdWeightPU140"   , &qcdWeightPU140   );
      if(variableParser.isToBeStored("qcdWeightPU200")) tree->SetBranchAddress("qcdWeightPU200"   , &qcdWeightPU200   );
      if(variableParser.isToBeStored("HepMCGenEvent_scale")) tree->SetBranchAddress("HepMCGenEvent_scale"   , &HepMCGenEvent_scale   );
      if(variableParser.isToBeStored("GenEventInfo_qScale")) tree->SetBranchAddress("GenEventInfo_qScale"   , &GenEventInfo_qScale   );
      if(variableParser.isToBeStored("pileupInfo_BX0_numPUInteractions")) tree->SetBranchAddress("pileupInfo_BX0_numPUInteractions"   , &pileupInfo_BX0_numPUInteractions   );
      if(variableParser.isToBeStored("pileupInfo_BX0_numTrueInteractions")) tree->SetBranchAddress("pileupInfo_BX0_numTrueInteractions"   , &pileupInfo_BX0_numTrueInteractions   );
      if(variableParser.isToBeStored("pileupInfo_BX0_max_pT_hats")) tree->SetBranchAddress("pileupInfo_BX0_max_pT_hats"   , &pileupInfo_BX0_max_pT_hats   );
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat000to020")) tree->SetBranchAddress("pileupInfo_BX0_n_pThat000to020"   , &pileupInfo_BX0_n_pThat000to020   );
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat020to030")) tree->SetBranchAddress("pileupInfo_BX0_n_pThat020to030"   , &pileupInfo_BX0_n_pThat020to030   );
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat030to050")) tree->SetBranchAddress("pileupInfo_BX0_n_pThat030to050"   , &pileupInfo_BX0_n_pThat030to050   );
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat050to080")) tree->SetBranchAddress("pileupInfo_BX0_n_pThat050to080"   , &pileupInfo_BX0_n_pThat050to080   );
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat080to120")) tree->SetBranchAddress("pileupInfo_BX0_n_pThat080to120"   , &pileupInfo_BX0_n_pThat080to120   );
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat120to170")) tree->SetBranchAddress("pileupInfo_BX0_n_pThat120to170"   , &pileupInfo_BX0_n_pThat120to170   );
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat170to300")) tree->SetBranchAddress("pileupInfo_BX0_n_pThat170to300"   , &pileupInfo_BX0_n_pThat170to300   );
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat300to470")) tree->SetBranchAddress("pileupInfo_BX0_n_pThat300to470"   , &pileupInfo_BX0_n_pThat300to470   );
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat470to600")) tree->SetBranchAddress("pileupInfo_BX0_n_pThat470to600"   , &pileupInfo_BX0_n_pThat470to600   );
      if(variableParser.isToBeStored("pileupInfo_BX0_n_pThat600toInf")) tree->SetBranchAddress("pileupInfo_BX0_n_pThat600toInf"   , &pileupInfo_BX0_n_pThat600toInf   );
      if(variableParser.isToBeStored("BX")) tree->SetBranchAddress("BX"         , &BX         );
      if(variableParser.isToBeStored("nPV")) tree->SetBranchAddress("nPV"        , &nPV        );
      if(variableParser.isToBeStored("PVz")) tree->SetBranchAddress("PVz"        , &PVz        );
      if(variableParser.isToBeStored("PVez")) tree->SetBranchAddress("PVez"       , &PVez       );
      if(variableParser.isToBeStored("GenPVz")) tree->SetBranchAddress("GenPVz"     , &GenPVz     );
      if(variableParser.isToBeStored("rho")) tree->SetBranchAddress("rho"        , &rho        );
      if(variableParser.isToBeStored("nPUtrue")) tree->SetBranchAddress("nPUtrue"      , &nPUtrue     );
      if(variableParser.isToBeStored("nPU")) tree->SetBranchAddress("nPU"          , &nPU         );
      if(variableParser.isToBeStored("PU_bunch")) tree->SetBranchAddress("PU_bunch"     , PU_bunch     );
      if(variableParser.isToBeStored("PU_z")) tree->SetBranchAddress("PU_z"         , PU_z         );
      if(variableParser.isToBeStored("PU_sumpT_low")) tree->SetBranchAddress("PU_sumpT_low" , PU_sumpT_low );
      if(variableParser.isToBeStored("PU_sumpT_high")) tree->SetBranchAddress("PU_sumpT_high", PU_sumpT_high);
      if(variableParser.isToBeStored("PU_ntrks_low")) tree->SetBranchAddress("PU_ntrks_low" , PU_ntrks_low );
      if(variableParser.isToBeStored("PU_ntrks_high")) tree->SetBranchAddress("PU_ntrks_high", PU_ntrks_high);

      if(variableParser.isToBeStored("ncQuarks")) tree->SetBranchAddress("ncQuarks"      , &ncQuarks     );
      if(variableParser.isToBeStored("cQuark_pT")) tree->SetBranchAddress("cQuark_pT"     , cQuark_pT     );
      if(variableParser.isToBeStored("cQuark_eta")) tree->SetBranchAddress("cQuark_eta"    , cQuark_eta    );
      if(variableParser.isToBeStored("cQuark_phi")) tree->SetBranchAddress("cQuark_phi"    , cQuark_phi    );
      if(variableParser.isToBeStored("cQuark_pdgID")) tree->SetBranchAddress("cQuark_pdgID"  , cQuark_pdgID  );
      if(variableParser.isToBeStored("cQuark_status")) tree->SetBranchAddress("cQuark_status" , cQuark_status );
      if(variableParser.isToBeStored("cQuark_fromGSP")) tree->SetBranchAddress("cQuark_fromGSP", cQuark_fromGSP);

      if(variableParser.isToBeStored("nbQuarks")) tree->SetBranchAddress("nbQuarks",          &nbQuarks     );
      if(variableParser.isToBeStored("bQuark_pT")) tree->SetBranchAddress("bQuark_pT",         bQuark_pT     );
      if(variableParser.isToBeStored("bQuark_eta")) tree->SetBranchAddress("bQuark_eta",        bQuark_eta    );
      if(variableParser.isToBeStored("bQuark_phi")) tree->SetBranchAddress("bQuark_phi",        bQuark_phi    );
      if(variableParser.isToBeStored("bQuark_pdgID")) tree->SetBranchAddress("bQuark_pdgID",      bQuark_pdgID  );
      if(variableParser.isToBeStored("bQuark_status")) tree->SetBranchAddress("bQuark_status",     bQuark_status );
      if(variableParser.isToBeStored("bQuark_fromGSP")) tree->SetBranchAddress("bQuark_fromGSP",    bQuark_fromGSP);

      if(variableParser.isToBeStored("nBHadrons")) tree->SetBranchAddress("nBHadrons",          &nBHadrons            );
      if(variableParser.isToBeStored("BHadron_pT")) tree->SetBranchAddress("BHadron_pT",           BHadron_pT          );
      if(variableParser.isToBeStored("BHadron_eta")) tree->SetBranchAddress("BHadron_eta",          BHadron_eta         );
      if(variableParser.isToBeStored("BHadron_phi")) tree->SetBranchAddress("BHadron_phi",          BHadron_phi         );
      if(variableParser.isToBeStored("BHadron_mass")) tree->SetBranchAddress("BHadron_mass",         BHadron_mass        );
      if(variableParser.isToBeStored("BHadron_pdgID")) tree->SetBranchAddress("BHadron_pdgID",        BHadron_pdgID       );
      if(variableParser.isToBeStored("BHadron_mother")) tree->SetBranchAddress("BHadron_mother",       BHadron_mother      );
      if(variableParser.isToBeStored("BHadron_hasBdaughter")) tree->SetBranchAddress("BHadron_hasBdaughter", BHadron_hasBdaughter);
      if(variableParser.isToBeStored("BHadron_SVx")) tree->SetBranchAddress("BHadron_SVx",          BHadron_SVx         );
      if(variableParser.isToBeStored("BHadron_SVy")) tree->SetBranchAddress("BHadron_SVy",          BHadron_SVy         );
      if(variableParser.isToBeStored("BHadron_SVz")) tree->SetBranchAddress("BHadron_SVz",          BHadron_SVz         );
      if(variableParser.isToBeStored("BHadron_nCharged")) tree->SetBranchAddress("BHadron_nCharged",     BHadron_nCharged    );
      if(variableParser.isToBeStored("BHadron_DHadron1")) tree->SetBranchAddress("BHadron_DHadron1",     BHadron_DHadron1    );
      if(variableParser.isToBeStored("BHadron_DHadron2")) tree->SetBranchAddress("BHadron_DHadron2",     BHadron_DHadron2    );

      if(variableParser.isToBeStored("nDHadrons")) tree->SetBranchAddress("nDHadrons",    &nDHadrons    );
      if(variableParser.isToBeStored("nDaughters")) tree->SetBranchAddress("nDaughters",   &nDaughters   );
      if(variableParser.isToBeStored("DHadron_pT")) tree->SetBranchAddress("DHadron_pT",    DHadron_pT    );
      if(variableParser.isToBeStored("DHadron_eta")) tree->SetBranchAddress("DHadron_eta",   DHadron_eta   );
      if(variableParser.isToBeStored("DHadron_phi")) tree->SetBranchAddress("DHadron_phi",   DHadron_phi   );
      if(variableParser.isToBeStored("DHadron_pdgID")) tree->SetBranchAddress("DHadron_pdgID", DHadron_pdgID );
      if(variableParser.isToBeStored("DHadron_mass")) tree->SetBranchAddress("DHadron_mass",  DHadron_mass  );
      if(variableParser.isToBeStored("DHadron_SVx")) tree->SetBranchAddress("DHadron_SVx",   DHadron_SVx   );
      if(variableParser.isToBeStored("DHadron_SVy")) tree->SetBranchAddress("DHadron_SVy",   DHadron_SVy   );
      if(variableParser.isToBeStored("DHadron_SVz")) tree->SetBranchAddress("DHadron_SVz",   DHadron_SVz   );
      if(variableParser.isToBeStored("DHadron_nDaughters")) tree->SetBranchAddress("DHadron_nDaughters",         DHadron_nDaughters        );
      if(variableParser.isToBeStored("DHadron_DaughtersPdgID")) tree->SetBranchAddress("DHadron_DaughtersPdgID",     DHadron_DaughtersPdgID    );
      if(variableParser.isToBeStored("DHadron_nChargedDaughters")) tree->SetBranchAddress("DHadron_nChargedDaughters",  DHadron_nChargedDaughters );
      if(variableParser.isToBeStored("DHadron_nCharged")) tree->SetBranchAddress("DHadron_nCharged", DHadron_nCharged );

      if(variableParser.isToBeStored("nGenlep")) tree->SetBranchAddress("nGenlep",     &nGenlep       );
      if(variableParser.isToBeStored("Genlep_pT")) tree->SetBranchAddress("Genlep_pT",     Genlep_pT    );
      if(variableParser.isToBeStored("Genlep_eta")) tree->SetBranchAddress("Genlep_eta",    Genlep_eta   );
      if(variableParser.isToBeStored("Genlep_phi")) tree->SetBranchAddress("Genlep_phi",    Genlep_phi   );
      if(variableParser.isToBeStored("Genlep_pdgID")) tree->SetBranchAddress("Genlep_pdgID",  Genlep_pdgID );
      if(variableParser.isToBeStored("Genlep_status")) tree->SetBranchAddress("Genlep_status", Genlep_status);
      if(variableParser.isToBeStored("Genlep_mother")) tree->SetBranchAddress("Genlep_mother", Genlep_mother);

      if(variableParser.isToBeStored("nGenquark")) tree->SetBranchAddress("nGenquark",     &nGenquark       );
      if(variableParser.isToBeStored("Genquark_pT")) tree->SetBranchAddress("Genquark_pT",     Genquark_pT    );
      if(variableParser.isToBeStored("Genquark_eta")) tree->SetBranchAddress("Genquark_eta",    Genquark_eta   );
      if(variableParser.isToBeStored("Genquark_phi")) tree->SetBranchAddress("Genquark_phi",    Genquark_phi   );
      if(variableParser.isToBeStored("Genquark_pdgID")) tree->SetBranchAddress("Genquark_pdgID",  Genquark_pdgID );
      if(variableParser.isToBeStored("Genquark_mother")) tree->SetBranchAddress("Genquark_mother", Genquark_mother);

      if(variableParser.isToBeStored("nGenJets")) tree->SetBranchAddress("nGenJets",     &nGenJets       );
      if(variableParser.isToBeStored("GenJet_pT")) tree->SetBranchAddress("GenJet_pT",     GenJet_pT   );
      if(variableParser.isToBeStored("GenJet_eta")) tree->SetBranchAddress("GenJet_eta",    GenJet_eta   );
      if(variableParser.isToBeStored("GenJet_phi")) tree->SetBranchAddress("GenJet_phi",    GenJet_phi   );
      if(variableParser.isToBeStored("GenJet_mass")) tree->SetBranchAddress("GenJet_mass",  GenJet_mass );

      if(variableParser.isToBeStored("nGenPruned")) tree->SetBranchAddress("nGenPruned",     &nGenPruned       );
      if(variableParser.isToBeStored("GenPruned_pT")) tree->SetBranchAddress("GenPruned_pT",     GenPruned_pT    );
      if(variableParser.isToBeStored("GenPruned_eta")) tree->SetBranchAddress("GenPruned_eta",    GenPruned_eta   );
      if(variableParser.isToBeStored("GenPruned_phi")) tree->SetBranchAddress("GenPruned_phi",    GenPruned_phi   );
      if(variableParser.isToBeStored("GenPruned_mass")) tree->SetBranchAddress("GenPruned_mass",    GenPruned_mass   );
      if(variableParser.isToBeStored("GenPruned_pdgID")) tree->SetBranchAddress("GenPruned_pdgID",  GenPruned_pdgID );
      if(variableParser.isToBeStored("GenPruned_status")) tree->SetBranchAddress("GenPruned_status", GenPruned_status);
      if(variableParser.isToBeStored("GenPruned_mother")) tree->SetBranchAddress("GenPruned_mother", GenPruned_mother);

      if(variableParser.isToBeStored("nGenV0")) tree->SetBranchAddress("nGenV0",        &nGenV0         );
      if(variableParser.isToBeStored("GenV0_pT")) tree->SetBranchAddress("GenV0_pT",        GenV0_pT       );
      if(variableParser.isToBeStored("GenV0_eta")) tree->SetBranchAddress("GenV0_eta",       GenV0_eta      );
      if(variableParser.isToBeStored("GenV0_phi")) tree->SetBranchAddress("GenV0_phi",       GenV0_phi      );
      if(variableParser.isToBeStored("GenV0_pdgID")) tree->SetBranchAddress("GenV0_pdgID",     GenV0_pdgID    );
      if(variableParser.isToBeStored("GenV0_SVx")) tree->SetBranchAddress("GenV0_SVx",       GenV0_SVx      );
      if(variableParser.isToBeStored("GenV0_SVy")) tree->SetBranchAddress("GenV0_SVy",       GenV0_SVy      );
      if(variableParser.isToBeStored("GenV0_SVz")) tree->SetBranchAddress("GenV0_SVz",       GenV0_SVz      );
      if(variableParser.isToBeStored("GenV0_nCharged")) tree->SetBranchAddress("GenV0_nCharged",  GenV0_nCharged );

      if(variableParser.isToBeStored("PV_x")) tree->SetBranchAddress("PV_x"     , PV_x     );
      if(variableParser.isToBeStored("PV_y")) tree->SetBranchAddress("PV_y"     , PV_y     );
      if(variableParser.isToBeStored("PV_z")) tree->SetBranchAddress("PV_z"     , PV_z     );
      if(variableParser.isToBeStored("PV_ex")) tree->SetBranchAddress("PV_ex"    , PV_ex    );
      if(variableParser.isToBeStored("PV_ey")) tree->SetBranchAddress("PV_ey"    , PV_ey    );
      if(variableParser.isToBeStored("PV_ez")) tree->SetBranchAddress("PV_ez"    , PV_ez    );
      if(variableParser.isToBeStored("PV_chi2")) tree->SetBranchAddress("PV_chi2"  , PV_chi2  );
      if(variableParser.isToBeStored("PV_ndf")) tree->SetBranchAddress("PV_ndf"   , PV_ndf   );
      if(variableParser.isToBeStored("PV_isgood")) tree->SetBranchAddress("PV_isgood", PV_isgood);
      if(variableParser.isToBeStored("PV_isfake")) tree->SetBranchAddress("PV_isfake", PV_isfake);

      if(variableParser.isToBeStored("nTrkAll")) tree->SetBranchAddress("nTrkAll",          &nTrkAll);
      if(variableParser.isToBeStored("TrkAll_d0")) tree->SetBranchAddress("TrkAll_d0",        TrkAll_d0);
      if(variableParser.isToBeStored("TrkAll_dz")) tree->SetBranchAddress("TrkAll_dz",        TrkAll_dz);
      if(variableParser.isToBeStored("TrkAll_p")) tree->SetBranchAddress("TrkAll_p",         TrkAll_p);
      if(variableParser.isToBeStored("TrkAll_pt")) tree->SetBranchAddress("TrkAll_pt",        TrkAll_pt);
      if(variableParser.isToBeStored("TrkAll_eta")) tree->SetBranchAddress("TrkAll_eta",       TrkAll_eta);
      if(variableParser.isToBeStored("TrkAll_phi")) tree->SetBranchAddress("TrkAll_phi",       TrkAll_phi);
      if(variableParser.isToBeStored("TrkAll_chi2")) tree->SetBranchAddress("TrkAll_chi2",      TrkAll_chi2);
      if(variableParser.isToBeStored("TrkAll_charge")) tree->SetBranchAddress("TrkAll_charge",    TrkAll_charge);
      if(variableParser.isToBeStored("TrkAll_nHitAll")) tree->SetBranchAddress("TrkAll_nHitAll",   TrkAll_nHitAll);
      if(variableParser.isToBeStored("TrkAll_nHitPixel")) tree->SetBranchAddress("TrkAll_nHitPixel", TrkAll_nHitPixel);
      if(variableParser.isToBeStored("TrkAll_nHitStrip")) tree->SetBranchAddress("TrkAll_nHitStrip", TrkAll_nHitStrip);
      if(variableParser.isToBeStored("TrkAll_nHitTIB")) tree->SetBranchAddress("TrkAll_nHitTIB",   TrkAll_nHitTIB);
      if(variableParser.isToBeStored("TrkAll_nHitTID")) tree->SetBranchAddress("TrkAll_nHitTID",   TrkAll_nHitTID);
      if(variableParser.isToBeStored("TrkAll_nHitTOB")) tree->SetBranchAddress("TrkAll_nHitTOB",   TrkAll_nHitTOB);
      if(variableParser.isToBeStored("TrkAll_nHitTEC")) tree->SetBranchAddress("TrkAll_nHitTEC",   TrkAll_nHitTEC);
      if(variableParser.isToBeStored("TrkAll_nHitPXB")) tree->SetBranchAddress("TrkAll_nHitPXB",   TrkAll_nHitPXB);
      if(variableParser.isToBeStored("TrkAll_nHitPXF")) tree->SetBranchAddress("TrkAll_nHitPXF",   TrkAll_nHitPXF);
      if(variableParser.isToBeStored("TrkAll_isHitL1")) tree->SetBranchAddress("TrkAll_isHitL1",   TrkAll_isHitL1);
      if(variableParser.isToBeStored("TrkAll_nSiLayers")) tree->SetBranchAddress("TrkAll_nSiLayers", TrkAll_nSiLayers);
      if(variableParser.isToBeStored("TrkAll_nPxLayers")) tree->SetBranchAddress("TrkAll_nPxLayers", TrkAll_nPxLayers);
      if(variableParser.isToBeStored("TrkAll_PV")) tree->SetBranchAddress("TrkAll_PV",        TrkAll_PV);
      if(variableParser.isToBeStored("TrkAll_PVweight")) tree->SetBranchAddress("TrkAll_PVweight",  TrkAll_PVweight);

      if(variableParser.isToBeStored("ttbar_chan")) tree->SetBranchAddress("ttbar_chan" , &ttbar_chan  );
      if(variableParser.isToBeStored("ttbar_trigWord")) tree->SetBranchAddress("ttbar_trigWord" , &ttbar_trigWord);
      if(variableParser.isToBeStored("ttbar_metfilterWord")) tree->SetBranchAddress("ttbar_metfilterWord" , &ttbar_metfilterWord);
      if(variableParser.isToBeStored("ttbar_allmepartons")) tree->SetBranchAddress("ttbar_allmepartons" , &ttbar_allmepartons);
      if(variableParser.isToBeStored("ttbar_matchmepartons")) tree->SetBranchAddress("ttbar_matchmepartons" , &ttbar_matchmepartons);
      if(variableParser.isToBeStored("ttbar_ng")) tree->SetBranchAddress("ttbar_ng"   , &ttbar_ng    );
      if(variableParser.isToBeStored("ttbar_gpt")) tree->SetBranchAddress("ttbar_gpt"  ,  ttbar_gpt   );
      if(variableParser.isToBeStored("ttbar_geta")) tree->SetBranchAddress("ttbar_geta" ,  ttbar_geta  );
      if(variableParser.isToBeStored("ttbar_gphi")) tree->SetBranchAddress("ttbar_gphi" ,  ttbar_gphi  );
      if(variableParser.isToBeStored("ttbar_gm")) tree->SetBranchAddress("ttbar_gm"   ,  ttbar_gm    );
      if(variableParser.isToBeStored("ttbar_gid")) tree->SetBranchAddress("ttbar_gid"  ,  ttbar_gid   );
      if(variableParser.isToBeStored("ttbar_nl")) tree->SetBranchAddress("ttbar_nl"   , &ttbar_nl    );
      if(variableParser.isToBeStored("ttbar_lpt")) tree->SetBranchAddress("ttbar_lpt"  ,  ttbar_lpt   );
      if(variableParser.isToBeStored("ttbar_leta")) tree->SetBranchAddress("ttbar_leta" ,  ttbar_leta  );
      if(variableParser.isToBeStored("ttbar_lphi")) tree->SetBranchAddress("ttbar_lphi" ,  ttbar_lphi  );
      if(variableParser.isToBeStored("ttbar_lm")) tree->SetBranchAddress("ttbar_lm"   ,  ttbar_lm    );
      if(variableParser.isToBeStored("ttbar_lid")) tree->SetBranchAddress("ttbar_lid"  ,  ttbar_lid   );
      if(variableParser.isToBeStored("ttbar_lgid")) tree->SetBranchAddress("ttbar_lgid" ,  ttbar_lgid  );
      if(variableParser.isToBeStored("ttbar_lch")) tree->SetBranchAddress("ttbar_lch"  ,  ttbar_lch   );
      if(variableParser.isToBeStored("ttbar_metpt")) tree->SetBranchAddress("ttbar_metpt",  &ttbar_metpt);
      if(variableParser.isToBeStored("ttbar_metphi")) tree->SetBranchAddress("ttbar_metphi", &ttbar_metphi);
      if(variableParser.isToBeStored("ttbar_nw")) tree->SetBranchAddress("ttbar_nw"  ,  &ttbar_nw    );
      if(variableParser.isToBeStored("ttbar_w")) tree->SetBranchAddress("ttbar_w"    ,  ttbar_w     );
      if(variableParser.isToBeStored("ttbar_ptweight")) tree->SetBranchAddress("ttbar_ptweight", &ttbar_ptweight);

      if(variableParser.isToBeStored("nPatMuon")) tree->SetBranchAddress("nPatMuon", &nPatMuon);
      if(variableParser.isToBeStored("PatMuon_pt")) tree->SetBranchAddress("PatMuon_pt", PatMuon_pt);
      if(variableParser.isToBeStored("PatMuon_eta")) tree->SetBranchAddress("PatMuon_eta", PatMuon_eta);
      if(variableParser.isToBeStored("PatMuon_phi")) tree->SetBranchAddress("PatMuon_phi", PatMuon_phi);
      if(variableParser.isToBeStored("PatMuon_isSoftMuon")) tree->SetBranchAddress("PatMuon_isSoftMuon", PatMuon_isSoftMuon);
      if(variableParser.isToBeStored("PatMuon_isMediumMuon")) tree->SetBranchAddress("PatMuon_isMediumMuon", PatMuon_isMediumMuon);
      if(variableParser.isToBeStored("PatMuon_isTightMuon")) tree->SetBranchAddress("PatMuon_isTightMuon", PatMuon_isTightMuon);
      if(variableParser.isToBeStored("PatMuon_iso")) tree->SetBranchAddress("PatMuon_iso", PatMuon_iso);
      if(variableParser.isToBeStored("PatMuon_isoTrackerOnly")) tree->SetBranchAddress("PatMuon_isoTrackerOnly", PatMuon_isoTrackerOnly);
      if(variableParser.isToBeStored("PatMuon_IP")) tree->SetBranchAddress("PatMuon_IP", PatMuon_IP);
      if(variableParser.isToBeStored("PatMuon_IPsig")) tree->SetBranchAddress("PatMuon_IPsig", PatMuon_IPsig);
      if(variableParser.isToBeStored("PatMuon_IP2D")) tree->SetBranchAddress("PatMuon_IP2D", PatMuon_IP2D);
      if(variableParser.isToBeStored("PatMuon_IP2Dsig")) tree->SetBranchAddress("PatMuon_IP2Dsig", PatMuon_IP2Dsig);

      if(variableParser.isToBeStored("nPatElec")) tree->SetBranchAddress("nPatElec", &nPatElec);
      if(variableParser.isToBeStored("PatElec_pt")) tree->SetBranchAddress("PatElec_pt", PatElec_pt);
      if(variableParser.isToBeStored("PatElec_eta")) tree->SetBranchAddress("PatElec_eta", PatElec_eta);
      if(variableParser.isToBeStored("PatElec_superClusterEta")) tree->SetBranchAddress("PatElec_superClusterEta", PatElec_superClusterEta);
      if(variableParser.isToBeStored("PatElec_phi")) tree->SetBranchAddress("PatElec_phi", PatElec_phi);
      if(variableParser.isToBeStored("PatElec_isLooseElec")) tree->SetBranchAddress("PatElec_isLooseElec", PatElec_isLooseElec);
      if(variableParser.isToBeStored("PatElec_isMediumElec")) tree->SetBranchAddress("PatElec_isMediumElec", PatElec_isMediumElec);
      if(variableParser.isToBeStored("PatElec_isTightElec")) tree->SetBranchAddress("PatElec_isTightElec", PatElec_isTightElec);
      if(variableParser.isToBeStored("PatElec_sumChargedHadronPt"))  tree->SetBranchAddress("PatElec_sumChargedHadronPt"  , PatElec_sumChargedHadronPt);
      if(variableParser.isToBeStored("PatElec_sumNeutralHadronEt"))  tree->SetBranchAddress("PatElec_sumNeutralHadronEt"  , PatElec_sumNeutralHadronEt);
      if(variableParser.isToBeStored("PatElec_sumPhotonEt"       ))  tree->SetBranchAddress("PatElec_sumPhotonEt"         , PatElec_sumPhotonEt);
      if(variableParser.isToBeStored("PatElec_sumPUPt"           ))  tree->SetBranchAddress("PatElec_sumPUPt"             , PatElec_sumPUPt);

    }

};

#endif
