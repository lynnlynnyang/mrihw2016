# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:08:37 2016

@author: Lynn
"""
import os
import dicom
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
im = np.zeros((100,256,256))
for i in range(100):
    im[i] = (dicom.read_file("3-%d.ima" %(i + 1))).pixel_array
"""
im = np.zeros((20, 256, 256))
for i in range(20):
    im2 = im2 + im[i]
"""
a=(sum(im[0:20],0)/20 + sum(im[40:60],0)/20+sum(im[80:100],0)/20)/3
b=(sum(im[20:40],0)/20+sum(im[60:80],0)/20)/2
c=b-a
#print(np.amax(c[1,0]) )
#print(c[2,2])
#print(b-a)

fig, ax = plt.subplots()
plt.imshow(b-a, cmap=plt.cm.gray),plt.clim(-100,100)
cax = ax.imshow(b-a, interpolation='nearest', cmap=cm.gist_rainbow)
cbar = fig.colorbar(cax,orientation='horizontal')
#print(np.min(c))
curve=im[:,120,27]
#print(curve[:])
plt.figure()
plt.plot(curve)

EV=np.concatenate([np.zeros(20)+510,np.ones(20)*530,np.zeros(20)+510,np.ones(20)*530,np.zeros(20)+510])
#print(EV)
plt.plot(EV)
#result=np.ndarray((256,256),dtype=object);
result=np.zeros((256,256));
for ii in range(256):
    for jj in range(256):
        coeftemp=np.corrcoef(EV,im[:,ii,jj])
        result[ii,jj]=coeftemp[0,1]




cor_index = []
cor_sum = 0

for ii in range(256):
    for jj in range(256):
        if(result[ii,jj] >= 0.30):
            cor_index.append(ii)
            cor_index.append(jj)
            cor_sum += result[ii,jj]
            #print(result[ii,jj])
            
cor_avg = cor_sum /(len(cor_index)/2)



for i in range(0,int(len(cor_index)/2),2):
    #print(i)
    result[cor_index[i],cor_index[i+1]] = cor_avg


for ii in range(256):
    for jj in range(256):
        if(result[ii,jj] < 0.30):
          result[ii,jj] = 0 
            





plt.figure()

fig, ax = plt.subplots()
plt.imshow(result, cmap=cm.gist_rainbow)
cax = ax.imshow(result, interpolation='nearest', cmap=cm.gist_rainbow)
cbar = fig.colorbar(cax,orientation='horizontal')
