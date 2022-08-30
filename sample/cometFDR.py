import sys

inputPath = sys.argv[1]
outputPath = sys.argv[2]
decoyCharacter = sys.argv[3]   #"XXX_"
FDR = float(sys.argv[4])  #0.01
chooseMethod = int(sys.argv[5]) #1 # 0 == TDS, 1 == cTDS

inputFile = open(inputPath,'r')
outputFile = open(outputPath,'w')

def reversedProb(prob):
    if prob != 0:
        reverseProb = 1/prob
    else:
        reverseProb = 0
    return reverseProb

tCount = 0
dCount = 0
fdrTarget = 0
fdrDecoy = 0
targetProb = 0
decoyProb = 0
tProbCount = 0
dProbCount = 0
count = 0
flag = "T"

totalList = []

for line in inputFile:
    if line[0] == "C" or line[0] =="s":
        outputFile.write(line)
    else:
        tmp = line.split("\t")
        count = 0
        
        proteinList = tmp[15].split(",")
        for protein in proteinList:
            if decoyCharacter in protein:
                count += 1

######################################################
                
        if chooseMethod == 0:
            if len(proteinList) == count:
                dCount += 1
                dProbCount += reversedProb(decoyProb)
                flag = "D"
            else:
                totalList.append(line)
                tProbCount += reversedProb(targetProb)
                tCount += 1
                flag = "T"

            if (dCount+1)/tCount <= FDR and flag == "T":
                fdrTarget = tCount
                fdrDecoy = dCount
                
######################################################
                
        if chooseMethod == 1:
            targetProb = int(tmp[18]) / (int(tmp[18]) + int(tmp[19]))
            decoyProb = int(tmp[19]) / (int(tmp[18]) + int(tmp[19]))

            if len(proteinList) == count:
                dCount += 1
                dProbCount += reversedProb(decoyProb)
                flag = "D"
            else:
                totalList.append(line)
                tProbCount += reversedProb(targetProb)
                tCount += 1
                flag = "T"

            if dProbCount/tProbCount <= FDR and flag == "T":
                fdrTarget = tCount
                fdrDecoy = dCount

for i in range(0, fdrTarget):
    outputFile.write(totalList[i])
        
print(str(fdrTarget) + " " + str(fdrDecoy))

inputFile.close()
outputFile.close()
