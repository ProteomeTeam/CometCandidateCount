# CometCandidateCount (Comet-CC)

** The modified code to output the number of target and decoy candidate peptides is output only as a .txt file.

The original version of Comet can be downloaded from http://comet-ms.sourceforge.net.

Comet-CC is an modified version of the comet to output target and decoy candidate peptides.
We can estimate cTDS using target and decoy candidate peptides generated from Comet-CC.

Comet-CC can be searched the same as Comet. (using sample database and sample dataset)

==> comet.exe -Dhuman_sample_R.fast -Pcomet.params.human.new -NsampleSearchResult sample.mgf

1. -D: database file path
2. -P: paramter file path
3. -N: outputfile name path
4. last mgf file path

We remove duplicate scans and sort the e-value of search results with removeDuplicationAndSort.jar (applied sequentially)

==> java -jar removeDuplicationAndSort.jar sampleSearchResult.txt sampleSearchResult.reName.txt
1. inputReuslt file path
2. outputResult file path

Then, we estimate the FDR. (applied sequentially)

==> python cometFDR.py sampleSearchResult.reName.txt sampleSearchResult.reName.1%.TDS.txt "XXX_" 0.01 0

==> python cometFDR.py sampleSearchResult.reName.txt sampleSearchResult.reName.1%.cTDS.txt "XXX_" 0.01 1
1. input file path
2. output file path
3. decoyCharacter (ex "XXX_")
4. FDR (ex 0.01)
5. chooseMethod (ex TDS == 0, cTDS == 1)
