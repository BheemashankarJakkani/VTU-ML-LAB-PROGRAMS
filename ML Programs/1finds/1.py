import numpy as np
import pandas as pd
import csv


file=open('data.csv','r')
readcsv=csv.reader(file,delimiter=',')
#print(readcsv)

cdata=list()

for row in readcsv:
    if row[len(row)-1].upper()=='YES':
       cdata.append(row)
print(cdata)

nlines=len(cdata)
ncol=len(cdata[0])

h=list()

for i in range(0,ncol-1):
    h.append(cdata[0][i])

print("initial hypothesis h1: ",h)


print(nlines,ncol)
for i in range(1,nlines):
    for j in range(0,ncol-1):
        if cdata[i][j]!=h[j]:
           h[j]='?'
        else:
           h[j]=h[j]
    print("h",(i+1),":",h)

print("Final hypothesis is given by ",h)

