# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 13:28:13 2018

@author: changc1
"""

# Fibonacci number generator
def fib(n):
    a, b = 0, 1
    while b < n:
        print (b, end=',')
        a, b = b, a+b
        
def fib2(n):
    result=[]
    print(id(result))
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
        
