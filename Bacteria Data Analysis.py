# Bacteria Data Analysis Project

import numpy as np
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
    dataMatrix = np.array(dataMatrix)

    for x in dataMatrix:
        x[2] = int(x[2]) #sikre sig at der ikke kommer decimal tal som bakterie nr
        if float(x[0]) < 10 or float(x[0]) > 60: #tjekker om værdien i søjle 1 er mindre eller større end 60. kræver float, ellers tager den det som string
            dataMatrix = np.delete(dataMatrix, int(np.where(dataMatrix[:,0] == x[0])[0]), 0)
        elif float(x[1]) < 0: #tjekker om det er positivt
             dataMatrix = np.delete(dataMatrix, int(np.where(dataMatrix[:,1] == x[1])[0]), 0)
        elif int(x[2]) > 4 or int(x[2]) < 1: #tjekker om det ligger uden for 1 - 4, det er ikke behøvet at tjekke om decimal tal da det er klare længere oppe
             dataMatrix = np.delete(dataMatrix, int(np.where(dataMatrix[:,2] == x[2])[0]), 0)

    return(dataMatrix)

#dataLoad("test.txt")
print(dataLoad("test.txt"))
#def dataStatistics(data, statistic):
# Insert your code here
#return result

#def dataPlot(data):
# Insert your code her
