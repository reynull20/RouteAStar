import Graph, Astar, LoadFile
import networkx as nx
import matplotlib.pyplot as plt
import math

while(True):
    fn = input("Enter Graf File Name : ")
    g1 = Graph.Graph()
    GV = nx.Graph() #Untuk visualisasi
    LoadFile.loadToGraf(fn,g1,GV)
    Gres = GV
    print("Available Node :")
    i = 0
    for item in g1.graf.keys():
        if(i < 4):
            print(item, end=" | ")
        else:
            print(item)
            i = 0
        i += 1
    exit = False
    while(exit != True):
        print()
        nx.draw(GV,nx.get_node_attributes(GV,'pos'),with_labels = True)
        plt.show()
        s1 = input("Pick Source Node : ")
        s2 = input("Pick Goal Node : ")
        while((s1 not in g1.graf.keys()) and (s2 not in g1.graf.keys())):
            print("Invalid Node! input again")
            s1 = input("Pick Source Node : ")
            s2 = input("Pick Goal Node : ")
        ans = Astar.Astar(s1, s2)
        nx.draw(Gres,nx.get_node_attributes(GV,'pos'),with_labels = True)
        listans, sumAns = ans.Solve(g1)
        if(len(listans) != 0):
            for i in range(len(listans)-1):
                sumAns += g1.graf[listans[i]][listans[i+1]]
                
            print("Path : ")
            i = 0
            for item in listans:
                px, py = g1.getPos(item)
                plt.plot(px, py, marker = "o", markerfacecolor = 'w',markersize=20)
                if(i != 0):
                    print(" => ",end='')
                print(item, end='')
                i += 1
            print()
            print("Total Cost = " + str(sumAns))
            plt.show()
        else:
            print("There is no route available!")
        print()
        print("Test another Node?(Y/n) : ")
        exit = input()
        while(True):
            if(exit == "Y" or exit == "y"):
                exit = True
                break
            elif(exit == "n" or exit == "N"):
                exit = False
                break
            else:
                print("Invalid Input!")
                print("Test another Node?(Y/n) : ")
                exit = input()
