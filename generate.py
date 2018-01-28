import random
import csv
with open("dataset3.csv",'wb') as csvfile:
    writer = csv.writer(csvfile,delimiter=',')
    n = 100
    writer.writerow(['P'+str(i) for i in range(n)])
    for i in range(n):
        p = []
        #writer.writerow([random.randint(0,1) for j in range(n)])
        for j in range(n):
            if(i==j):
                p.append(0)
            else:
                p.append(random.randint(0,1))
        writer.writerow(p)
