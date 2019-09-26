# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:08:47 2019

@author: cchang
"""

def my_function():
    """Do nothing, but document it.
    
    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)


'''
Annotations are stored in the __annotations__ attribute of the function as a 
dictionary and have no effect on any other part of the function. 
Parameter annotations are defined by a colon after the parameter name, 
followed by an expression evaluating to the value of the annotation, e.g. str. 
Return annotations are defined by a literal ->, followed by an expression, 
e.g. str, between the parameter list and the colon denoting the end of the def 
statement.
'''
def myf(ham: str, egg: str = 'brown eggs', num: int = 12) -> float:
    print("Annotations: ", myf.__annotations__)
    print("Arguments: ", ham, egg, num)
    return ham + ' and ' + egg

myf('black ham')

'''
Name your classes and functions consistently; 
the convention is to use UpperCamelCase for classes and 
lowercase_with_underscores for functions and methods. 
Always use self as the name for the first method argument 
(see A First Look at Classes for more on classes and methods).
'''