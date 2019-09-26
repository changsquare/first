#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:34:13 2019

@author: chang2
"""
''' 
When there is only one [], execute in sequence
'''
comb1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

comb2 = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            comb2.append((x, y))
            
'''
When there is nexted [], execute outer [] FIRST
'''
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]

tp1 = [[row[i] for row in matrix] for i in range(4)]
'''
Execute for in in range (4) first, then the nested []
'''
tp2 = []
for i in range(4):
    tp2.append([row[i] for row in matrix])


'''
In the real world...
'''
bbb = list(zip(*matrix))
ccc = set(zip(*matrix))

'''
Tuples
'''
t1 = 12345, 54321, 'hello!'
t2 = (12345, 54321, 'world')

t3 = ([1, 2, 3], [3, 2, 1])
t3[0]
#t3[0] = [9, 8 ,7]