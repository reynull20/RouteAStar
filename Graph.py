from Astar import Astar
import math

class Node:
    def __init__(self, node_name, posX, posY):
        self.name = node_name
        self.heuristic = 0
        self.posX = posX
        self.posY - posY

    def setHeuristic(self, goal):
        self.heuristic = math.sqrt(math.pow((self.posX - goal.posX),2) + math.pow((self.posY - goal.posY),2))

class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1.name
        self.node2 = node2.name
        self.weight = weight


class Graph:
    def __init__(self):
        self.graf = {}
        self.Node = {}

    def addEdge(self, froms, goals, weight):
        if (froms not in self.graf):
            self.graf[froms] = {}
        if (goals not in self.graf):
            self.graf[goals] = {}
        self.graf[froms][goals] = weight
        self.graf[goals][froms] = weight

    def getHeuristic(self, node):
        return self.Node[node][2]
    
    def getPos(self, node):
        return self.Node[node][0], self.Node[node][1]
    
    def addNode(self, nama, posX, posY):
        if (nama in self.Node.keys()):
            return

        self.Node[nama] = [posX, posY, 0]

    def setHeuristic(self, goals):
        for item in self.Node.keys():
            self.Node[item][2] = math.sqrt(math.pow((self.Node[item][0] - self.Node[goals][0]),2) + math.pow((self.Node[item][1] - self.Node[goals][1]),2))


'''
g1 = Graph()
g1.addNode('A', 40, 23)
g1.addNode('B', 23, 44)
g1.addNode('C', 74, 55)
g1.addNode('D', 24, 45)
g1.addEdge('A', 'B', 5)
g1.addEdge('B', 'C', 3)
g1.setHeuristic('C')
a1 = Astar()
'''