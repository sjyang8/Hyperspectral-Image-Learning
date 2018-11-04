#Import the library
import SimpSOM as sps
import os
from spectral import *
import scipy.io as sio

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "data/92AV3C.lan"
abs_file_path = os.path.join(script_dir, rel_path)
rel_path2 = "data/Indian_pines_gt.mat"
abs_file_path2 = os.path.join(script_dir,rel_path2)

gt = sio.loadmat(abs_file_path2)
gtd = gt['indian_pines_gt']

img = open_image(abs_file_path)
imgX = img.load()
imgX = imgX.reshape(145*145,220)
raw_data = imgX
#sps.run_colorsExample()
def HSI_SOM(x,y,data):
    net = sps.somNet(x,y,data,PBC=True)
    net.train(0.01,10)
    net.save('HSI_SOM_weights')
    return net
    
x = 145
y = 145
net = HSI_SOM(x,y,raw_data)
net.nodes_graph(colnum=0)
#Print a map of the network nodes and colour them according to the first feature (column number 0) of the dataset
#and then according to the distance between each node and its neighbours.
net.diff_graph()
#Project the datapoints on the new 2D network map.
net.project(raw_data,labels=range(0,16))
#Cluster the datapoints according to the Quality Threshold algorithm.
net.cluster(raw_data,type='qthresh')

