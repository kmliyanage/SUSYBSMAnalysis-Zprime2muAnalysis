# SUSYBSMAnalysis-Zprime2muAnalysis
HEEP
cmsrel CMSSW_10_2_5
cd CMSSW_10_2_5/src/
cmsenv
git clone -b mini-AOD-2018 git@github.com:kmliyanage/SUSYBSMAnalysis-Zprime2muAnalysis.git
mkdir SUSYBSMAnalysis
mv SUSYBSMAnalysis-Zprime2muAnalysis SUSYBSMAnalysis/Zprime2muAnalysis
scram b
