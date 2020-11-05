
// -*- C++ -*-
//
// Package:    BTagHLTAnalyzerT
// Class:      BTagHLTAnalyzerT
//
/**\class BTagHLTAnalyzer BTagHLTAnalyzer.cc RecoBTag/PerformanceMeasurements/plugins/BTagHLTAnalyzer.cc

   Description: <one line class summary>

   Implementation:
   <Notes on implementation>
*/
//
// Original Author:  Andrea Jeremy
//         Created:  Thu Dec 20 10:00:00 CEST 2012
//
//
//
// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Common/interface/RefToPtr.h"
#include "DataFormats/JetReco/interface/JetTracksAssociation.h"
#include "DataFormats/BTauReco/interface/CandIPTagInfo.h"
#include "DataFormats/BTauReco/interface/ShallowTagInfo.h"
//#include "DataFormats/BTauReco/interface/CandSoftLeptonTagInfo.h"
#include "DataFormats/BTauReco/interface/BoostedDoubleSVTagInfo.h"
#include "DataFormats/BTauReco/interface/TrackIPTagInfo.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "DataFormats/GeometrySurface/interface/Line.h"
#include "DataFormats/GeometryCommonDetAlgo/interface/Measurement1D.h"

//#include "SimTracker/Records/interface/TrackAssociatorRecord.h"
//#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticle.h"

//#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
//#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "RecoBTag/PerformanceMeasurements/interface/CategoryFinder.h"

// reco track and vertex
#include "DataFormats/Candidate/interface/VertexCompositePtrCandidate.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"
#include "DataFormats/BTauReco/interface/JetTag.h"
#include "DataFormats/JetReco/interface/JetCollection.h"
#include "DataFormats/JetReco/interface/Jet.h"

#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHit.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHitFwd.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TFile.h"
#include "TTree.h"
#include "TVector3.h"
#include "TLorentzVector.h"
#include "Math/GenVector/VectorUtil.h"
#include "Math/GenVector/PxPyPzE4D.h"
#include "TGraphErrors.h"

#include "DataFormats/BTauReco/interface/SecondaryVertexTagInfo.h"
#include "DataFormats/BTauReco/interface/ParticleMasses.h"


//#include "SimDataFormats/Associations/interface/TrackToTrackingParticleAssociator.h"
//#include "SimTracker/TrackHistory/interface/TrackCategories.h"
//#include "SimTracker/TrackHistory/interface/TrackClassifier.h"
//#include "DataFormats/BTauReco/interface/SoftLeptonTagInfo.h"
//#include "DataFormats/BTauReco/interface/DeepFlavourFeatures.h"
//#include "DataFormats/BTauReco/interface/DeepDoubleXFeatures.h"
//#include "DataFormats/BTauReco/interface/DeepBoostedJetFeatures.h"
//#include "DataFormats/MuonReco/interface/Muon.h"
//#include "DataFormats/PatCandidates/interface/Electron.h"
//#include "DataFormats/PatCandidates/interface/MET.h"

// trigger
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Framework/interface/TriggerNamesService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

//#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "DataFormats/JetReco/interface/JetCollection.h"
//#include "DataFormats/JetReco/interface/GenJetCollection.h"
//#include "DataFormats/PatCandidates/interface/Jet.h"
//#include "DataFormats/PatCandidates/interface/Muon.h"

// reconstruct IP
#include "TrackingTools/IPTools/interface/IPTools.h"

// Math clusters to TrackingParticles
//#include "SimTracker/TrackerHitAssociation/interface/ClusterTPAssociation.h"

#include "RecoBTau/JetTagComputer/interface/GenericMVAJetTagComputer.h"
#include "RecoBTau/JetTagComputer/interface/GenericMVAJetTagComputerWrapper.h"
#include "RecoBTau/JetTagComputer/interface/JetTagComputer.h"
#include "RecoBTau/JetTagComputer/interface/JetTagComputerRecord.h"
#include "RecoBTag/SecondaryVertex/interface/CombinedSVComputer.h"
#include "RecoBTag/SecondaryVertex/interface/TrackKinematics.h"
#include "RecoBTag/SecondaryVertex/interface/V0Filter.h"
//#include "RecoBTag/ImpactParameter/plugins/IPProducer.h"
#include "RecoVertex/VertexPrimitives/interface/ConvertToFromReco.h"

#include "TrackingTools/GeomPropagators/interface/AnalyticalImpactPointExtrapolator.h"

#include "FWCore/Utilities/interface/RegexMatch.h"
#include <boost/regex.hpp>

#include "RecoBTag/PerformanceMeasurements/interface/JetInfoBranches.h"
#include "RecoBTag/PerformanceMeasurements/interface/EventInfoBranches.h"
//#include "RecoBTag/PerformanceMeasurements/interface/BookHistograms.h"
#include "RecoBTag/PerformanceMeasurements/interface/VariableParser.h"

//#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "FWCore/Common/interface/Provenance.h"
#include "PhysicsTools/SelectorUtils/interface/PFJetIDSelectionFunctor.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/IPTools/interface/IPTools.h"

//#include "fastjet/contrib/Njettiness.hh"

//#include "RecoBTag/SecondaryVertex/interface/CombinedSVSoftLeptonComputer.h"

//
// constants, enums and typedefs
//
typedef std::vector<reco::CaloJet> CaloJetCollection ;
typedef std::vector<reco::PFJet> PFJetCollection ;
typedef std::vector<reco::ShallowTagInfo> ShallowTagCollection ;
typedef edm::AssociationVector<edm::RefToBaseProd<reco::Jet>,std::vector<float> > HLTBTagValue;




namespace BTagHLT {
  const math::XYZPoint & position(const reco::Vertex & sv) {return sv.position();}
  const math::XYZPoint & position(const reco::VertexCompositePtrCandidate & sv) {return sv.vertex();}
  const double xError(const reco::Vertex & sv) {return sv.xError();}
  const double xError(const reco::VertexCompositePtrCandidate & sv) {return sqrt(sv.vertexCovariance(0,0));}
  const double yError(const reco::Vertex & sv) {return sv.yError();}
  const double yError(const reco::VertexCompositePtrCandidate & sv) {return sqrt(sv.vertexCovariance(1,1));}
  const double zError(const reco::Vertex & sv) {return sv.zError();}
  const double zError(const reco::VertexCompositePtrCandidate & sv) {return sqrt(sv.vertexCovariance(2,2));}
  const double chi2(const reco::Vertex & sv) {return sv.chi2();}
  const double chi2(const reco::VertexCompositePtrCandidate & sv) {return sv.vertexChi2();}
  const double ndof(const reco::Vertex & sv) {return sv.ndof();}
  const double ndof(const reco::VertexCompositePtrCandidate & sv) {return sv.vertexNdof();}
  const unsigned int vtxTracks(const reco::Vertex & sv) {return sv.nTracks();}
  const unsigned int vtxTracks(const reco::VertexCompositePtrCandidate & sv) {return sv.numberOfSourceCandidatePtrs();}


  const reco::TrackBaseRef toTrackRef(const reco::TrackRef & trk) {return reco::TrackBaseRef(trk);}
  const reco::TrackBaseRef toTrackRef(const edm::Ptr<reco::Candidate> & cnd)
    {
      const pat::PackedCandidate * pcand = dynamic_cast<const pat::PackedCandidate *>(cnd.get());
    
      if(pcand) // MiniAOD case
        return reco::TrackBaseRef(); // return null reference since no tracks are stored in MiniAOD
      else
      {
        const reco::PFCandidate * pfcand = dynamic_cast<const reco::PFCandidate *>(cnd.get());
    
        if ( (std::abs(pfcand->pdgId()) == 11 || pfcand->pdgId() == 22) && pfcand->gsfTrackRef().isNonnull() && pfcand->gsfTrackRef().isAvailable() )
          return reco::TrackBaseRef(pfcand->gsfTrackRef());
        else if ( pfcand->trackRef().isNonnull() && pfcand->trackRef().isAvailable() )
          return reco::TrackBaseRef(pfcand->trackRef());
        else
          return reco::TrackBaseRef();
      }
    }

}

template<typename IPTI,typename VTX>
class BTagHLTAnalyzerT : public edm::EDAnalyzer
{
public:
  explicit BTagHLTAnalyzerT(const edm::ParameterSet&);
  ~BTagHLTAnalyzerT();
  typedef IPTI IPTagInfo;
  typedef typename IPTI::input_container Tracks;
  typedef typename IPTI::input_container::value_type TrackRef;
  typedef typename edm::Ref<std::vector<reco::Track> > TrackRefCalo;
  typedef VTX Vertex;
  typedef reco::TemplatedSecondaryVertexTagInfo<IPTI,VTX> SVTagInfo;
  

private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  void vertexKinematicsAndChange(const Vertex & vertex, reco::TrackKinematics & vertexKinematics, Int_t & charge);
  void vertexKinematicsAndChange(const reco::Vertex & vertex, reco::TrackKinematics & vertexKinematics, Int_t & charge);

  template<typename JetColl>
  bool havePassingJets(const edm::Handle<JetColl>&);

  void setTracksPVBase(const reco::Track & track, const edm::Handle<reco::VertexCollection> & pvHandle, int & iPV, float & PVweight);

  void setTracksSV(const TrackRef & trackRef, const SVTagInfo *, int & isFromSV, int & iSV, float & SVweight);
  void setTracksSV(const TrackRefCalo & trackRef, const reco::SecondaryVertexTagInfo *, int & isFromSV, int & iSV, float & SVweight);

  bool NameCompatible(const std::string& pattern, const std::string& name);

  bool processTrig(const edm::Handle<edm::TriggerResults>&, const std::vector<std::string>&) ;

  template<typename JetColl, typename SVColl>
  void processHLTJets(const edm::Handle<JetColl>&,  const edm::EDGetTokenT<ShallowTagCollection>&,  const edm::EDGetTokenT<std::vector<SVColl> >&, 
		      const edm::EDGetTokenT<HLTBTagValue>&, const edm::EDGetTokenT<HLTBTagValue>&,
		      const edm::Event&, const edm::EventSetup&, const int) ;

  void processHLTPFJets(const edm::Handle<PFJetCollection>&, const edm::EDGetTokenT<ShallowTagCollection>&, 
			const edm::EDGetTokenT<HLTBTagValue>&, const edm::EDGetTokenT<HLTBTagValue>&,
			const edm::Event&, const edm::EventSetup&, const int) ;


  // ----------member data ---------------------------
  std::string outputFile_;
  //std::vector< std::string > moduleLabel_;

  edm::EDGetTokenT<edm::TriggerResults> triggerTable_;

  std::string   branchNamePrefix_;
  edm::EDGetTokenT<CaloJetCollection> CaloJetCollectionTag_;
  edm::EDGetTokenT<ShallowTagCollection> CaloJetTagCollectionTag_;
  edm::EDGetTokenT<std::vector<reco::SecondaryVertexTagInfo> > CaloSVCollectionTag_;
  edm::EDGetTokenT<HLTBTagValue> CaloJetCSVTag_;
  edm::EDGetTokenT<HLTBTagValue> CaloJetDeepCSVTag_;

  edm::EDGetTokenT<PFJetCollection> PFJetCollectionTag_;
  edm::EDGetTokenT<ShallowTagCollection> PFJetTagCollectionTag_;
  edm::EDGetTokenT<std::vector<SVTagInfo> > PFSVCollectionTag_;
  edm::EDGetTokenT<HLTBTagValue> PFJetCSVTag_;
  edm::EDGetTokenT<HLTBTagValue> PFJetDeepCSVTag_;

  edm::EDGetTokenT<reco::VertexCollection> primaryVertexColl_;

  TFile*  rootFile_;
  double minJetPt_;
  double maxJetEta_;

  bool isData_;
  bool runHLTJetVariables_;

  // trigger list
  std::vector<std::string> triggerPathNames_;

  edm::Service<TFileService> fs;

  ///////////////
  // Ntuple info

  TTree *smalltree;

  //// Event info
  EventInfoBranches EventInfo;

  //// Jet info
  std::vector<JetInfoBranches> JetInfo;

  const  reco::Vertex  *pv;

  edm::ESHandle<TransientTrackBuilder> trackBuilder ;
  edm::Handle<reco::VertexCollection> primaryVertex ;


  // helper class for associating PF candidates to jets
  //IPProducerHelpers::FromJetAndCands m_helper;

  // track V0 filter
  reco::V0Filter trackPairV0Filter;

  // track cuts
  double distJetAxis_;
  double decayLength_;
  double deltaR_;


  std::unordered_set<std::string> variables; // This unordered_set is going to contain the name of each single variable to be stored in the output tree

};

template<typename IPTI,typename VTX>
BTagHLTAnalyzerT<IPTI,VTX>::BTagHLTAnalyzerT(const edm::ParameterSet& iConfig):
  pv(0),
  //m_helper(iConfig, consumesCollector(),"Jets"),
  trackPairV0Filter(iConfig.getParameter<edm::ParameterSet>("trackPairV0Filter")),
  distJetAxis_(iConfig.getParameter<double>("distJetAxis")),
  decayLength_(iConfig.getParameter<double>("decayLength")),
  deltaR_(iConfig.getParameter<double>("deltaR"))
{
  //now do what ever initialization you need
  std::string module_type  = iConfig.getParameter<std::string>("@module_type");
  std::string module_label = iConfig.getParameter<std::string>("@module_label");
  std::cout << "Constructing " << module_type << ":" << module_label << std::endl;

  std::vector<edm::ParameterSet> groupSet = iConfig.getParameter<std::vector<edm::ParameterSet>>("groups");
  std::vector<edm::ParameterSet> variableSet = iConfig.getParameter<std::vector<edm::ParameterSet>>("variables");

  VariableParser variableParser(false);
  variables = variableParser.parseGroupsAndVariables(groupSet, variableSet);
  //variableParser.printStoredVariables();
  //variableParser.printGroups(groupSet);
  //variableParser.printVariables(variableSet);
  variableParser.saveStoredVariablesToFile();
  // Parameters

  minJetPt_  = iConfig.getParameter<double>("MinPt");
  maxJetEta_ = iConfig.getParameter<double>("MaxEta");

  runHLTJetVariables_ = iConfig.getParameter<bool>("runHLTJetVariables");

  // Modules
  primaryVertexColl_   = consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("HLTprimaryVertexColl"));

//
//  branchNamePrefix_ = iConfig.getParameter<std::string>("BranchNamePrefix");
  CaloJetCollectionTag_ = consumes<CaloJetCollection>(iConfig.getParameter<edm::InputTag>("CaloJets"));
  CaloJetTagCollectionTag_ = consumes<ShallowTagCollection>(iConfig.getParameter<edm::InputTag>("CaloJetTags"));
  CaloSVCollectionTag_   = consumes<std::vector<reco::SecondaryVertexTagInfo> >(iConfig.getParameter<edm::InputTag>("CaloSVs"));
  CaloJetCSVTag_ = consumes<HLTBTagValue>(iConfig.getParameter<edm::InputTag>("CaloJetCSVTags"));
  CaloJetDeepCSVTag_ = consumes<HLTBTagValue>(iConfig.getParameter<edm::InputTag>("CaloJetDeepCSVTags"));

  PFJetCollectionTag_   = consumes<PFJetCollection>(iConfig.getParameter<edm::InputTag>("PFJets"));
  PFJetTagCollectionTag_ = consumes<ShallowTagCollection>(iConfig.getParameter<edm::InputTag>("PFJetTags"));
  PFSVCollectionTag_   = consumes<std::vector<SVTagInfo> >(iConfig.getParameter<edm::InputTag>("PFSVs"));
  PFJetCSVTag_ = consumes<HLTBTagValue>(iConfig.getParameter<edm::InputTag>("PFJetCSVTags"));
  PFJetDeepCSVTag_ = consumes<HLTBTagValue>(iConfig.getParameter<edm::InputTag>("PFJetDeepCSVTags"));

  triggerTable_             = consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("triggerTable"));

  triggerPathNames_        = iConfig.getParameter<std::vector<std::string> >("HLTTriggerPathNames");



  ///////////////
  // TTree

  smalltree = fs->make<TTree>("ttree", "ttree");

  //--------------------------------------
  // event information
  //--------------------------------------
  EventInfo.RegisterBranches(smalltree, variableParser);


  //--------------------------------------
  // jet information
  //--------------------------------------
  JetInfo.reserve(2);
  JetInfo[0].RegisterBranches(smalltree, variableParser, "CaloJet");
  JetInfo[1].RegisterBranches(smalltree, variableParser, "PFJet");

}

template<typename IPTI,typename VTX>
BTagHLTAnalyzerT<IPTI,VTX>::~BTagHLTAnalyzerT()
{
}



//
// member functions
//

// ------------ method called to for each event  ------------
template<typename IPTI,typename VTX>
void BTagHLTAnalyzerT<IPTI,VTX>::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std;
  using namespace reco;
  //------------------------------------------------------
  // Event information
  //------------------------------------------------------
  EventInfo.Run = iEvent.id().run();

  EventInfo.BX  = iEvent.bunchCrossing();

  isData_ = iEvent.isRealData();

  if ( !isData_ && EventInfo.Run > 0 ) EventInfo.Run = -EventInfo.Run;

  EventInfo.Evt  = iEvent.id().event();
  EventInfo.LumiBlock  = iEvent.luminosityBlock();

  //------------------
  // Primary vertex
  //------------------
  iEvent.getByToken(primaryVertexColl_,primaryVertex);

  bool pvFound = (primaryVertex->size() != 0);
  if ( pvFound ) {
    pv = &(*primaryVertex->begin());
  }
  else {
    reco::Vertex::Error e;
    e(0,0)=0.0015*0.0015;
    e(1,1)=0.0015*0.0015;
    e(2,2)=15.*15.;
    reco::Vertex::Point p(0,0,0);
    pv=  new reco::Vertex(p,e,1,1,1);
  }
  EventInfo.PVz = (*primaryVertex)[0].z();
  EventInfo.PVez = (*primaryVertex)[0].zError();

  EventInfo.nPV=0;
  for (unsigned int i = 0; i< primaryVertex->size() ; ++i) {
    EventInfo.PV_x[EventInfo.nPV]      = (*primaryVertex)[i].x();
    EventInfo.PV_y[EventInfo.nPV]      = (*primaryVertex)[i].y();
    EventInfo.PV_z[EventInfo.nPV]      = (*primaryVertex)[i].z();
    EventInfo.PV_ex[EventInfo.nPV]     = (*primaryVertex)[i].xError();
    EventInfo.PV_ey[EventInfo.nPV]     = (*primaryVertex)[i].yError();
    EventInfo.PV_ez[EventInfo.nPV]     = (*primaryVertex)[i].zError();
    EventInfo.PV_chi2[EventInfo.nPV]   = (*primaryVertex)[i].normalizedChi2();
    EventInfo.PV_ndf[EventInfo.nPV]    = (*primaryVertex)[i].ndof();
    EventInfo.PV_isgood[EventInfo.nPV] = (*primaryVertex)[i].isValid();
    EventInfo.PV_isfake[EventInfo.nPV] = (*primaryVertex)[i].isFake();

    ++EventInfo.nPV;
  }


  //----------------------------------------
  // Transient track for IP calculation
  //----------------------------------------
  iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder", trackBuilder);

  //------------------------------------------------------
  // Trigger info
  //------------------------------------------------------

  edm::Handle<edm::TriggerResults> trigRes;
  iEvent.getByToken(triggerTable_, trigRes);

  EventInfo.nBitTrigger = int(triggerPathNames_.size()/32)+1;
  for(int i=0; i<EventInfo.nBitTrigger; ++i) EventInfo.BitTrigger[i] = 0;

  std::vector<std::string> triggerList;
  edm::Service<edm::service::TriggerNamesService> tns;
  bool foundNames = tns->getTrigPaths(*trigRes,triggerList);
  if ( !foundNames ) edm::LogError("TriggerNamesNotFound") << "Could not get trigger names!";
  if ( trigRes->size() != triggerList.size() ) edm::LogError("TriggerPathLengthMismatch") << "Length of names and paths not the same: "
											  << triggerList.size() << "," << trigRes->size() ;
  
  //debug: check if passes trigger
  //bool passTrig = processTrig(trigRes, triggerList);
  if(!passTrig){
    //cout << "Error, failed TRIG"<<endl;
    
    return;
    }

  //------------------------------------------------------
  // Jet info
  //------------------------------------------------------
  int iJetColl = 0 ;

  edm::Handle <CaloJetCollection> caloJetsColl;
  iEvent.getByToken (CaloJetCollectionTag_, caloJetsColl);
  bool havePassingCaloJet = havePassingJets<CaloJetCollection>(caloJetsColl);
  
  if(havePassingCaloJet){
    processHLTJets<CaloJetCollection, reco::SecondaryVertexTagInfo>(caloJetsColl, CaloJetTagCollectionTag_, CaloSVCollectionTag_, CaloJetCSVTag_, CaloJetDeepCSVTag_, iEvent, iSetup, iJetColl);
  }
  
  //
  // Increment Jet Collection
  //
  ++iJetColl;

  edm::Handle <PFJetCollection> pfJetsColl;
  iEvent.getByToken (PFJetCollectionTag_, pfJetsColl);
  bool havePassingPFJet = havePassingJets<PFJetCollection>(pfJetsColl);

  if(havePassingPFJet){
    processHLTPFJets(pfJetsColl, PFJetTagCollectionTag_, PFJetCSVTag_, PFJetDeepCSVTag_, iEvent, iSetup, iJetColl); 
  }



  //// Fill TTree
  smalltree->Fill();

  return;
}

template<typename IPTI,typename VTX>
bool BTagHLTAnalyzerT<IPTI,VTX>::processTrig(const edm::Handle<edm::TriggerResults>& trigRes, const std::vector<std::string>& triggerList)
{
  bool passTrig = false;
  for (unsigned int i = 0; i < trigRes->size(); ++i) {

    if ( !trigRes->at(i).accept() ) continue;


    for (std::vector<std::string>::const_iterator itTrigPathNames = triggerPathNames_.begin();
        itTrigPathNames != triggerPathNames_.end(); ++itTrigPathNames)
    {
      int triggerIdx = ( itTrigPathNames - triggerPathNames_.begin() );
      int bitIdx = int(triggerIdx/32);
      if ( NameCompatible(*itTrigPathNames,triggerList[i]) ) {
	passTrig = true;
	EventInfo.BitTrigger[bitIdx] |= ( 1 << (triggerIdx - bitIdx*32) );
      }
    }

  } //// Loop over trigger names

  return passTrig;
}

// This is needed to get a TrackingParticle --> Cluster match (instead of Cluster-->TP) (only needed in processJets)


template<typename IPTI,typename VTX>
template<typename JetColl, typename SVColl>
void BTagHLTAnalyzerT<IPTI,VTX>::processHLTJets(const edm::Handle<JetColl>& jetsColl, const edm::EDGetTokenT<ShallowTagCollection>& jetTagsCollToken, const edm::EDGetTokenT<std::vector<SVColl> >& svCollToken, 
						const edm::EDGetTokenT<HLTBTagValue>& CSVToken, const edm::EDGetTokenT<HLTBTagValue>& deepCSVToken,
						const edm::Event& iEvent, const edm::EventSetup& iSetup, const int iJetColl)
{

  //int numjet = 0;
  JetInfo[iJetColl].nJet = 0;
  JetInfo[iJetColl].nTrack = 0;
  JetInfo[iJetColl].nTrkTagVar = 0;
  JetInfo[iJetColl].nSVTagVar  = 0;
  JetInfo[iJetColl].nSV = 0;
  JetInfo[iJetColl].nTrkEtaRelTagVarCSV = 0;
  //JetInfo[iJetColl].nTrkTagVarCSV = 0;
  //xstd::cout << "getting jetTags Coll " << std::endl;
  edm::Handle <ShallowTagCollection> jetTagsColl;
  iEvent.getByToken (jetTagsCollToken, jetTagsColl);
  //std::cout << " checking for failure" << std::endl;
  if(!jetTagsColl.isValid()) return;

  edm::Handle <std::vector<SVColl> > jetSVTagsColl;
  iEvent.getByToken (svCollToken, jetSVTagsColl);

  edm::Handle <HLTBTagValue> jetCSVColl;
  iEvent.getByToken (CSVToken, jetCSVColl);

  edm::Handle <HLTBTagValue> jetDeepCSVColl;
  iEvent.getByToken (deepCSVToken, jetDeepCSVColl);

  for ( typename JetColl::const_iterator jet = jetsColl->begin(); jet != jetsColl->end(); ++jet ) {

    double ptjet  = jet->pt()  ;
    double etajet = jet->eta() ;
    double phijet = jet->phi() ;

    if( ptjet < minJetPt_ || std::fabs( etajet ) > maxJetEta_ ) continue;

    if(runHLTJetVariables_){
      JetInfo[iJetColl].Jet_area[JetInfo[iJetColl].nJet]      = jet->jetArea();
      JetInfo[iJetColl].Jet_eta[JetInfo[iJetColl].nJet]       = jet->eta();
      JetInfo[iJetColl].Jet_phi[JetInfo[iJetColl].nJet]       = jet->phi();
      JetInfo[iJetColl].Jet_pt[JetInfo[iJetColl].nJet]        = jet->pt();
      JetInfo[iJetColl].Jet_mass[JetInfo[iJetColl].nJet]      = jet->mass();

      //std::cout << "CSV is " << jet->bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") << std::endl;

      //
      //  Fill CSV Value
      //
      JetInfo[iJetColl].Jet_CombIVF[JetInfo[iJetColl].nJet]     = -1;
      if(jetCSVColl.isValid()){
	unsigned int nCSV = jetCSVColl->size();
	for(unsigned int iCSV = 0; iCSV < nCSV; ++iCSV){
	  const reco::Jet* thisCSVJet = jetCSVColl->key(iCSV).get();
	  if(reco::deltaR( etajet, phijet, thisCSVJet->eta(), thisCSVJet->phi()) < 0.1){
	    JetInfo[iJetColl].Jet_CombIVF[JetInfo[iJetColl].nJet]     = jetCSVColl->value(iCSV);
	  }
	}
      }

      //
      //  Fill DeepCSV Value
      //
      JetInfo[iJetColl].Jet_DeepCSVb[JetInfo[iJetColl].nJet]     = -1;
      if(jetDeepCSVColl.isValid()){
	unsigned int nDeepCSV = jetDeepCSVColl->size();
	for(unsigned int iDeepCSV = 0; iDeepCSV < nDeepCSV; ++iDeepCSV){
	  const reco::Jet* thisDeepCSVJet = jetDeepCSVColl->key(iDeepCSV).get();
	  if(reco::deltaR( etajet, phijet, thisDeepCSVJet->eta(), thisDeepCSVJet->phi()) < 0.1){
	    JetInfo[iJetColl].Jet_DeepCSVb[JetInfo[iJetColl].nJet]     = jetDeepCSVColl->value(iDeepCSV);
	  }
	}
      }


      //
      //  Fill Shallow Tag Vars
      //
      for(ShallowTagCollection::const_iterator jetTagInfo = jetTagsColl->begin(); jetTagInfo != jetTagsColl->end(); ++jetTagInfo){
	reco::TaggingVariableList tagVars = jetTagInfo->taggingVariables();
	auto tagJet = jetTagInfo->jet();
	float tagJetPhi  = tagJet->phi();
	float tagJetEta  = tagJet->eta();
	if(  std::fabs(tagJetPhi - phijet) < 0.1 && std::fabs(tagJetEta - etajet) < 0.1){

	  int nTracks = tagVars.getList(reco::btau::jetNSelectedTracks,false).at(0);
	  int nSVs    = tagVars.getList(reco::btau::jetNSecondaryVertices,false).at(0);

	  // per jet per track
          JetInfo[iJetColl].Jet_nFirstTrkTagVar[JetInfo[iJetColl].nJet] = JetInfo[iJetColl].nTrkTagVar;
	  JetInfo[iJetColl].Jet_ntracks[JetInfo[iJetColl].nJet] = nTracks;
	  
	  JetInfo[iJetColl].TagVar_jetNTracks[JetInfo[iJetColl].nJet]                  = nTracks;
	  JetInfo[iJetColl].TagVar_jetNSecondaryVertices[JetInfo[iJetColl].nJet]       = nSVs;

	  //std::cout << "Filling jet-level " << std::endl;
	  //std::cout << tagVars.getList(reco::btau::trackSumJetEtRatio,false).size() << std::endl;
	  if(tagVars.getList(reco::btau::trackJetPt,false).size()){
	    JetInfo[iJetColl].TagVarCSV_trackJetPt[JetInfo[iJetColl].nJet]                  = ( tagVars.getList(reco::btau::trackJetPt,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_trackJetPt[JetInfo[iJetColl].nJet]                  = 0;
	  }

	  if(tagVars.getList(reco::btau::jetNTracks,false).size()){
	    JetInfo[iJetColl].TagVarCSV_jetNTracks[JetInfo[iJetColl].nJet]                  = ( tagVars.getList(reco::btau::jetNTracks,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_jetNTracks[JetInfo[iJetColl].nJet]                  = 0;
	  }

	  if(tagVars.getList(reco::btau::trackSumJetEtRatio,false).size()){
	    JetInfo[iJetColl].TagVarCSV_trackSumJetEtRatio[JetInfo[iJetColl].nJet]          = ( tagVars.getList(reco::btau::trackSumJetEtRatio,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_trackSumJetEtRatio[JetInfo[iJetColl].nJet]          = 0;
	  }

	  if(tagVars.getList(reco::btau::trackSumJetDeltaR,false).size()){
	    JetInfo[iJetColl].TagVarCSV_trackSumJetDeltaR[JetInfo[iJetColl].nJet]           = ( tagVars.getList(reco::btau::trackSumJetDeltaR,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_trackSumJetDeltaR[JetInfo[iJetColl].nJet]           = 0;
	  }

	  if(tagVars.getList(reco::btau::trackSip2dValAboveCharm,false).size()){
	    JetInfo[iJetColl].TagVarCSV_trackSip2dValAboveCharm[JetInfo[iJetColl].nJet]     = ( tagVars.getList(reco::btau::trackSip2dValAboveCharm,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_trackSip2dValAboveCharm[JetInfo[iJetColl].nJet]     = 0;
	  }

	  if(tagVars.getList(reco::btau::trackSip2dSigAboveCharm,false).size()){
	    JetInfo[iJetColl].TagVarCSV_trackSip2dSigAboveCharm[JetInfo[iJetColl].nJet]     = ( tagVars.getList(reco::btau::trackSip2dSigAboveCharm,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_trackSip2dSigAboveCharm[JetInfo[iJetColl].nJet]     = 0;
	  }

	  if(tagVars.getList(reco::btau::trackSip3dValAboveCharm,false).size()){
	    JetInfo[iJetColl].TagVarCSV_trackSip3dValAboveCharm[JetInfo[iJetColl].nJet]     = ( tagVars.getList(reco::btau::trackSip3dValAboveCharm,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_trackSip3dValAboveCharm[JetInfo[iJetColl].nJet]     = 0;
	  }

	  if(tagVars.getList(reco::btau::trackSip3dSigAboveCharm,false).size()){
	    JetInfo[iJetColl].TagVarCSV_trackSip3dSigAboveCharm[JetInfo[iJetColl].nJet]     = ( tagVars.getList(reco::btau::trackSip3dSigAboveCharm,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_trackSip3dSigAboveCharm[JetInfo[iJetColl].nJet]     = 0;
	  }

	  if(tagVars.getList(reco::btau::vertexCategory,false).size()){
	    JetInfo[iJetColl].TagVarCSV_vertexCategory[JetInfo[iJetColl].nJet]              = ( tagVars.getList(reco::btau::vertexCategory,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_vertexCategory[JetInfo[iJetColl].nJet]              = 0;
	  }

	  if(tagVars.getList(reco::btau::jetNSecondaryVertices,false).size()){
	    JetInfo[iJetColl].TagVarCSV_jetNSecondaryVertices[JetInfo[iJetColl].nJet]       = ( tagVars.getList(reco::btau::jetNSecondaryVertices,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_jetNSecondaryVertices[JetInfo[iJetColl].nJet]       = 0;
	  }

	  if(tagVars.getList(reco::btau::vertexMass,false).size()){
	    JetInfo[iJetColl].TagVarCSV_vertexMass[JetInfo[iJetColl].nJet]                  = ( tagVars.getList(reco::btau::vertexMass,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_vertexMass[JetInfo[iJetColl].nJet]                  = 0;
	  }

	  if(tagVars.getList(reco::btau::vertexNTracks,false).size()){
	    JetInfo[iJetColl].TagVarCSV_vertexNTracks[JetInfo[iJetColl].nJet]               = ( tagVars.getList(reco::btau::vertexNTracks,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_vertexNTracks[JetInfo[iJetColl].nJet]               = 0;
	  }

	  if(tagVars.getList(reco::btau::vertexEnergyRatio,false).size()){
	    JetInfo[iJetColl].TagVarCSV_vertexEnergyRatio[JetInfo[iJetColl].nJet]           = ( tagVars.getList(reco::btau::vertexEnergyRatio,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_vertexEnergyRatio[JetInfo[iJetColl].nJet]           = 0;
	  }

	  if(tagVars.getList(reco::btau::vertexJetDeltaR,false).size()){
	    JetInfo[iJetColl].TagVarCSV_vertexJetDeltaR[JetInfo[iJetColl].nJet]             = ( tagVars.getList(reco::btau::vertexJetDeltaR,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_vertexJetDeltaR[JetInfo[iJetColl].nJet]             = 0;
	  }

	  if(tagVars.getList(reco::btau::flightDistance2dVal,false).size()){
	    JetInfo[iJetColl].TagVarCSV_flightDistance2dVal[JetInfo[iJetColl].nJet]         = ( tagVars.getList(reco::btau::flightDistance2dVal,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_flightDistance2dVal[JetInfo[iJetColl].nJet]         = 0;
	  }

	  if(tagVars.getList(reco::btau::flightDistance2dSig,false).size()){
	    JetInfo[iJetColl].TagVarCSV_flightDistance2dSig[JetInfo[iJetColl].nJet]         = ( tagVars.getList(reco::btau::flightDistance2dSig,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_flightDistance2dSig[JetInfo[iJetColl].nJet]         = 0;
	  }

	  if(tagVars.getList(reco::btau::flightDistance3dVal,false).size()){
	    JetInfo[iJetColl].TagVarCSV_flightDistance3dVal[JetInfo[iJetColl].nJet]         = ( tagVars.getList(reco::btau::flightDistance3dVal,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_flightDistance3dVal[JetInfo[iJetColl].nJet]         = 0;
	  }

	  if(tagVars.getList(reco::btau::flightDistance3dSig,false).size()){
	    JetInfo[iJetColl].TagVarCSV_flightDistance3dSig[JetInfo[iJetColl].nJet]         = ( tagVars.getList(reco::btau::flightDistance3dSig,false).at(0));
	  }else{
	    JetInfo[iJetColl].TagVarCSV_flightDistance3dSig[JetInfo[iJetColl].nJet]         = 0;
	  }


          std::vector<float> tagValList = tagVars.getList(reco::btau::trackMomentum,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackMomentum[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackEta,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackEta[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackPhi,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackPhi[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackPtRel,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackPtRel[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackPPar,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackPPar[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackEtaRel,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackEtaRel[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackDeltaR,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackDeltaR[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackPtRatio,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackPtRatio[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackPParRatio,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackPParRatio[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackSip2dVal,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackSip2dVal[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackSip2dSig,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackSip2dSig[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackSip3dVal,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackSip3dVal[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackSip3dSig,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackSip3dSig[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackDecayLenVal,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackDecayLenVal[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackDecayLenSig,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackDecayLenSig[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackJetDistVal,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackJetDistVal[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackJetDistSig,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackJetDistSig[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackChi2,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackChi2[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackNTotalHits,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackNTotalHits[JetInfo[iJetColl].nTrkTagVar] );
          tagValList = tagVars.getList(reco::btau::trackNPixelHits,false);
          if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_trackNPixelHits[JetInfo[iJetColl].nTrkTagVar] );

	  JetInfo[iJetColl].nTrkTagVar += nTracks;
	  JetInfo[iJetColl].Jet_nLastTrkTagVar[JetInfo[iJetColl].nJet] = JetInfo[iJetColl].nTrkTagVar;


	  //JetInfo[iJetColl].Jet_nFirstTrkTagVarCSV[JetInfo[iJetColl].nJet] = JetInfo[iJetColl].nTrkTagVarCSV;
	  //JetInfo[iJetColl].nTrkTagVarCSV += tagVars.getList(reco::btau::trackSip2dValAboveCharm,false).size();
	  //JetInfo[iJetColl].Jet_nLastTrkTagVarCSV[JetInfo[iJetColl].nJet] = JetInfo[iJetColl].nTrkTagVarCSV;

	  JetInfo[iJetColl].Jet_nFirstTrkEtaRelTagVarCSV[JetInfo[iJetColl].nJet] = JetInfo[iJetColl].nTrkEtaRelTagVarCSV;
	  tagValList = tagVars.getList(reco::btau::trackEtaRel,false);
	  JetInfo[iJetColl].TagVarCSV_jetNTracksEtaRel[JetInfo[iJetColl].nJet] = tagValList.size();

	  if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVarCSV_trackEtaRel[JetInfo[iJetColl].nTrkEtaRelTagVarCSV] );

	  JetInfo[iJetColl].nTrkEtaRelTagVarCSV += JetInfo[iJetColl].TagVarCSV_jetNTracksEtaRel[JetInfo[iJetColl].nJet];
	  JetInfo[iJetColl].Jet_nLastTrkEtaRelTagVarCSV[JetInfo[iJetColl].nJet] = JetInfo[iJetColl].nTrkEtaRelTagVarCSV;

	  // per jet per secondary vertex
	  JetInfo[iJetColl].Jet_nFirstSVTagVar[JetInfo[iJetColl].nJet] = JetInfo[iJetColl].nSVTagVar;

	  tagValList = tagVars.getList(reco::btau::vertexMass,false);
	  if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_vertexMass[JetInfo[iJetColl].nSVTagVar] );
	  tagValList = tagVars.getList(reco::btau::vertexNTracks,false);
	  if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_vertexNTracks[JetInfo[iJetColl].nSVTagVar] );
	  tagValList = tagVars.getList(reco::btau::vertexJetDeltaR,false);
	  if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_vertexJetDeltaR[JetInfo[iJetColl].nSVTagVar] );
	  tagValList = tagVars.getList(reco::btau::flightDistance2dVal,false);
	  if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_flightDistance2dVal[JetInfo[iJetColl].nSVTagVar] );
	  tagValList = tagVars.getList(reco::btau::flightDistance2dSig,false);
	  if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_flightDistance2dSig[JetInfo[iJetColl].nSVTagVar] );
	  tagValList = tagVars.getList(reco::btau::flightDistance3dVal,false);
	  if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_flightDistance3dVal[JetInfo[iJetColl].nSVTagVar] );
	  tagValList = tagVars.getList(reco::btau::flightDistance3dSig,false);
	  if(tagValList.size()>0) std::copy( tagValList.begin(), tagValList.end(), &JetInfo[iJetColl].TagVar_flightDistance3dSig[JetInfo[iJetColl].nSVTagVar] );

	  JetInfo[iJetColl].nSVTagVar += nSVs;
	  JetInfo[iJetColl].Jet_nLastSVTagVar[JetInfo[iJetColl].nJet] = JetInfo[iJetColl].nSVTagVar;

    
	}// Matched TagInfo
      }// Loop on ShalowTags


      reco::TrackKinematics allKinematics;

      JetInfo[iJetColl].Jet_nFirstTrack[JetInfo[iJetColl].nJet]  = JetInfo[iJetColl].nTrack;


      // loop over SV TagInfos
      for(auto iterTI = jetSVTagsColl->begin(); iterTI != jetSVTagsColl->end(); ++iterTI) {

	auto tagJet = iterTI->jet();
	float tagJetPhi  = tagJet->phi();
	float tagJetEta  = tagJet->eta();
	if(  std::fabs(tagJetPhi - phijet) < 0.1 && std::fabs(tagJetEta - etajet) < 0.1){

	  // get TagInfos
	  int nseltracks = 0;
	  const SVColl & svTagInfo = *(iterTI);
	  const auto & ipInfo = *(iterTI->trackIPTagInfoRef().get());

	  unsigned int trackSize = ipInfo.selectedTracks().size();
	  JetInfo[iJetColl].Jet_ntracks[JetInfo[iJetColl].nJet] = trackSize;

	  for (unsigned int itt=0; itt < trackSize; ++itt){
	    const auto ptrackRef = (ipInfo.selectedTracks()[itt]); //TrackRef or 
	    const reco::TrackBaseRef ptrackBaseRef = BTagHLT::toTrackRef(ptrackRef);
	    const reco::Track * ptrackPtr = reco::btag::toTrack(ptrackRef);
	    const reco::Track & ptrack = *ptrackPtr;

	    reco::TransientTrack transientTrack = trackBuilder->build(ptrackRef);
	    GlobalVector direction(jet->px(), jet->py(), jet->pz());
	    
	    //--------------------------------
	    Double_t decayLength=-1;
	    TrajectoryStateOnSurface closest = IPTools::closestApproachToJet(transientTrack.impactPointState(), *pv, direction, transientTrack.field());
	    if (closest.isValid())
	      decayLength =  (closest.globalPosition() - RecoVertex::convertPos(pv->position())).mag();
	    else
	      decayLength = -1;
	    
	    Double_t distJetAxis =  IPTools::jetTrackDistance(transientTrack, direction, *pv).second.value();
	    
	    JetInfo[iJetColl].Track_dist[JetInfo[iJetColl].nTrack]     = distJetAxis;
	    JetInfo[iJetColl].Track_length[JetInfo[iJetColl].nTrack]   = decayLength;
	    
	    JetInfo[iJetColl].Track_dxy[JetInfo[iJetColl].nTrack]      = ptrack.dxy(pv->position());
	    JetInfo[iJetColl].Track_dz[JetInfo[iJetColl].nTrack]       = ptrack.dz(pv->position());
	    JetInfo[iJetColl].Track_dxyError[JetInfo[iJetColl].nTrack]      = ptrack.dxyError();
	    JetInfo[iJetColl].Track_dzError[JetInfo[iJetColl].nTrack]       = ptrack.dzError();

	    {
	      TransverseImpactPointExtrapolator extrapolator(transientTrack.field());
	      TrajectoryStateOnSurface closestOnTransversePlaneState = extrapolator.extrapolate(transientTrack.impactPointState(),RecoVertex::convertPos(pv->position()));
	      if( closestOnTransversePlaneState.isValid() )
		{
		  GlobalPoint impactPoint    = closestOnTransversePlaneState.globalPosition();
		  GlobalVector IPVec(impactPoint.x()-pv->x(),impactPoint.y()-pv->y(),0.);
		  double prod = IPVec.dot(direction);
		  int sign = (prod>=0) ? 1 : -1;
		  JetInfo[iJetColl].Track_sign2D[JetInfo[iJetColl].nTrack]      = sign;
		}
	      else
		{
		  JetInfo[iJetColl].Track_sign2D[JetInfo[iJetColl].nTrack]      = -666.;
		}
	    }{
	      AnalyticalImpactPointExtrapolator extrapolator(transientTrack.field());
	      TrajectoryStateOnSurface closestIn3DSpaceState = extrapolator.extrapolate(transientTrack.impactPointState(),RecoVertex::convertPos(pv->position()));
	      if( closestIn3DSpaceState.isValid() )
		{
		  GlobalPoint impactPoint = closestIn3DSpaceState.globalPosition();
		  GlobalVector IPVec(impactPoint.x()-pv->x(),impactPoint.y()-pv->y(),impactPoint.z()-pv->z());
		  double prod = IPVec.dot(direction);
		  int sign = (prod>=0) ? 1 : -1;
		  JetInfo[iJetColl].Track_sign3D[JetInfo[iJetColl].nTrack]      = sign;
		}
	      else
		{
		  std::cout << "FAILURE: TrajectoryStateOnSurface is not available" << std::endl;
		  JetInfo[iJetColl].Track_sign3D[JetInfo[iJetColl].nTrack]      = -666.;
		}
	    }

	    float deltaR = reco::deltaR( ptrackRef->eta(), ptrackRef->phi(),
					 JetInfo[iJetColl].Jet_eta[JetInfo[iJetColl].nJet], JetInfo[iJetColl].Jet_phi[JetInfo[iJetColl].nJet] );
	    
	    bool pass_cut_trk = false;
	    //if (std::fabs(distJetAxis) < _distJetAxis && decayLength < _decayLength) 

	    if (std::fabs(distJetAxis) < distJetAxis_ && decayLength < decayLength_ && deltaR < deltaR_){
	      pass_cut_trk = true;
	      nseltracks++;
	    }

	    if(pass_cut_trk){
	      JetInfo[iJetColl].Track_IP2D[JetInfo[iJetColl].nTrack]     = ipInfo.impactParameterData()[itt].ip2d.value();
              JetInfo[iJetColl].Track_IP2Dsig[JetInfo[iJetColl].nTrack]  = ipInfo.impactParameterData()[itt].ip2d.significance();
              JetInfo[iJetColl].Track_IP[JetInfo[iJetColl].nTrack]       = ipInfo.impactParameterData()[itt].ip3d.value();
              JetInfo[iJetColl].Track_IPsig[JetInfo[iJetColl].nTrack]    = ipInfo.impactParameterData()[itt].ip3d.significance();
              JetInfo[iJetColl].Track_IP2Derr[JetInfo[iJetColl].nTrack]  = ipInfo.impactParameterData()[itt].ip2d.error();
              JetInfo[iJetColl].Track_IPerr[JetInfo[iJetColl].nTrack]    = ipInfo.impactParameterData()[itt].ip3d.error();
              JetInfo[iJetColl].Track_Proba[JetInfo[iJetColl].nTrack]    = ipInfo.probabilities(0)[itt];
        
              JetInfo[iJetColl].Track_p[JetInfo[iJetColl].nTrack]        = ptrack.p();
              JetInfo[iJetColl].Track_pt[JetInfo[iJetColl].nTrack]       = ptrack.pt();
              JetInfo[iJetColl].Track_eta[JetInfo[iJetColl].nTrack]      = ptrack.eta();
              JetInfo[iJetColl].Track_phi[JetInfo[iJetColl].nTrack]      = ptrack.phi();
              JetInfo[iJetColl].Track_chi2[JetInfo[iJetColl].nTrack]     = ptrack.normalizedChi2();
              JetInfo[iJetColl].Track_charge[JetInfo[iJetColl].nTrack]   = ptrack.charge();
        
              JetInfo[iJetColl].Track_nHitAll[JetInfo[iJetColl].nTrack]  = ptrack.numberOfValidHits();
              JetInfo[iJetColl].Track_nHitPixel[JetInfo[iJetColl].nTrack]= ptrack.hitPattern().numberOfValidPixelHits();
              JetInfo[iJetColl].Track_nHitStrip[JetInfo[iJetColl].nTrack]= ptrack.hitPattern().numberOfValidStripHits();
              JetInfo[iJetColl].Track_nHitTIB[JetInfo[iJetColl].nTrack]  = ptrack.hitPattern().numberOfValidStripTIBHits();
              JetInfo[iJetColl].Track_nHitTID[JetInfo[iJetColl].nTrack]  = ptrack.hitPattern().numberOfValidStripTIDHits();
              JetInfo[iJetColl].Track_nHitTOB[JetInfo[iJetColl].nTrack]  = ptrack.hitPattern().numberOfValidStripTOBHits();
              JetInfo[iJetColl].Track_nHitTEC[JetInfo[iJetColl].nTrack]  = ptrack.hitPattern().numberOfValidStripTECHits();
              JetInfo[iJetColl].Track_nHitPXB[JetInfo[iJetColl].nTrack]  = ptrack.hitPattern().numberOfValidPixelBarrelHits();
              JetInfo[iJetColl].Track_nHitPXF[JetInfo[iJetColl].nTrack]  = ptrack.hitPattern().numberOfValidPixelEndcapHits();
              JetInfo[iJetColl].Track_isHitL1[JetInfo[iJetColl].nTrack]  = ptrack.hitPattern().hasValidHitInPixelLayer(PixelSubdetector::SubDetector::PixelBarrel, 1);

              JetInfo[iJetColl].Track_algo[JetInfo[iJetColl].nTrack]  = ptrack.algo();
              JetInfo[iJetColl].Track_originalAlgo[JetInfo[iJetColl].nTrack]  = ptrack.originalAlgo();
	      

	      setTracksPVBase(ptrack, primaryVertex,
			      JetInfo[iJetColl].Track_PV[JetInfo[iJetColl].nTrack],
			      JetInfo[iJetColl].Track_PVweight[JetInfo[iJetColl].nTrack]);

	      if(JetInfo[iJetColl].Track_PV[JetInfo[iJetColl].nTrack]==0 &&
		 JetInfo[iJetColl].Track_PVweight[JetInfo[iJetColl].nTrack]>0.5) { allKinematics.add(ptrackRef); }


	      setTracksSV(ptrackRef, &svTagInfo,
			  JetInfo[iJetColl].Track_isfromSV[JetInfo[iJetColl].nTrack],
			  JetInfo[iJetColl].Track_SV[JetInfo[iJetColl].nTrack],
			  JetInfo[iJetColl].Track_SVweight[JetInfo[iJetColl].nTrack]);



	      // check if the track is a V0 decay product candidate
	      JetInfo[iJetColl].Track_isfromV0[JetInfo[iJetColl].nTrack] = 0;
	      
	      // apply the V0 filter
	      std::vector<const reco::Track*> trackPairV0Test(2);
	      trackPairV0Test[0] = ptrackPtr;
	      for (unsigned int jtt=0; jtt < trackSize; ++jtt){
	      	if (itt == jtt) continue;
	      	  
	      	const auto pairTrackRef = (ipInfo.selectedTracks()[jtt]);
		const reco::Track * pairTrackPtr = reco::btag::toTrack(pairTrackRef);
	      	trackPairV0Test[1] = pairTrackPtr;
	      	
	      	if (!trackPairV0Filter(trackPairV0Test))
	      	  {
	      	    JetInfo[iJetColl].Track_isfromV0[JetInfo[iJetColl].nTrack] = 1;
	      	    break;
	      	  }
	      }// jtt

	      ++JetInfo[iJetColl].nTrack;

	    }//if(pass_cut_trk){

	    JetInfo[iJetColl].Jet_ntracks[JetInfo[iJetColl].nJet] = JetInfo[iJetColl].nTrack-JetInfo[iJetColl].Jet_nFirstTrack[JetInfo[iJetColl].nJet];
	  }//Loop on tracks


	  math::XYZTLorentzVector allSum = allKinematics.weightedVectorSum() ; // allKinematics.vectorSum()

	  JetInfo[iJetColl].Jet_nLastTrack[JetInfo[iJetColl].nJet]   = JetInfo[iJetColl].nTrack;
	  JetInfo[iJetColl].Jet_nseltracks[JetInfo[iJetColl].nJet] = nseltracks;


	  // 
	  // SV
	  //
	  JetInfo[iJetColl].Jet_nFirstSV[JetInfo[iJetColl].nJet]  = JetInfo[iJetColl].nSV;
	  JetInfo[iJetColl].Jet_SV_multi[JetInfo[iJetColl].nJet]  = svTagInfo.nVertices();

	  for (size_t vtx = 0; vtx < (size_t)svTagInfo.nVertices(); ++vtx) {
	    
	    JetInfo[iJetColl].SV_x[JetInfo[iJetColl].nSV]    = BTagHLT::position(svTagInfo.secondaryVertex(vtx)).x();
	    JetInfo[iJetColl].SV_y[JetInfo[iJetColl].nSV]    = BTagHLT::position(svTagInfo.secondaryVertex(vtx)).y();
	    JetInfo[iJetColl].SV_z[JetInfo[iJetColl].nSV]    = BTagHLT::position(svTagInfo.secondaryVertex(vtx)).z();
	    JetInfo[iJetColl].SV_ex[JetInfo[iJetColl].nSV]   = BTagHLT::xError(svTagInfo.secondaryVertex(vtx));
	    JetInfo[iJetColl].SV_ey[JetInfo[iJetColl].nSV]   = BTagHLT::yError(svTagInfo.secondaryVertex(vtx));
	    JetInfo[iJetColl].SV_ez[JetInfo[iJetColl].nSV]   = BTagHLT::zError(svTagInfo.secondaryVertex(vtx));
	    JetInfo[iJetColl].SV_chi2[JetInfo[iJetColl].nSV] = BTagHLT::chi2(svTagInfo.secondaryVertex(vtx));
	    JetInfo[iJetColl].SV_ndf[JetInfo[iJetColl].nSV]  = BTagHLT::ndof(svTagInfo.secondaryVertex(vtx));
	    
	    JetInfo[iJetColl].SV_flight[JetInfo[iJetColl].nSV]      = svTagInfo.flightDistance(vtx).value();
	    JetInfo[iJetColl].SV_flightErr[JetInfo[iJetColl].nSV]   = svTagInfo.flightDistance(vtx).error();
	    JetInfo[iJetColl].SV_flight2D[JetInfo[iJetColl].nSV]    = svTagInfo.flightDistance(vtx, true).value();
	    JetInfo[iJetColl].SV_flight2DErr[JetInfo[iJetColl].nSV] = svTagInfo.flightDistance(vtx, true).error();
	    JetInfo[iJetColl].SV_nTrk[JetInfo[iJetColl].nSV]        = BTagHLT::vtxTracks(svTagInfo.secondaryVertex(vtx));
	    
	    JetInfo[iJetColl].SV_vtx_pt[JetInfo[iJetColl].nSV]  = svTagInfo.secondaryVertex(vtx).p4().pt();
	    JetInfo[iJetColl].SV_vtx_eta[JetInfo[iJetColl].nSV] = svTagInfo.secondaryVertex(vtx).p4().eta();
	    JetInfo[iJetColl].SV_vtx_phi[JetInfo[iJetColl].nSV] = svTagInfo.secondaryVertex(vtx).p4().phi();
	    JetInfo[iJetColl].SV_mass[JetInfo[iJetColl].nSV]    = svTagInfo.secondaryVertex(vtx).p4().mass();
	    
	    Int_t totcharge=0;
	    reco::TrackKinematics vertexKinematics;
	    
	    // get the vertex kinematics and charge
	    vertexKinematicsAndChange(svTagInfo.secondaryVertex(vtx), vertexKinematics, totcharge);
	    
	    // total charge at the secondary vertex
	    JetInfo[iJetColl].SV_totCharge[JetInfo[iJetColl].nSV]=totcharge;
	    
	    math::XYZTLorentzVector vertexSum = vertexKinematics.weightedVectorSum();
	    edm::RefToBase<reco::Jet> jet = ipInfo.jet();
	    math::XYZVector jetDir = jet->momentum().Unit();
	    GlobalVector flightDir = svTagInfo.flightDirection(vtx);

	    JetInfo[iJetColl].SV_deltaR_jet[JetInfo[iJetColl].nSV]     = ( reco::deltaR(flightDir, jetDir) );
	    JetInfo[iJetColl].SV_deltaR_sum_jet[JetInfo[iJetColl].nSV] = ( reco::deltaR(vertexSum, jetDir) );
	    JetInfo[iJetColl].SV_deltaR_sum_dir[JetInfo[iJetColl].nSV] = ( reco::deltaR(vertexSum, flightDir) );

	    Line::PositionType pos(GlobalPoint(BTagHLT::position(svTagInfo.secondaryVertex(vtx)).x(),
					       BTagHLT::position(svTagInfo.secondaryVertex(vtx)).y(),
					       BTagHLT::position(svTagInfo.secondaryVertex(vtx)).z()));

	    Line trackline(pos,flightDir);
	    // get the Jet  line
	    Line::PositionType pos2(GlobalPoint(pv->x(),pv->y(),pv->z()));
	    Line::DirectionType dir2(GlobalVector(jetDir.x(),jetDir.y(),jetDir.z()));
	    Line jetline(pos2,dir2);
	    // now compute the distance between the two lines
	    JetInfo[iJetColl].SV_vtxDistJetAxis[JetInfo[iJetColl].nSV] = (jetline.distance(trackline)).mag();
	    
	    JetInfo[iJetColl].SV_EnergyRatio[JetInfo[iJetColl].nSV]= vertexSum.E() / allSum.E();
	    JetInfo[iJetColl].SV_dir_x[JetInfo[iJetColl].nSV]= flightDir.x();
	    JetInfo[iJetColl].SV_dir_y[JetInfo[iJetColl].nSV]= flightDir.y();
	    JetInfo[iJetColl].SV_dir_z[JetInfo[iJetColl].nSV]= flightDir.z();
	    
	    ++JetInfo[iJetColl].nSV;
	  }//loop on seconday vertices
	  
	  JetInfo[iJetColl].Jet_nLastSV[JetInfo[iJetColl].nJet] = JetInfo[iJetColl].nSV;

	  
	  
	  
	}// matched SV TagInfo
      }// Loop over SV TagInfos    

    

    }//runHLTJetVariables


    //++numjet;
    ++JetInfo[iJetColl].nJet;
  }

  return;
}



template<typename IPTI,typename VTX>
void BTagHLTAnalyzerT<IPTI,VTX>::processHLTPFJets(const edm::Handle<PFJetCollection>& jetsColl, const edm::EDGetTokenT<ShallowTagCollection>& jetTagsCollToken, 
						  const edm::EDGetTokenT<HLTBTagValue>& CSVToken, const edm::EDGetTokenT<HLTBTagValue>& deepCSVToken,
						  const edm::Event& iEvent, const edm::EventSetup& iSetup, const int iJetColl)
{


  processHLTJets<PFJetCollection, SVTagInfo>(jetsColl,jetTagsCollToken,PFSVCollectionTag_,CSVToken, deepCSVToken, iEvent,iSetup,iJetColl);

  for ( PFJetCollection::const_iterator jet = jetsColl->begin(); jet != jetsColl->end(); ++jet ) {

    double ptjet  = jet->pt()  ;
    double etajet = jet->eta() ;
    
    if( ptjet < minJetPt_ || std::fabs( etajet ) > maxJetEta_ ) continue;

    if(runHLTJetVariables_){

      // per jet
      // run 2 id: https://twiki.cern.ch/CMS/JetID13TeVRun2017
      JetInfo[iJetColl].TagVar_chargedHadronEnergyFraction[JetInfo[iJetColl].nJet] = jet->chargedHadronEnergyFraction();
      JetInfo[iJetColl].TagVar_neutralHadronEnergyFraction[JetInfo[iJetColl].nJet] = jet->neutralHadronEnergyFraction();
      JetInfo[iJetColl].TagVar_photonEnergyFraction[JetInfo[iJetColl].nJet]        = jet->photonEnergyFraction();
      JetInfo[iJetColl].TagVar_electronEnergyFraction[JetInfo[iJetColl].nJet]      = jet->electronEnergyFraction();
      JetInfo[iJetColl].TagVar_muonEnergyFraction[JetInfo[iJetColl].nJet]          = jet->muonEnergyFraction();
      JetInfo[iJetColl].TagVar_chargedHadronMultiplicity[JetInfo[iJetColl].nJet]   = jet->chargedHadronMultiplicity();
      JetInfo[iJetColl].TagVar_neutralHadronMultiplicity[JetInfo[iJetColl].nJet]   = jet->neutralHadronMultiplicity();
      JetInfo[iJetColl].TagVar_photonMultiplicity[JetInfo[iJetColl].nJet]          = jet->photonMultiplicity();
      JetInfo[iJetColl].TagVar_electronMultiplicity[JetInfo[iJetColl].nJet]        = jet->electronMultiplicity();
      JetInfo[iJetColl].TagVar_muonMultiplicity[JetInfo[iJetColl].nJet]            = jet->muonMultiplicity();
      JetInfo[iJetColl].TagVar_neutralEmEnergyFraction[JetInfo[iJetColl].nJet] = jet->neutralEmEnergyFraction();
      JetInfo[iJetColl].TagVar_numberOfDaughters[JetInfo[iJetColl].nJet] = jet->numberOfDaughters();
      JetInfo[iJetColl].TagVar_chargedMultiplicity[JetInfo[iJetColl].nJet] = jet->chargedMultiplicity();
      JetInfo[iJetColl].TagVar_chargedEmEnergyFraction[JetInfo[iJetColl].nJet] = jet->chargedEmEnergyFraction();
      JetInfo[iJetColl].TagVar_neutralMultiplicity[JetInfo[iJetColl].nJet] = jet->neutralMultiplicity();
    }


  }// over jets


  return;
}



template<typename IPTI,typename VTX>
template<typename JetColl>
bool BTagHLTAnalyzerT<IPTI,VTX>::havePassingJets(const edm::Handle<JetColl>& jetsColl)
{
  for ( typename JetColl::const_iterator jet = jetsColl->begin(); jet != jetsColl->end(); ++jet ) {

    double ptjet  = jet->pt()  ;
    double etajet = jet->eta() ;

    if( ptjet < minJetPt_ || std::fabs( etajet ) > maxJetEta_ ) continue;

    return true;
  }

  return false;
}




// ------------ method called once each job just before starting event loop  ------------
template<typename IPTI,typename VTX>
void BTagHLTAnalyzerT<IPTI,VTX>::beginJob() {
}


// ------------ method called once each job just after ending the event loop  ------------
template<typename IPTI,typename VTX>
void BTagHLTAnalyzerT<IPTI,VTX>::endJob() {
}







// -------------------------------------------------------------------------
// NameCompatible
// -------------------------------------------------------------------------
template<typename IPTI,typename VTX>
bool BTagHLTAnalyzerT<IPTI,VTX>::NameCompatible(const std::string& pattern, const std::string& name)
{
  const boost::regex regexp(edm::glob2reg(pattern));

  return boost::regex_match(name,regexp);
}















template<>
void BTagHLTAnalyzerT<reco::CandIPTagInfo,reco::VertexCompositePtrCandidate>::vertexKinematicsAndChange(const reco::Vertex & vertex, reco::TrackKinematics & vertexKinematics, Int_t & charge)
{
  Bool_t hasRefittedTracks = vertex.hasRefittedTracks();

  for(reco::Vertex::trackRef_iterator track = vertex.tracks_begin();
      track != vertex.tracks_end(); ++track) {
    Double_t w = vertex.trackWeight(*track);
    if (w < 0.5)
      continue;
    if (hasRefittedTracks) {
      reco::Track actualTrack = vertex.refittedTrack(*track);
      vertexKinematics.add(actualTrack, w);
      charge+=actualTrack.charge();
    }
    else {
      const reco::Track& mytrack = **track;
      vertexKinematics.add(mytrack, w);
      charge+=mytrack.charge();
    }
  }
}


template<>
void BTagHLTAnalyzerT<reco::CandIPTagInfo,reco::VertexCompositePtrCandidate>::vertexKinematicsAndChange(const Vertex & vertex, reco::TrackKinematics & vertexKinematics, Int_t & charge)
{
  const std::vector<reco::CandidatePtr> & tracks = vertex.daughterPtrVector();

  for(std::vector<reco::CandidatePtr>::const_iterator track = tracks.begin(); track != tracks.end(); ++track) {
    const reco::Track& mytrack = *(*track)->bestTrack();
    vertexKinematics.add(mytrack, 1.0);
    charge+=mytrack.charge();
  }
}




template<typename IPTI,typename VTX>
void BTagHLTAnalyzerT<IPTI,VTX>::setTracksPVBase( const reco::Track & track, const edm::Handle<reco::VertexCollection> & pvHandle, int & iPV, float & PVweight )
{
  iPV = -1;
  PVweight = 0.;

  //const reco::TrackBaseRef trackBaseRef( trackRef );

  typedef reco::VertexCollection::const_iterator IV;
  typedef reco::Vertex::trackRef_iterator IT;

  for(IV iv=pvHandle->begin(); iv!=pvHandle->end(); ++iv)
  {
    const reco::Vertex & vtx = *iv;
    // loop over tracks in vertices
    for(IT it=vtx.tracks_begin(); it!=vtx.tracks_end(); ++it)
    {
      const reco::TrackBaseRef & baseRef = *it;
      // one of the tracks in the vertex is the same as the track considered in the function

      float deltaR = reco::deltaR( baseRef->eta(), baseRef->phi(),
				   track.eta(), track.phi());

      if( deltaR < 0.001)
      {
        float w = vtx.trackWeight(baseRef);
        // select the vertex for which the track has the highest weight
        if( w > PVweight )
        {
          PVweight = w;
          iPV = ( iv - pvHandle->begin() );
          break;
        }
      }
    }
  }
}

// -------------- setTracksSV ----------------
template<typename IPTI,typename VTX>
void BTagHLTAnalyzerT<IPTI,VTX>::setTracksSV(const TrackRef & trackRef, const SVTagInfo * svTagInfo, int & isFromSV, int & iSV, float & SVweight)
{
  isFromSV = 0;
  iSV = -1;
  SVweight = 0.;

  size_t nSV = svTagInfo->nVertices();
  for(size_t iv=0; iv<nSV; ++iv)
  {
    const Vertex & vtx = svTagInfo->secondaryVertex(iv);
    const std::vector<reco::CandidatePtr> & tracks = vtx.daughterPtrVector();
    
    auto trackMatch = std::find(tracks.begin(),tracks.end(),trackRef);
    // one of the tracks in the vertex is the same as the track considered in the function
    if( trackMatch != tracks.end() )
    {
      SVweight = 1.;
      isFromSV = 1;
      iSV = iv;
    }

    // select the first vertex for which the track is used in the fit
    // (reco::VertexCompositePtrCandidate does not store track weights so can't select the vertex for which the track has the highest weight)
    if(iSV>=0)
      break;
  }
}

template<typename IPTI,typename VTX>
void BTagHLTAnalyzerT<IPTI,VTX>::setTracksSV(const TrackRefCalo & trackRef, const reco::SecondaryVertexTagInfo * svTagInfo, int & isFromSV, int & iSV, float & SVweight)
{
  isFromSV = 0;
  iSV = -1;
  SVweight = 0.;

  //const reco::TrackBaseRef trackBaseRef( trackRef );

  typedef reco::Vertex::trackRef_iterator IT;

  size_t nSV = svTagInfo->nVertices();
  for(size_t iv=0; iv<nSV; ++iv)
  {
    const reco::Vertex & vtx = svTagInfo->secondaryVertex(iv);
    // loop over tracks in vertices
    for(IT it=vtx.tracks_begin(); it!=vtx.tracks_end(); ++it)
    {
      const reco::TrackBaseRef & baseRef = *it;
      // one of the tracks in the vertex is the same as the track considered in the function
      float deltaR = reco::deltaR( baseRef->eta(), baseRef->phi(),
				   trackRef->eta(), trackRef->phi());

      if( deltaR < 0.001)
      {
        float w = vtx.trackWeight(baseRef);
        // select the vertex for which the track has the highest weight
        if( w > SVweight )
        {
          SVweight = w;
          isFromSV = 1;
          iSV = iv;
          break;
        }
      }
    }
  }
}


// define specific instances of the templated BTagHLTAnalyzer
typedef BTagHLTAnalyzerT<reco::CandIPTagInfo,reco::VertexCompositePtrCandidate> BTagHLTAnalyzer;
//define plugins
DEFINE_FWK_MODULE(BTagHLTAnalyzer);
