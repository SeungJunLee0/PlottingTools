#export alignmentName="data_CSC-1100-110001_2018UL_IOV1_CMSSW106_JSON-313041-320377_dataRun2_MuAl_v1_01"
export alignmentName="data_GEM-1100-110001_2018UL_IOV1_CMSSW106_JSON-313041-320377_dataRun2_MuAl_v1_01"

#xmlfile_ref="Geometries/data_CSC-1100-110001_2018UL_IOV2_CMSSW106_JSON-320377-322603_dataRun2_MuAl_v1_01.xml"
xmlfile_ref="Geometries/data_GEM-1100-110001_2018UL_IOV2_CMSSW106_JSON-320377-322603_dataRun2_MuAl_v1_01.xml"

referenceName="IOV3"

correctionName="Displacements from IOV3" 

runComparison=true
uploadComparison=false
runCorrelation=false
printCorrelationFactors=true

doDT="false"
#doCSC="true"
doCSC="false"
doGEM="true"

:<<'END'
if [ "$runComparison" = true ]; then
    echo output: OUTPUT/${alignmentName}.out.txt
    python PlotConfig_Generic.py $xmlfile_ref $doDT $doCSC $referenceName $correctionName > OUTPUT/${alignmentName}.out.txt -b
fi
END

if [ "$runComparison" = true ]; then
    echo output: OUTPUT/${alignmentName}.out.txt
    python PlotConfig_Generic.py $xmlfile_ref $doDT $doGEM $referenceName $correctionName $doCSC > OUTPUT/${alignmentName}.out.txt -b
fi

if [ "$uploadComparison" = true ]; then
    cd RESULT/
    echo "copying $alignmentName"
    scp -r $alignmentName ${USER}@lxplus.cern.ch:/afs/cern.ch/cms/CAF/CMSALCA/ALCA_MUONALIGN/www/tmp/
     echo "copied"
    cd ..
fi

if [ "$doDT" = true -a "$runCorrelation" = true ]; then
    python TMP_CREATE_CORRELATION_PLOTS_2.py $alignmentName $printCorrelationFactors $xmlfile_ref -b
fi

if [ "$doCSC" = true -a "$runCorrelation" = true ]; then
    python TMP_CREATE_CORRELATION_PLOTS_3.py $alignmentName $printCorrelationFactors -b
fi
if [ "$doGEM" = true -a "$runCorrelation" = true ]; then
    python TMP_CREATE_CORRELATION_PLOTS_4.py $alignmentName $printCorrelationFactors -b
fi
