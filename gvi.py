import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import networkx as nx

import os

cwd = os.getcwd()
print("cwd = ", cwd)
floormappath = cwd + "\\data\\images\\floormapN17.jpeg"
resultspath = cwd + "\\data\\results\\"
print("floormappath = ",floormappath)
G = nx.cycle_graph(2)
pos =   {0:[0,0], 1:[ 300,  300]}
plt.figure(1)
img=mpimg.imread(floormappath)
plt.imshow(img)
plt.show()
nx.draw(G,pos)
plt.show()
plt.savefig(resultspath+'test.png')