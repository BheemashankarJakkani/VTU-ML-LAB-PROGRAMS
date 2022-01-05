import numpy as np
import pandas as pd
import csv

data=pd.DataFrame(data=pd.read_csv('data.csv'))

target=np.array(data.iloc[:,-1])
concepts=np.array(data.iloc[:,:-1])

spech=concepts[0]
print(spech)

genh=[["?" for i in range(len(spech))] for j in range(len(spech))]

print(genh)
for i,h in enumerate(concepts):
    if target[i].upper()=="YES":
        for x in range(len(spech)):
            if h[x]!=spech[x]:
               spech[x]='?'
               genh[x][x]='?'
        #print(spech)
    if target[i].upper()=="NO":
       for x in range(len(spech)):
           if h[x]!=spech[x]:
              genh[x][x]=spech[x]
           else:
              genh[x][x]='?'

    print("spech",i," : ",spech)
    print("genh ",i," : ",genh)


index=list()
for i,h in enumerate(genh):
    if h==['?','?','?','?','?','?']:
       index.append(i)

for i in range(len(index)):
      genh.remove(['?','?','?','?','?','?'])


print("Final spech ",i," : ",spech)
print("Final genh ",i," : ",genh)



