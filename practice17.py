#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 21:39:24 2019

@author: chang2
"""

'''
Section 9.4:
Methods may reference global names in the same way as ordinary functions. 
The global scope associated with a method is the module containing its 
definition. (A class is never used as a global scope.)
While one rarely encounters a good reason for using global data in a method, 
there are many legitimate uses of the global scope: for one thing, functions 
and modules imported into the global scope can be used by methods, as well as 
functions and classes defined in it. Usually, the class containing the method 
is itself defined in this global scope, 
and in the next section we’ll find some good reasons why a method would want to
reference its own class.

Each value is an object, and therefore has a class (also called its type). 
It is stored as object.__class__.
'''

'''
9.5:
(For C++ programmers: all methods in Python are effectively virtual.)
'''

 