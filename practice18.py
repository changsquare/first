# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:21:22 2019

@author: cchang
"""

import numpy as np


'''
https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html
  1. If the number of objects in the selection tuple is less than N , then : is 
     assumed for any subsequent dimensions.
  2. Basic slicing with more than one non-: entry in the slicing tuple, acts 
     like repeated application of slicing using a single non-: entry, where the 
     non-: entries are successively taken (with all other non-: entries 
     replaced by :). Thus, x[ind1,...,ind2,:] acts like x[ind1][...,ind2,:] 
     under basic slicing. [Warning The above is not true for advanced indexing]
'''

x = np.array([[[1],[2],[3]], [[4],[5],[6]]])
print(x.shape)
'''
The outermost bracket is the first dimension (which has 2)
The middle bracket is the second dimention (which has 3)
The innermost bracket is the last dimension (which has 1)
'''
x[0,2]
x[0][2]
x[0]
x[1][1]
x[0][0][0]
x[...,0] #The first two dimension are all included, and take the first of the last dimension
x[0,...] #Take the first element of the first dimension, and all of the last two dimension  
x[0,...,0] #Take the first element of the first dimension, all elements of the second dimension, and the 1st element of the last dimension
x[0,...,0][1]