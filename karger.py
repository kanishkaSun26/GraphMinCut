import math
import random
import numpy as np
from copy import deepcopy as dp

def readGraph():
    graph={}
    with open('graph.txt') as read:
        for string in read:
            data=[int(x) for x in string.split("\t")[:-1]]
            data=np.asarray(data)
            graph.update({data[0]:data[1:]})
    return graph

def contract(g,i,j):
    g[i]=np.concatenate((g[i],g[j]),axis=None)
    g.pop(j)
    for k in g.keys():
        g[k][g[k]==j]=i
    g[i]=np.delete(g[i],np.where(g[i]==i))
    return(g)

def getVertices(g):
    i=random.choice(list(g.keys()))
    j=random.choice(g[i])
    return i,j

def main():
    graph=readGraph()
    n=len(graph)
    mincut=n**2
    for p in range(0,1000):#(n**2)*math.log(n)):
        g=dp(graph)
        while(len(g)>2):
            i,j=getVertices(g)
            g=contract(g,i,j)
        mincut=min(mincut,len(g[i]))
    return graph,mincut

graph,mincut=main()
print(mincut)