import Graph, Astar, LoadFile

g1 = Graph.Graph()
ans = Astar.Astar("R", "S")
LoadFile.loadToGraf("test.txt",g1)
for item in ans.Solve(g1):
    print(item)