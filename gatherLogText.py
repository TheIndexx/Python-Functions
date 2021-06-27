import sys
import os
# Call parameters are as follows: (function.py), TR_Dump.log path, run name


# Get Dump Log Path and Run Name

# filePath = input('Enter TR_dump.log path: ')
# runName = input('Enter run name: ')

# Open and Read File

file = open(sys.argv[1], "r")
fileContents = file.read()

def getLogText():
    allRuns = fileContents.split('NEW RUN') # Split file contents by New Run into array
    length = len(allRuns) # Check length of array
    x = -1
    runNum = 0
    for i in allRuns: # Loop through array
        x += 1
        if sys.argv[2] in i:
            runNum = x # If run name in run, save run location as var runNum
    print(allRuns[runNum]) # Print all the contents of run with run name
    return True

getLogText() # Call Function