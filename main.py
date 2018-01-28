import copy
import csv
import matplotlib.pyplot as plt
import numpy as np


class PageRanker:
    def __init__(self,iterations,scale,equilibrium=False):
        self.iterations = iterations
        self.equilibrium = equilibrium
        self.scale = scale
        #self.pages = []
        self.adjMatrix = []
        self.ranks = []

    def readdata(self,filename):
        with open (filename,'rb') as csvfile:
            reader = csv.reader(csvfile,delimiter=',')
            self.pages = reader.next()
            for row in reader:
                p = []
                for temp in row:
                    p.append(int(temp))
                self.adjMatrix.append(p)
        #print self.adjMatrix
        #print self.pages

    def updateRank(self,n):
        temp = copy.copy(self.ranks)
        for i in range(n):
            self.ranks[i] = 0
            for j in range(n):
                if(self.adjMatrix[i][j] == 1):
                    self.ranks[i] += temp[j]/self.outlinks[j]
        self.ranks = [round(x,3) for x in self.ranks]

    def ranker(self):
        n = len(self.pages)
        for i in range(n):
            self.ranks.append(1.0/n)
        self.outlinks = [sum(x) for x in zip(*self.adjMatrix)]
        if(self.equilibrium):
            temp = [0 for i in range(n)]
            while(temp!=self.ranks):
                temp = copy.copy(self.ranks)
                self.updateRank(n)
        else:
            for i in range(self.iterations):
                self.updateRank(n)
        for i in range(n):
            self.ranks[i] = self.ranks[i]*self.scale+(1-self.scale)/n
        #print self.ranks
        #print sum(self.ranks)


    def bargraph(self):
        y = np.arange(len(self.pages))
        plt.bar(y,self.ranks,align="center",alpha=0.5)
        plt.xticks(y,self.pages)
        plt.ylabel("Rank (0-1)")
        plt.title("PageRank Algorithm")
        plt.show()
        global filename
        plt.savefig(filename[:-4])

filename = raw_input("Enter dataset file : ")
equ = raw_input("Run until Equilibrium?(y/n) : ")
scale = float(raw_input("Enter Scaling Factor(b/w 0.8 and 0.9 recommended & 1 in case of no scaling) : "))
if(equ == 'y'):
    p = PageRanker(0,scale,True)
else:
    iterations = int(raw_input("Enter no. of iterations : "))
    p = PageRanker(iterations,scale)
p.readdata(filename)
p.ranker()
p.bargraph()
