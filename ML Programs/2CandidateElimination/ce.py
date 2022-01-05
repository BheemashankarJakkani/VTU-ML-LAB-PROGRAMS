import csv
import os
import numpy as np

def candidateElimination():
    
    data=[]
    csvfile=open('data.csv','r')
    reader=csv.reader(csvfile,delimiter=',')
  
    for row in reader:
        data.append(np.array(row))

    #convert to numpy array
    data=np.asarray(data,dtype='object')
   
    x=data[:,:-1]
    y=data[:,-1].reshape(x.shape[0],1)

    print("\nTraining Data");
    print(x);
    print("\nLabels:")
    print(y) 

    print("\n Shape of x :")
    print(x.shape)
    print("\n Shape of y :")
    print(y.shape)

    specific=["%" for _ in range(x.shape[1])]
    specific=np.asarray(specific,dtype='object')

    general=["?" for _ in range(x.shape[1]) for _ in range(x.shape[1])]
    general=np.asarray(general,dtype='object')
  
    print("\n Initial specific Hypothesis :")
    print(specific)
 
    print("\nInitial General Hypothesis :");
    print(general)

   # Set first positive example to Hypothesis
    if y[0]=="P":
       specific=x[0]
    else:
      for i in range(y.shape[0]):
          if y[i]=="P":
             specific=x[i]
             break

    print("\n Candidate  Elimination")
 
    #for each training example
    for i in range(x.shape[0]):
      
       #positive example
       if y[i]=="P":
          for j in range(x.shape[1]):
              if x[i][j]!=specific[j]:
                 specific[j]="?"
 
              if specific[j]!=general[j][j] and general[j][j]!="?":
                 general[j][j]="?"
 
          print("\n ---------Step" +str(i+1)+ "---------\n")
          print("\n Specific Set: ")
          print(specific)
          print("\n General Set: ")
          print(general)
          print("\n-----------------------------\n")


      #negative Example
       else:
          for j in range(x.shape[1]):
              if x[i][j]!=specific[j]:
                  general[j][j]=specific[j]
 
          print("\n--------Step" +str(i+1)+ "--------\n")
          print("\nSpecific set : ")
          print(specific)
          print("\nGeneral Set :")
          print(general)
          print("\n")


    print("\n Final Specific Hypothesis : ")
    print(specific)
    print("\n Final General Hypotheis : ")
    print(general)
    print("\n")





candidateElimination()   


















         














 

  
