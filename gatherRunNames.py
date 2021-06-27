import sys
import os
from inspect import getsourcefile
from os.path import abspath
# Call parameters are as follows: (function.py), Dump folder, Dump file path, run name
# If using Dump folder, put - in second parameter, if using Dump file put - in first parameter


# directoryName = input('Enter Dump log folder directoru (will parse through sub-directories too): ')
directoryName = sys.argv[1]
# runName = input('Enter run name: ')
runName = sys.argv[3]
directoryFile = sys.argv[2]

if directoryFile == '-':
    for subdir, dirs, files in os.walk(directoryName):
        for filename in files:
            filepath = subdir + os.sep + filename

            if filepath.endswith(".log"):
                with open(os.path.join(directoryName, filepath)) as f:
                    content = f.read()
                    if runName in content:
                        print("Run was found in: " + f.name)
                        jojo = content.split('NEW RUN')
                        length = len(jojo)
                        for i in range(length):
                            lineNum = -1
                            lineNum2 = 0
                            eachSim = jojo[i]

                            simLines = eachSim.split('\n')
                            for line in simLines:
                                lineNum += 1
                                if 'names = ' in line:
                                    lineNum2 = lineNum

                            eachLine = simLines[lineNum2]
                            simName = eachLine.split('names = ')
                            if len(simName) > 1:
                                print("All Runs in TR_Dump log: " + '\n' + simName[1])
elif directoryName == '-': 
    openFile = open(directoryFile, 'r')
    content = openFile.read()
    jojo = content.split('NEW RUN')
    length = len(jojo)
    for i in range(length):
        lineNum = -1
        lineNum2 = 0
        eachSim = jojo[i]

        simLines = eachSim.split('\n')
        for line in simLines:
            lineNum += 1
            if 'names = ' in line:
                lineNum2 = lineNum

        eachLine = simLines[lineNum2]
        simName = eachLine.split('names = ')
        if len(simName) > 1:
            print("All Runs in TR_Dump log: " + '\n' + simName[1])
else:
    print('Incorrect parameter input')