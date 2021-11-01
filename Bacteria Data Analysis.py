# Bacteria Data Analysis Project

import numpy as np
from numpy.lib.shape_base import split
#Todo Error Handling



def dataLoad(filename):

    filein = open(filename,"r")
    lines =filein.readlines()
    data = "".join(lines).split() #den ligger alle linjerne sammen i en string, som så bliver splittet op med hver værdier i en liste
    dataMatrix = []
    #while loop løber så længe data listen ikke er tom.
    while data != []:
        dataMatrix.append(data[:3]) #tager de første tre på listen og ligger i matrixen
        data = data[3:] #ligger alle på nær de første tre i samme variable (fjerner de første tre)
    
    return np.array(dataMatrix)

print(dataLoad("test.txt"))
#print(dataLoad("test.txt"))
#def dataStatistics(data, statistic):
# Insert your code here
#return result

#def dataPlot(data):
# Insert your code her
