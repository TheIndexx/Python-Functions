# Only input is tissue model text
# Example input:
"""/************************************************/
*                   NEW RUN ...                 */
/************************************************/
Created on Wed Mar 10 10:14:00 2021
 
	names = ex(fl)__1014__10-03-2021.dump
	numberofphotons = 3.000000E+08
#of layers: 1 
index at top surface = 1.47 
index at bottom surface = 1.47 
	Layer 0 :
	mua_x = 0.141 [1/cm] 
	mus_x = 117 [1/cm] 
	mua_m = 0 [1/cm] 
	mus_m = 0 [1/cm] 
	muaf_x = 0 [1/cm] 
	flqy= 0 
	g_x =  0.9 
	g_m =  0 
	z-top = 0.000E+00 [cm] 
	z-bottom = 1.000E+02 [cm] 
	refractive index = 1.4 
	TAU (for this layer) = 0 [s] 
Number of detector positions 25 
	 0.1 cm	 0.2 cm	 0.3 cm	 0.4 cm	 0.5 cm	 0.6 cm	 0.7 cm	 0.8 cm	 0.9 cm	 1 cm	 1.1 cm	 1.2 cm	 1.3 cm	 1.4 cm	 1.5 cm	 1.6 cm	 1.7 cm	 1.8 cm	 1.9 cm	 2 cm	 2.1 cm	 2.2 cm	 2.3 cm	 2.4 cm	 2.5 cm
Time Resolution is 1.00E-02 (ns)
SOURCE_FIBER_RADIUS = 2.00E-02 (cm)
Numerical Aperture = 2.00E-02 
	Maximum acceptance angle (in air) = 90 
MAXTIMEOFFLIGHT = 6.00E-09 (s) 
Vel of light, c = 3.00E+10 (cm/s) 
Photon Weight Attenuation using BEERS LAW
Total random #s generated = 1.409120E+12 
Photons absorbed:
	ex = 0.000000E+00; fl = 0.000000E+00; total = (0.000000E+00)
Photons transmitted:
	ex = 0.000000E+00; fl = 0.000000E+00; total = (0.000000E+00)
Photons remitted:
	ex = 0.000000E+00; fl = 0.000000E+00; total = (0.000000E+00)
R_d (ex/fl): 
	R_ex = 0.000000E+00; R_fl = 0.000000E+00; R_total = (0.000000E+00)
T_d (ex/fl): 
	T_ex = 0.000000E+00; T_fl = 0.000000E+00; T_total = (0.000000E+00)
Local abs (ex/fl): 
	ex_abs = 0.000000E+00; fl_abs = 0.000000E+00; tot_abs = (0.000000E+00)

****************************
""" 
# Output: Input File according to format on 'A User Manual for Time-Resolved Monte Carlo Simulations of Photon Transport in Turbid Media'

def createInputFile(inputText):

    def findInItem(str, listToParse):
        for item in listToParse:
            if str in item:
                return item
    
    inputFile = []
    inputLines = inputText.split('\n')
    endlayerIndex = [i for i,x in enumerate(inputLines) if 'TAU' in x]
    startlayerIndex = [i for i,x in enumerate(inputLines) if 'Layer' in x]
    layerNum = -1

    inputFile.append(findInItem('numberofphotons', inputLines).split('= ')[1])
    inputFile.append('1')
    inputFile.append(findInItem('index at top surface', inputLines).split('= ')[1])
    inputFile.append(findInItem('index at bottom surface', inputLines).split('= ')[1])
    inputFile.append(findInItem('#of layers', inputLines).split(': ')[1])
    inputFile.append(findInItem('index at bottom surface', inputLines).split('= ')[1])
    for startlayerInd in startlayerIndex:
        layerNum += 1
        layerTxt = inputLines[startlayerInd: endlayerIndex[layerNum] + 1]
        inputFile.append('#layer ' + str(layerNum))
        inputFile.append(findInItem('mua_x', layerTxt).split('= ')[1].split(' [')[0])
        inputFile.append(findInItem('mus_x', layerTxt).split('= ')[1].split(' [')[0])
        inputFile.append(findInItem('mua_m', layerTxt).split('= ')[1].split(' [')[0])
        inputFile.append(findInItem('mus_x', layerTxt).split('= ')[1].split(' [')[0])
        inputFile.append(findInItem('muaf_x', layerTxt).split('= ')[1].split(' [')[0])
        inputFile.append(findInItem('flqy', layerTxt).split('= ')[1])
        inputFile.append(findInItem('g_x', layerTxt).split('= ')[1])
        inputFile.append(findInItem('g_m', layerTxt).split('= ')[1])
        inputFile.append(findInItem('z-bottom', layerTxt).split('= ')[1].split(' [')[0])
        inputFile.append(findInItem('refractive index', layerTxt).split('= ')[1])
        inputFile.append(findInItem('TAU', layerTxt).split('= ')[1].split(' [')[0])
    return inputFile

if __name__ == "__main__":
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    inputText = '\n'.join(lines)
    for line in createInputFile(inputText):
        print(line)