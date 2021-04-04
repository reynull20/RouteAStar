class Astar:
    def __init__(self):
        self.paths = {}
        self.openlist = []
        self.closedlist = []

    def getMinHeuristic(self):
        self.openlist.sort(key = lambda x: x[1])
        return self.openlist[0]

    def aStarRes(self, g1, source, dest):
        g1.setHeuristic(dest)

        #Isi List : (<node tujuan>, <total weight>, <node sekarang>)
        currNode = source
        currWeight = 0
        self.closedlist.append(tuple(source, g1.Node[source][2], source))

        while(currNode != dest):
            for item in g1.graf[currNode].keys():
                temp_nilai = g1.graf[currNode][item] + g1.Node[item][2] + currWeight
                self.openlist.append(tuple(item, temp_nilai, currNode))

            temp = self.getMinHeuristic()
            self.closedlist.append(temp)
            currNode = temp[0]

        return self.paths