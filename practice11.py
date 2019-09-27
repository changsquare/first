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

'''
dict.items()
'''
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

'''
enumerate()
'''
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

'''
zip(), and str.format()
'''
ques = ['name', 'age', 'hobby']
ans = ['john', '32', 'jogging']
for q, a in zip(ques, ans):
    print('What''s you {0}? It is {1}'.format(q, a))

'''
reversed()
'''
for i in reversed(range(1, 10, 2)):
    print(i)
    
    
'''
sorted() : returns a new sorted list while leaving the source unaltered.
'''
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(basket):
    print(f)
print('----------')
for f in set(sorted(basket)):
    print(f)
print('----------')
for f in sorted(set(basket)):
    print(f)

'''
It is sometimes tempting to change a list while you are looping over it; 
however, it is often simpler and safer to create a new list instead.
'''
import math
raw_data = [56.3, float('nan'), 34.5, 43.66, 76.9, float('NaN'), 34.3]
filtered_data = []
for v in raw_data:
    if not math.isnan(v):
        filtered_data.append(v)
print(filtered_data)


'''
The Boolean operators and and or are so-called short-circuit operators: 
their arguments are evaluated from left to right, and evaluation stops as soon 
as the outcome is determined. For example, if A and C are true but B is false, 
A and B and C does not evaluate the expression C. When used as a general value 
and not as a Boolean, the return value of a short-circuit operator is the last 
evaluated argument.
'''
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null_return = string1 or string2 or string3
print(non_null_return)
