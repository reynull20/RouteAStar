import Graph, Astar, LoadFile
import networkx as nx
import matplotlib.pyplot as plt

GV = nx.Graph()

g1 = Graph.Graph()
ans = Astar.Astar("R", "S")
LoadFile.loadToGraf("test.txt",g1,GV)
nx.draw(GV,nx.get_node_attributes(GV,'pos'))
greennodes = ans.Solve(g1)
for item in greennodes:
    print(item)
plt.plot(2,0,marker = 'o',markerfacecolor = 'r')
plt.show()
