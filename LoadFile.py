from Graph import Graph
import math

def loadToGraf(filename, grafDest):
    filebuff = open("./"+filename)
    listofnode = []
    
    i = 0
    for item in filebuff:
        if (i == 0):
            count = int(item)
        elif(i < count+1):
            temp = item.strip().split(" ")
            grafDest.addNode(temp[0], float(temp[1]), float(temp[2]))
            listofnode.append(temp[0])
        else:
            temp1 = item.strip().split(" ")
            for j in range(len(temp1)):
                if(temp1[j] != "0" and temp1[j] != "0.0"):
                    tempX1, tempY1 = grafDest.getPos(listofnode[i-count-1])
                    tempX2, tempY2 = grafDest.getPos(listofnode[j])
                    tempWeight = math.sqrt(math.pow((tempX1 - tempX2),2) + math.pow((tempY1 - tempY2),2))
                    grafDest.addEdge(listofnode[i-count-1], listofnode[j], tempWeight)
                    #print(listofnode[i-count-1] + " " + listofnode[j])
        i += 1

'''
g1 = Graph()
loadToGraf("test.txt", g1)
for item in g1.graf.keys():
    print(item,end=" : ")
    for item2 in g1.graf[item].keys():
        print(str(item2), end=" ")
    print()
'''