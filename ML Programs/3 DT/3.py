import numpy as np
import pandas as pd
import csv
import math
class Node:
        def __init__(self,l):
            self.label=l
            self.branches={}


def entropy(data):
    tot=len(data)
    pos=len(data.loc[data["Playtennis"]=='Y'])
    neg=len(data.loc[data["Playtennis"]=='N'])
    entropy=0
    if pos>0:
        entropy=(-1)*(pos/float(tot))*(math.log(pos,2)-math.log(tot,2))
    if neg>0:
        entropy=(-1)*(neg/float(tot))*(math.log(neg,2)-math.log(tot,2))
    
    return entropy   


def decision_tree(data):

    root=Node("NULL")
    
    if(entropy(data)==0):
           if(len(data.loc[data[data.columns[-1]] == 'Y']) == len(data)):
                  root.label="Y"
                  return root
           else:
                  root.label="N"
                  return root
    
    if(len(data.columns)==1):
          return 
 
    else:
          attrib=get_attrib(data)
          root.label=attrib
          values=set(data[attrib])

          for val in values:
                 root.branches[val]=decision_tree(data.loc[data[attrib]==val].drop(attrib,axis=1))
    
          return root


def get_attrib(data):
    entropy_s=entropy(data)
    attribute=""
    max_gain=0
    for attr in data.columns[:len(data.columns)-1]:
        g=gain(entropy_s,data,attr)
        
        if g>max_gain:
           max_gain=g
           attribute=attr

    return attribute

def gain(s,data,attr):
    gain=s
    values=set(data[attr])
    print(values)
    for val in values:
        gain-=len(data.loc[data[attr]==val])/float(len(data))*entropy(data.loc[data[attr]==val])
    return gain

def get_rules(root,rule,rules):
	if not root.branches:
		rules.append(rule[:-2]+" => "+root.label)
		return rules

	for i in root.branches:
		get_rules(root.branches[i],rule+root.label+"="+i+" ^ ",rules)
	return rules

def test(tree,test_str):
	if not tree.branches:
		return tree.label
	return test(tree.branches[test_str[tree.label]],test_str)


data=pd.read_csv('Data.csv')

entropy_s=entropy(data)
attrib_count = 0
cols = len(data.columns)-1

tree=decision_tree(data)

rules=get_rules(tree,"",[])
print(rules)

test_str={}

for i in data.columns[:-1]:
    test_str[i]=input(i+": ")

print(test_str)

print(test(tree,test_str))
 
