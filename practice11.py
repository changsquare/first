# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:06:38 2019

@author: cchang
"""
'''
Curly braces or the set() function can be used to create sets. 
Note: to create an empty set you have to use set(), not {}; 
the latter creates an empty dictionary, a data structure that we discuss in 
the next section.
'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print('apple' in basket)

'''
Syntax : set(iterable)
Parameters : Any iterable sequence like list, tuple or dictionary.
Returns : An empty set if no element is passed. Sorted, non-repeating element iterable modified as passed as argument.
'''

a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)
print(a & b)

aa = set([12, 34])
aa = set(range(12,34))
print(aa)

'''
Dictionaries are indexed by keys, which can be any immutable type;
strings and numbers can always be keys.
Tuples can be used as keys if they contain only strings, numbers, or tuples; 
if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. 
You can’t use lists as keys.
It is best to think of a dictionary as a set of key: value pairs, 
with the requirement that the keys are unique (within one dictionary). 
A pair of braces creates an empty dictionary: {}.  
Performing list(d) on a dictionary returns a list of all the keys used in the 
dictionary, in insertion order 
(if you want it sorted, just use sorted(d) instead). 
To check whether a single key is in the dictionary, use the in keyword.
'''
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel['jack']
del tel['sape']
list(tel)
sorted(tel)
'guido' in tel

{x: x**2 for x in (2, 4, 6)}
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
#When the key is simple strin, you can use simple keyword construct
dict(sape=4139, guido=4127, jack=4098)

Activity

    Chang Chang deleted version 1

Chang Chang deleted version 2
Chang Chang uploaded versions 3 - 13
Comment(optional)
Write a comment

@mention users to notify them.
Drop files on this page to upload them into this folder.
0 items
Size: 1.8 KB

