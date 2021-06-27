import os
import re
import sys

## Finds TR_dump.log file given Run Name

## Format: function.py dumpName dirName(optional)
## Ex: gatherDumpFile.py TR_ex__1313__10-03-2021.dump C:/MonteCarloSimulations/Batch4
## Ex: gatherDumpFile.py TR_ex__1313__10-03-2021.dump

condensedName = ''

# Takes any user argument that contains the dump name and isolates the name
# Example: user argument = TR_ex__1313__10-03-2021.dump
#          isolated name = 1313__10-03-2021
def shortenName():
    global condensedName
    userRunName = sys.argv[1]
    K = 4

    temp = re.search('\d{% s}'% K, userRunName)
    res = (temp.group(0) if temp else '')

    userRunName2 = userRunName.split(str(res))
    userRunName3 = userRunName2[1]

    temp1 = re.search('\d{% s}'% K, userRunName3)
    res1 = (temp1.group(0) if temp else '')

    condensedNameSplit = userRunName3.split(str(res1))
    condensedName1 = condensedNameSplit[0] + str(res1)
    condensedName = str(str(res) + condensedName1)

# Grabs files with .log from given directory path
def getLogFile(directoryPath):
    for file in os.listdir(directoryPath):
        if file.endswith(".log"):
            print(os.path.join(directoryPath, file))

# If user only enters 2 arguments (function.py and dump name), search current working folder for TR_dump.log file
def currentDir():
    dirName = os.path.dirname(os.path.realpath(__file__))
    for root, subdirs, files in os.walk(dirName):
        for filename in files:
            if condensedName in filename:
                name_path = os.path.join(root,filename)
                dir_path = os.path.dirname(name_path)
                getLogFile(dir_path)
                break

# If user enters 3 arguments (function.py, dump name and directory), search directory
def givenDir():
    dirName = sys.argv[2]
    for root, subdirs, files in os.walk(dirName):
        for filename in files:
            if condensedName in filename:
                name_path = os.path.join(root,filename)
                dir_path = os.path.dirname(name_path)
                getLogFile(dir_path)
                break

if len(sys.argv) != 3:
    shortenName()
    currentDir()
else:
    shortenName()
    givenDir()