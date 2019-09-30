#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 18:32:21 2019

@author: chang2
"""

'''
Executing modules as scripts:
the code in the module will be executed, just as if you imported it, but with 
the __name__ set to "__main__". That means that by adding this code at the end
of your module:
'''

aa = [1, 2, 9]
bb = [33, 45, 23]

def fib1(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print('__name__ inside the Fibo module is: {0}'.format(__name__))
    

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result



if __name__ == "__main__":
    import sys
    fib1(int(sys.argv[1]))
    print('Name is {0}.'.format(__name__))

