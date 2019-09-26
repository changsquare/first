#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:24:23 2019

@author: chang2
"""

# FOR
words = ['cat','dog','window','california']
for w in words:
    print(w)
    w = w + '1'
    print(w)
'''
Use words[:] to create a copy for w
'''
i=0
for w in words:
    i = i+1
    if len(w) > 7:
        words.insert(0,w)
        print(words, i)
        if i > 7:
            break     
'''
It's better to separate words from w, i.e.
w is the counter, and words shoudl stay the same
***IF you want to change words in the loop
USE words[:] to make a copy for the counter w!!!***
It seems that the counter will get updated each time the words are updated.
So without [:], the code above becomes an infinite loop
because words become a new thing every time california is added and the for-loop re-starts (See range()) 
'''

#RANGE
'''
range() does NOT generate a list! It's an iterable, i.e. 
it generates a counter each time it is called by FOR or LIST (iterator).
'''
for i in range(5,12,3):
    print(i)

list(range(5,12,4))

# Break, Continue, and ELSE in a loop [for-loop and while-loop]
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print (n, 'is', x, 'times', n//x)
            break
    else:
        print(n, 'is prime.')
'''
break breaks the for loop.
else is executed the loop terminates regularly, i.e. NOT by break
''' 
'''
continue just continues to the next iteration
'''
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print (n, 'is', x, 'times', n//x)
            continue
    else:
        print(n, 'is prime.')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        