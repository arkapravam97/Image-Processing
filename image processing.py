# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:44:34 2022

@author: Arkaprava Mondal
"""

from  matplotlib import pyplot as plt
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.io import imread
import glob
from math import sqrt

extent = 0,5,0,5
example_file = glob.glob(r"vo21.jpeg")[0]
im = imread(example_file,as_gray=True)
#plt.imshow(im,cmap=plt.get_cmap('gray'),extent=extent)
plt.savefig("Gray_2.png",dpi=3000)
plt.show()
blobs_log=blob_log(im,max_sigma=10,num_sigma=10, threshold=0.001)
blobs_log[:,2]=blobs_log[:,2]*sqrt(2)
numrows = len(blobs_log)
print("Number of particles counted : " ,numrows)
fig, ax = plt.subplots(1, 1)
plt.imshow(im, cmap=plt.get_cmap('gray'))
for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r+2, color='lime', linewidth=1, fill=False)
    ax.add_patch(c)
Area=25
Density= numrows/Area
print("The density of particles in the image is " + str(Density) + " particles per micro metres squared")
#plt.savefig("Identified_2.png",dpi=3000)