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
    file.write('hello world\n')
    file.write('star war!\n')
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
'''
with open('workfile','r') as f:
    for line in f:
        print(line, end='')

'''
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


'''
f.tell() returns an integer giving the file object’s current position in the 
file represented as number of bytes from the beginning of the file when in 
binary mode and an opaque number when in text mode.

To change the file object’s position, use f.seek(offset, whence). The position 
is computed from adding offset to a reference point; the reference point is 
selected by the whence argument. A whence value of 0 measures from the 
beginning of the file, 1 uses the current file position, and 2 uses the end of 
the file as the reference point. whence can be omitted and defaults to 0, 
using the beginning of the file as the reference point.

f.read(size). size is # of characters in string and bytes for binary files. If
ignored, it reads to the EOF. 
'''
with open('workfile2', 'br+') as f2:
    f2.write(b'0123456789abcdef')
    print('At the end, since we just finished writing: {0}'.format(f2.tell()))
    print('Go to the 0-th/beginning location: {0}'.format(f2.seek(0))) # Return to the beginning. 
    print('Go to the 4-th location from beginning: {0}'.format(f2.seek(4,0))) 
    print('Confirm it is at 4: {0}'.format(f2.tell()))
    print('Read 2 items: {0}'.format(f2.read(2)))
    print('Now we are at 6-th location: {0}'.format(f2.tell()))
    print('Advance 2 locations from current locateion to 8: {0}'.format(f2.seek(2,1)))
    print('Conform we are at 8: {0}'.format(f2.tell()))
    print('Advance 3 locations from current locateion to b: {0}'.format(f2.seek(3,1)))
    print('Conform we are at 11: {0}'.format(f2.tell()))
    print('Confirm again by reading the 11-th item: {}'.format(f2.read(1)))
    print('Goto -3-th location from the end: {0}'.format(f2.seek(-3,2)))
    print('Conform by reading it: {}'.format(f2.read(1)))
    
'''
JSON: to convert between string and numbers

serilaizing: take Python data hierarchies, and convert them to string representations;
deserializing: Reconstructing the data from the string representation

import json
converted_string = json.dumps([list_of_Python_data])

# Converts data into a text file
json.dump([list_of_python_data], file_name)

# To decode the object again,
list_of_python_data = json.load(file_object)
'''
import json
x3 = [12,34,'yacht']
with open('workfile3','r+') as f3:
    #json.dump(x3, f3)
    xx3 = json.load(f3)



