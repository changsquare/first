#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 17:12:45 2019

@author: chang2
"""

'''
lambda expression
They are syntactically restricted to a single expression. 
Semantically, they are just syntactic sugar for a normal function definition. 
Like nested function definitions, lambda functions can reference variables from the containing scope.
'''
# Example 1
def make_increment(n):
    '''
    This function (make_increment) actually returns a function (lambda fx)!!
    '''
    return lambda x: x + n

f = make_increment(2)
'''
f is the lambda fxn returned by make_increment(2)
'''
print(f(8))

# Example 2
def make_sum():
    return lambda x, y: x + y

g = make_sum()

print(g(33, 4))


'''
Example 2
'''
def takeSecond(elem):
    return elem[1]
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort(key = takeSecond) #sort by the second element
print(random)

random = [(2, 2), (3, 4), (4, 1), (1, 3)]
print(random)
random.sort(key = lambda elmnt: elmnt[1]) #sort by the second element
print(random)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key = lambda item: item[1])
print(pairs)

wordlist = ['world', 'hi', 'dog', 'cat', 'california', 'texas', 'tejas']
wordlist.sort(key = len)
print(wordlist)