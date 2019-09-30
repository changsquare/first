#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:37:27 2019

@author: chang2
"""

'''
1. To use formatted string literals, begin a string with f or F before the 
opening quotation mark
2. The str.format() method of strings requires more manual effort.
'''
year = 2016
event = 'election'
trump = f'Trumps\'s {year} {event}' 
print(trump)

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
trump1 = '{:-10} YES votes  {:2.3%}'.format(yes_votes, percentage)
print(trump1)
trump2 = '{:-9} YES votes  {:2.9%}'.format(yes_votes, percentage)
print(trump2)
trump3 = '{:-2} YES votes  {:2.4%}'.format(yes_votes, percentage)
print(trump3)

'''
The str() function is meant to return representations of values which are 
fairly human-readable, while repr() is meant to generate representations which 
can be read by the interpreter (or will force a SyntaxError if there is no 
equivalent syntax).
'''

'''
Formatted string literals (also called f-strings for short) 
let you include the value of Python expressions inside a string by prefixing 
the string with f or F and writing expressions as {expression}.
'''
import math
print(f'The value of pi is: {math.pi:.4}')
print(f'The value of pi is: {math.pi:.4f}')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 12345678901}
for name, phone in table.items():
    print(f'{name:10} --> {phone:10d}')
    
'''
String.format() method
'''
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print('The story of {1}, {0}, and {other}.'.format('Bill', 'Fredric', other='Georg'))

table = {'Fjord': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}, Fjord: {0[Fjord]:d}, Dcab: {0[Dcab]:d}'.format(table))
'''
The '0' in front of [] means the 'table', i.e. table is the 0-th item in format()
#print('Jack: {[Jack]:d}'.format(table)) will NOT work
Or you can use .format(keyword = input) 
'''
print('Jack: {kiy[Jack]:d}; Fjord: {kiy[Fjord]:d}; Dcab: {kiy[Dcab]:d}'.format(kiy = table))
'''
or you can use **table to decompose a dictionary
'''
print('Jack: {Jack:d}, Fjord: {Fjord:d}, Dcab: {Dcab:9d}'.format(**table))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    
'''
Read and Write files
'r': read
'w': write
'a': append
'r+': read and write
'''
f = open('workfile', 'r')
f.close()

'''
It is good practice to use the with keyword when dealing with file objects. 
The advantage is that the file is properly closed after its suite finishes, 
even if an exception is raised at some point. 
Using with is also much shorter than writing equivalent try-finally blocks

If not, you need to explicitely call f.close()
'''
with open('workfile') as f:
    read_data = f.read()
    print(f'read-data is {read_data}')

# 1) without using with statement 
#file = open('file_path', 'w') 
#file.write('hello world !') 
#file.close()     
# Not good because any error in file.write will cause the file to not close correctly
    
# 2) without using with statement 
file = open('workfile', 'w') 
try: 
    file.write('hello world') 
finally: 
    file.close() 
# Still need to type out file.close
    
    
'''
If the end of the file has been reached, f.read() will return an empty string ('').
'''
with open('workfile','r') as f:
    a1 = f.read()
    a2 = f.read()
print(f'a1 (reads to the end of file) = {a1}, a2 (is empty, i.e. starts at eof) = {a2}')


'''
f.readline() reads a single line from the file; a newline character (\n) is 
left at the end of the string, and is only omitted on the last line of the file
if the file doesn’t end in a newline. This makes the return value unambiguous; 
if f.readline() returns an empty string, the end of the file has been reached, 
while a blank line is represented by '\n', a string containing only a single 
newline.
'''

'''
For reading lines from a file, you can loop over the file object. 
This is memory efficient, fast, and leads to simple code:

for line in f:
...     print(line, end='')


If you want to read all the lines of a file in a list you can also use list(f) 
or f.readlines().
'''

'''
f.write(string) writes the contents of string to the file, returning the number
of characters written.
Other types of objects need to be converted – either to a string (in text mode)
or a bytes object (in binary mode) – before writing them:
'''
value = ('the answer', 24)
s = str(value)
with open('workfile','a') as f:
    aa1 = f.write('\n' + s)
