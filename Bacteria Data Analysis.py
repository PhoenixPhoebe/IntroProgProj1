# Bacteria Data Analysis Project
#

def dataLoad(filename):
# Insert your code here

    filein = open(filename,"r")
    lines =filein.readlines()
    data = "".join(lines)
    return data


print(dataLoad("test.txt"))
#def dataStatistics(data, statistic):
# Insert your code here
#return result

#def dataPlot(data):
# Insert your code her
