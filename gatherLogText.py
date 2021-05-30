import sys
import os

# Get Dump Log Path and Run Name

filePath = input('Enter TR_dump.log path: ')
runName = input('Enter run name: ')

# Open and Read File

file = open(filePath, "r")
fileContents = file.read()

def getLogText():
    allRuns = fileContents.split('NEW RUN') # Split file contents by New Run into array
    length = len(allRuns) # Check length of array
    x = -1
    runNum = 0
    for i in allRuns: # Loop through array
        x += 1
        if runName in i:
            runNum = x # If run name in run, save run location as var runNum
    print(allRuns[runNum]) # Print all the contents of run with run name
    return True

getLogText() # Call Function