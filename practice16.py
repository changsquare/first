# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:18:37 2019

@author: cchang
"""

'''
Static (C++) and Class (Python) variables:
Class or static variables are shared by all objects. Instance or non-static 
variables are different for different objects (every object has a copy of it).

Python: Python doesn’t require a static keyword. All variables which are 
        assigned a value in class declaration are class variables. And 
        variables which are assigned values inside class methods are instance 
        variables.
C++: C++ and Java use static keyword to make a variable as class variable. The 
     variables which don’t have preceding static keyword are instance 
     variables.
'''

class Dog:
    
    kind = 'canine'
    #tricks = []             # mistaken use of a class variable

    def __init__(self, name = 'default'):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

a = Dog()
b = Dog('Max')
c = Dog('Archie')
print('a\'s name is: {0}'.format(a.name))
print('b\'s name is: {0}'.format(b.name))
print('a\'s kind is: {0}'.format(a.kind))
print('b\'s kind is: {0}'.format(b.kind))
'''
One can access a class attribute via an instance or via the class name: 
'''
print('Access class attribute by class name: Dog.kind = {}'.format(Dog.kind))


'''
Class variable CAN be changed by one object! And AGAIN, that class variable 
being mutable or immutable will make a big difference!
    IMMUTABLE class variables: when changed/reassigned by an object, python 
    will create a new binding/name. And in fact, this new binding is to a newly
    created instance variable binded to the name that was the Class attribute's 
    name! As a result, one LOST access to this object's class varaible! and
    when using the name that was the class variable's name, it's actually 
    binded to the newly created instance variable!
    The objects's class varaibe is unchanged; it's just that this object/instance
    LOST access to its class attribute (because the name/binding is now re-assigned
    to a instance variable).
    MUTABLE class variables: Mutable calss variables will just get re-binded/
    re-assigned by individual objects! AND all other objects can see it! This 
    is because it's mutable, so no re-assignment when being changed!
    
Class variable/attritribute SHOULD be changed by ClassName.attribute = newValue!!
    This will change it for ALL object instances! Because all objects/instances
    see the same Class attribute (unless of course you force/re-bind the
    instance's original class name to become an instance name, then you lose
    access to that instance/object's class attribute)
'''
a.kind = 'pseudo-cat' # ONLY changes a's kind (class variable) by re-binding a.kind)
print('a\'s kind is: {0}'.format(a.kind)) #a.kind has been re-binded/re-named since kind is immutable
print('b\'s kind is still: {0}'.format(b.kind)) #b.kind is still named/binded to the class's kind!
# Since tricks is a list (mutable) and a class variable, all objects can see and write to the same address/name
a.add_trick('shake hands')
b.add_trick('belly up')
print('a can : {0}'.format(a.tricks[0]))
print('b can : {0}'.format(b.tricks[0])) 
# Since name is a instance variable, each object's name has its own address/name
a.name = 'Spotty'
print('a\'s name is: {0}'.format(a.name))
print('b\'s name is: {0}'.format(b.name))
'''
Class' immutable attributes should NOT have changed even after all 
instances' class attributes are changed. 
'''
print('Before changing b\'s class attribute: Dog.kind = {}'.format(Dog.kind))
b.kind = 'wolf'
print('After changing b\'s class attribute: Dog.kind = {}'.format(Dog.kind))
print('a\'s kind is: {0}'.format(a.kind)) 
print('b\'s kind is now: {0}'.format(b.kind)) #b.kind is now also re-binded!!
print('c\'s kind is still: {0}'.format(c.kind)) #b.kind is now also re-binded!!
#Now we change the Class attribute!!
Dog.kind = 'mutated canine!'
print('Dog Class\'s kind (class atttribute) was changed!! It\'s now: Dog.kind = {}'.format(Dog.kind))
print('a\'s kind is unchanged because it\'s an instance attribute now: {0}'.format(a.kind)) 
print('b\'s kind is unchanged for the same reason: {0}'.format(b.kind)) 
print('c\'s kind is changed because it\'s still a class attribute: {0}'.format(c.kind)) #b.kind is now also re-binded!!
# IF tricks is a class attribute, you can add trick to ALL dogs...
#Dog.tricks.append('stand on two legs')
c.tricks.append('fetch shoes')
print('a\'s tricks: {}'.format(a.tricks))
print('b\'s tricks: {}'.format(b.tricks))
print('c\'s tricks: {}'.format(c.tricks))
