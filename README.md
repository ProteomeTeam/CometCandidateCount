# CometCandidateCount (Comet-CC)

Comet-CC is an modified version of the comet to output target and decoy candidate peptides.
We can estimate cTDS using target and decoy candidate peptides generated from Comet-CC.

Comet-CC can be searched the same as Comet. (using sample database and sample dataset)
==> comet.exe -Dhuman_SwissProt_R.fast -Pcomet.params.human.new -NsampleSearchResult sample.mgf
-D: database file path
-P: paramter file path
-N: outputfile name path
last mgf file path

We remove duplicate scan and e-value sorting of search results with removeDuplicationAndSort.jar (applied sequentially)
==> java -jar removeDuplicationAndSort.jar sampleSearchResult.txt sampleSearchResult.reName.txt
1. inputReuslt file path
2. outputResult file path

Then, we estimate the FDR. (applied sequentially)
==> python cometFDR.py sampleSearchResult.reName.txt sampleSearchResult.reName.1%.TDS.txt "XXX_" 0.01 0
1. input file path
2. output file path
3. decoyCharacter (ex "XXX_")
4. FDR (ex 0.01)
5. chooseMethod (ex TDS == 0, cTDS == 1)
