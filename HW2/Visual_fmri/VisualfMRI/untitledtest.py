# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 20:29:14 2016

@author: Nami
"""


import os
import dicom
import numpy as np
import matplotlib.pyplot as plt
im = (dicom.read_file('3-1.ima')).pixel_array
print(im)
plt.imshow(im, cmap=plt.cm.gray)