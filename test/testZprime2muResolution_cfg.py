import FWCore.ParameterSet.Config as cms

from SUSYBSMAnalysis.Zprime2muAnalysis.Zprime2muAnalysisCommon_cff import *
from SUSYBSMAnalysis.Zprime2muAnalysis.Zprime2muResolution_cfi import *

files = [
    '/store/relval/CMSSW_2_1_10/RelValZMM/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v2/0000/04621FC6-9F99-DD11-9B7F-000423DD2F34.root',
    '/store/relval/CMSSW_2_1_10/RelValZMM/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v2/0000/060D150D-9899-DD11-ACC2-001617DBD472.root',
    '/store/relval/CMSSW_2_1_10/RelValZMM/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v2/0000/2444C906-9A99-DD11-B531-000423D174FE.root',
    '/store/relval/CMSSW_2_1_10/RelValZMM/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v2/0000/264D0836-FD99-DD11-A03C-000423D9A2AE.root',
    '/store/relval/CMSSW_2_1_10/RelValZMM/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v2/0000/2E69050E-A099-DD11-B17F-000423D9870C.root',
    '/store/relval/CMSSW_2_1_10/RelValZMM/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v2/0000/2EBACCA2-9D99-DD11-B1D6-001617C3B5E4.root',
    '/store/relval/CMSSW_2_1_10/RelValZMM/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v2/0000/4AD010CA-A099-DD11-8ADD-001617E30D06.root',
    '/store/relval/CMSSW_2_1_10/RelValZMM/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v2/0000/5C7BAA79-9F99-DD11-B86F-001617DF785A.root',
    '/store/relval/CMSSW_2_1_10/RelValZMM/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v2/0000/7EB9DF9E-9999-DD11-92B5-001617DF785A.root',
    '/store/relval/CMSSW_2_1_10/RelValZMM/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v2/0000/9E4859C3-A199-DD11-A7AF-000423D94700.root',
    '/store/relval/CMSSW_2_1_10/RelValZMM/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v2/0000/C6DE964B-A099-DD11-8552-000423D98FBC.root',
    '/store/relval/CMSSW_2_1_10/RelValZMM/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v2/0000/D6EC4DA6-A299-DD11-A76A-000423D94908.root',
    '/store/relval/CMSSW_2_1_10/RelValZMM/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v2/0000/D6ED1C9A-9899-DD11-98B0-001617DBD332.root',
    '/store/relval/CMSSW_2_1_10/RelValZMM/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v2/0000/DCD044F4-9699-DD11-82CC-000423D98920.root'
    ]

process = makeZprime2muAnalysisProcess(files)
attachResolution(process)

process.Zprime2muResolution.verbosity = 2
process.Zprime2muResolution.dateHistograms = False

# Example of how to replace one of the parameter sets (e.g. for
# running on the Z0->mumu sample above):
process.Zprime2muResolution.Z0params = cms.PSet(
    peakMass = cms.double(91.2),
    lowerMassWin = cms.double(0),
    upperMassWin = cms.double(300),
    binSize = cms.int32(25),
    maxTrigMass = cms.double(0.3)
    )
process.Zprime2muResolution.dataSet = 'Z0params'

#print process.dumpConfig()

