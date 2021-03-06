import sys
import re

# Get Dump Log Path, Run Name, Layer Number
# Call parameters are as follows: (function.py), TR_Dump.log path, run Num, layer number

# filePath = input('Enter TR_dump.log path: ')
# runNum = input('Enter run name: ')
# userLayerNum = input('Enter layer number: ')

# Open and Read File

file = open(sys.argv[1], "r")
fileContents = file.read()

runNum = int(sys.argv[2])

def getLayerText():
    allRuns = fileContents.split('NEW RUN') # Split file contents by New Run into array
    for i in allRuns[runNum:]: # Loop through array
        allLayers = re.findall(r'bottom(.+?)Number', i, flags=re.S) #Grabs all text containing layers
        allLines = allLayers[0].split('\n') #Puts all text from allLayers into array by line breaks
        for i in allLines: #Loop through each line
            if 'Layer' in i: #If 'Layer' is in line
                allLayerNum = [int(s) for s in i.split() if s.isdigit()] #Grab Layer number from line
                allLayerNum1 = allLayerNum[0] #Converts Layer number to int from array
                if int(allLayerNum1) == int(sys.argv[3]): #If layer number is same as user-requested layer number
                    layerIndex = allLines.index(i) #Find index of line from allLines array
                    endLayerIndex = layerIndex+13 #Find end of layer text
                    for line in allLines[layerIndex:endLayerIndex]:
                        print(line) #Print the Layer
                else:
                    print('Layer not found in file')
    return True

getLayerText()