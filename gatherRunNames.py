import sys
import os
from inspect import getsourcefile
from os.path import abspath

directoryName = input('Enter Dump log folder directoru (will parse through sub-directories too): ')
runName = input('Enter run name: ')

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