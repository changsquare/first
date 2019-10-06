#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 21:39:24 2019

@author: chang2
"""

'''
Section 9.4:
Methods may reference global names in the same way as ordinary functions. 
The global scope associated with a method is the module containing its 
definition. (A class is never used as a global scope.)
While one rarely encounters a good reason for using global data in a method, 
there are many legitimate uses of the global scope: for one thing, functions 
and modules imported into the global scope can be used by methods, as well as 
functions and classes defined in it. Usually, the class containing the method 
is itself defined in this global scope, 
and in the next section we’ll find some good reasons why a method woulde want to
reference its own class.

Each value is an object, and therefore has a class (also called its type). 
It is stored as object.__class__.
'''

'''
9.5:
(For C++ programmers: all methods in Python are effectively virtual.)
'''

'''
9.6:
“Private” instance variables that cannot be accessed except from inside an 
object don’t exist in Python. However, there is a convention that is followed 
by most Python code: a name prefixed with an underscore (e.g. _spam) should be 
treated as a non-public part of the API (whether it is a function, a method or 
a data member). It should be considered an implementation detail and subject to
change without notice.

name mangling:
Any identifier of the form __spam (at LEAST two leading underscores, at most 
one trailing underscore) is textually replaced with _classname__spam, where 
classname is the current class name with leading underscore(s) stripped. 

The example below would work even if MappingSubclass were to introduce a 
__update identifier since it is replaced with _Mapping__update in the Mapping 
class and _MappingSubclass__update in the MappingSubclass class respectively.
So Mapping's __init__() is using its OWN __update() which is actually _Mapping__update(), and
it is DIFFERENT from MappingSubclass's __update!!
'''
class Mapping:
    def __init__(self, iterable):
        self.item_list = []
        self.__update(iterable)
    def update(self, iterable):
        for item in iterable:
            self.item_list.append(item)
        print(self.item_list)
    __update = update # private copy of the original update()
    
class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.item_list.append(item)
        print(self.item_list)
    __update = update # Useless! Because this this __update is name-mangled to be DIFFERENT from base-class's __update!
            
mylista = ['apple', 'banana', 'pineapple', 'grapes']
mylistb = ['ape', 'dog', 'stingray', 'lobster']
mylistc = {'name', 'age', 'weight', 'height'}

a = Mapping(mylista)
b = MappingSubclass(mylistb)
#b = MappingSubclass(mylista, mylistb) # ERROR: subclass does NOT have __init__()! So subclass must init thru the same __init__() 
c = MappingSubclass(mylistc)

a.update(mylistb)
#b.update(mylistb) # ERROR: b is subclass, whose update() is overridden!
c.update(mylista, mylistb)

'''
9.7
Similar to C's struct, an empty class can serve the same purpose
class member data are created dynamically
'''
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

'''
9.8: Iterator
Behind the scenes, the for statement calls iter() on the container object. 
The function returns an iterator object that defines the method __next__() 
which accesses elements in the container one at a time. When there are no more 
elements, __next__() raises a StopIteration exception which tells the for loop 
to terminate. You can call the __next__() method using the next() built-in 
function.
'''
s = 'wxyz'
it = iter(s) # The iterator objector
print(it.__next__())
print(next(it))
print(it.__next__())
print(next(it))


'''
Having seen the mechanics behind the iterator protocol, it is easy to add 
iterator behavior to your classes:
Define an __iter__() method which returns an object with a __next__() method. 
If the class defines __next__(), then __iter__() can just return self:
'''
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)    
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]
        
zz = Reverse('abcde')
print(next(zz))
print(zz.__next__())
print(next(zz))
#print(zz.__next__())
#print(next(zz))
#print(zz.__next__())
print('---------------------------------------')
for char in zz:
    print(char)
  
        
        
        
        
        
        
        
        
        