from queue import PriorityQueue

class Astar:
    def __init__(self, start, goal):
        self.paths = []
        self.openlist = PriorityQueue()
        self.closedlist = []
        self.start = start
        self.goal = goal
        self.totalcost = 0

    def getMinHeuristic(self):
        return self.openlist.get()

    def aStarRes(self, g1):
        if (self.goal == self.start):
            return [self.goal]
        #inisialisasi
        self.paths = []
        self.closedlist = []
        self.openlist = PriorityQueue()
        g1.setHeuristic(self.goal)
        self.totalcost = 0

        #Isi List : (<total weight>, <node tujuan>, <node sekarang>)
        currNode = self.start
        currWeight = 0
        #self.closedlist.append(tuple(self.start, g1.Node[self.start][2], self.start))
        self.openlist.put((g1.Node[self.start][2], self.start, self.start))

        while(currNode != self.goal and self.openlist.qsize()):
            temp_buffer = self.getMinHeuristic()
            self.closedlist.append(temp_buffer)
            currNode = temp_buffer[1]

            #terbentuk rute dari start node ke goal node
            if self.goal in g1.graf[temp_buffer[1]].keys():
                if(len(self.closedlist) == 1):
                    return [self.start, self.goal]
                self.paths.append(self.goal)
                self.paths.append(temp_buffer[1])
                temp_node = temp_buffer[2]
                for i in range(len(self.closedlist)):
                    if(self.closedlist[len(self.closedlist)-i-1][1] == temp_node):
                       self.paths.append(self.closedlist[len(self.closedlist)-i-1][1])
                       temp_node = self.closedlist[len(self.closedlist)-i-1][2]
                return self.paths[::-1]

            #buat state anak & dimasukkan ke openlist
            for child in g1.graf[currNode].keys():
                if(child != currNode):
                    self.openlist.put(((g1.Node[child][2] + currWeight + g1.graf[currNode][child]), child, currNode))

        return []

    def Solve(self, g1):
        return self.aStarRes(g1), self.totalcost