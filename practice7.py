#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 17:03:37 2019

@author: chang2
"""

'''
Section 4.7.4
*arg unpacks a list or a tuple to be positional arguments to a function
**arg unpacks a dictionary to be keyworded arguments to a function
'''

a1 = list(range(3,6))
print(a1)
arg = [3, 6]
a2 = list(range(*arg))
print(a2)

a3 = list(range(3, 16, 2))
print(a3)
arg = [3, 16, 2]
a4 = list(range(*arg))
print(a4)

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"state": "bleedin' demised", "action": "VOOM", "voltage": "six million", }

parrot(**d)