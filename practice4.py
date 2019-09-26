#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:04:37 2019

@author: chang2
"""

i = 5
print('i id init: ', id(i))

def f(arg=i):
    print('i val in fxn: ', i, 'i id in fxn: ', id(i))
    '''
    Even INSIDE the function, i's address is still accessible!!
    And it's the updated one!ithin the function
    But arg is only w
    '''
    print('arg val in fxn pre: ', arg, 'arg id in fxn preop: ', id(arg))
    arg = j + 1
    print('arg val in fxn post: ', arg, 'arg id in fxn postop: ', id(arg))
    
    
    
print('i id 1: ', id(i))
i = 6
print('i id 2: ', id(i))

f()
print('i id 3: ', id(i))


f(7)