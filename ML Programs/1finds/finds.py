import csv

csvfile=open('data.csv','r')
readcsv=csv.reader(csvfile,delimiter=',')
print(readcsv)
cdata=list()
for row in readcsv:
   if row[len(row)-1].upper()=='YES':
      cdata.append(row)

print("After cleaning the data (Only Positive Data)")
for i in cdata:
   print(i)

#Number of columns and rows
n=len(cdata[0])
nlines=len(cdata)
print("The data is of columns: ",n," and row :",nlines)


#Initial Hypothysis
h0=list()
for i in range(0,n-1):
    h0.append('#')

print("\n\n\n")
print("Initial hypothesis is given by ")
print(h0)

h=list()
#Append first line of cdata to the h
for i in range(0,n-1):
    h.append(cdata[0][i])

print("h 1:",h)



#Apply find(s) Algorithm
for i in range(1,nlines):
    for j in range(0,n-1):
        if h[j]!=cdata[i][j]:
           h[j]='?'
        else:
           h[j]=h[j]
    
    print("h",(i+1),":",h)


#Final hypothesis given by 
print("\n\n\n") 
print("Final hypothesis is :")
print(h)

       





