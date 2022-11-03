import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import networkx as nx
#cols = all links
#rows = 250
df = pd.read_excel("C:/Users/chhem/OneDrive/Desktop/Project/FY/Dataset/1_data.xlsx")
df1 = pd.read_excel("C:/Users/chhem/OneDrive/Desktop/Project/FY/Dataset/1_links.xlsx")
df.dropna()
df1.dropna()
l = df1[0].tolist()  #all links
m = df[0].tolist()
size = len(m)
total = len(l)
rows = size
cols = total
mat = np.zeros((rows,cols))
#mat = [[0]*cols for _ in range(rows)]
#print(mat)
for i in range(size):
    first = df.iloc[i,:].tolist()
    first.pop(0)
    first.pop(0)
    c = 0
    for j in first:
        if j in l:
            index = l.index(j)
            mat[i][index] = 1
        """ print(i)
        print(c) """
        c = c+1
#print(first)
#first = df.iloc[0,:]
#print(mat)
""" G = nx.from_numpy_matrix(np.array(mat))  
nx.draw(G, with_labels=True) 
 """
print("-----  OUT DEGREE-----")
for i in range(rows):
  c = 0
  for j in range(cols):
    if mat[i][j]==1:
      c=c+1
  print(m[i],c)

labeldict = {}
c = 0
for i in l:
  labeldict[str(c)] = i
  c = c+1

G = nx.DiGraph() 
for i in range(rows): 
 for j in range( cols): 
   if mat[i][j] == 1: 
      G.add_edge(i,j) 

nx.draw( G, with_labels=True) 
plt.show() 
