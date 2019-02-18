import FWCore.ParameterSet.Config as cms

from SUSYBSMAnalysis.Zprime2muAnalysis.HardInteraction_cff import hardInteraction, hardInteraction_MiniAOD
from SUSYBSMAnalysis.Zprime2muAnalysis.TriggerDecision_cff import triggerDecision

EfficiencyFromMC = cms.EDAnalyzer('EfficiencyFromMC',
                                  hardInteraction = hardInteraction,
                                  triggerDecision = triggerDecision,
                                  check_l1 = cms.bool(True),
                                  trigger_summary_src = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
                                  nbins = cms.uint32(6000),
                                  min_mass = cms.double(0),
                                  max_mass = cms.double(6000),
                                  use_resonance_mass = cms.bool(False),
                                  use_resonance_mass_denom = cms.bool(False),
                                  dimuon_src = cms.InputTag('dimuons'),
                                  hlt_obj_src = cms.InputTag(''),
                                  hlt_single_min_pt = cms.double(50),
                                  hlt_single_max_eta = cms.double(2.4),
                                  checking_prescaled_path = cms.bool(False),
                                  acceptance_max_eta_1 = cms.double(2.4),
                                  acceptance_max_eta_2 = cms.double(2.4),
                                  acceptance_min_pt = cms.double(53),
                                  )

EfficiencyFromMCMini = cms.EDAnalyzer('EfficiencyFromMCMini',
                                  hardInteraction = hardInteraction_MiniAOD,
                                  triggerDecision = triggerDecision,
                                  check_l1 = cms.bool(True),
                                  #trigger_summary = cms.InputTag('selectedPatTrigger'),  # 80X
                                  trigger_summary = cms.InputTag('slimmedPatTrigger'),  # 92X
                                  bits = cms.InputTag("TriggerResults","","HLT"),
                                  nbins = cms.uint32(6000),
                                  min_mass = cms.double(0),
                                  max_mass = cms.double(6000),
                                  use_resonance_mass = cms.bool(False),
                                  use_resonance_mass_denom = cms.bool(False),
                                  dimuon_src = cms.InputTag('dimuons'),
                                  trigger_filters = cms.vstring(),
                                  trigger_path_names = cms.vstring(),
                                  hlt_obj_src = cms.InputTag(''),
                                  hlt_single_min_pt = cms.double(50),
                                  hlt_single_max_eta = cms.double(2.4),
                                  checking_prescaled_path = cms.bool(False),
                                  acceptance_max_eta_1 = cms.double(2.4),
                                  acceptance_max_eta_2 = cms.double(2.4),
                                  acceptance_min_pt = cms.double(53),
                                  )

EfficiencyFromMCnoTrigger = cms.EDAnalyzer('EfficiencyFromMCnoTrigger',
                                  hardInteraction = hardInteraction,
                                  triggerDecision = triggerDecision,
                                  check_l1 = cms.bool(True),
                                  trigger_summary_src = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
                                  nbins = cms.uint32(6000),
                                  min_mass = cms.double(0),
                                  max_mass = cms.double(6000),
                                  use_resonance_mass = cms.bool(False),
                                  use_resonance_mass_denom = cms.bool(False),
                                  dimuon_src = cms.InputTag('dimuons'),
                                  hlt_obj_src = cms.InputTag(''),
                                  hlt_single_min_pt = cms.double(50),
                                  hlt_single_max_eta = cms.double(2.4),
                                  checking_prescaled_path = cms.bool(False),
                                  acceptance_max_eta_1 = cms.double(2.4),
                                  acceptance_max_eta_2 = cms.double(2.4),
                                  acceptance_min_pt = cms.double(53),
                                  )
