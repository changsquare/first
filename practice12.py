#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 18:32:21 2019

@author: chang2
"""

'''
Python has a way to put definitions in a file and use them in a script or in 
an interactive instance of the interpreter. Such a file is called a module;

A module is a file containing Python definitions and statements. 
The file name is the module name with the suffix .py appended. 
Within a module, the module’s name (as a string) is available as the value of 
the global variable __name__.

A module can contain executable statements as well as function definitions. 
These statements are intended to initialize the module. 
They are executed only the first time the module name is encountered in an 
import statement. 1 (They are also run if the file is executed as a script.)

Each module has its own private symbol table, which is used as the global 
symbol table by all functions defined in the module. Thus, the author of a 
module can use global variables in the module without worrying about 
accidental clashes with a user’s global variables. 
On the other hand, if you know what you are doing you can touch a module’s 
global variables with the same notation used to refer to its functions, 
modname.itemname.

Modules can import other modules. 
The imported module names are placed in the importing module’s global symbol 
table.
In the example beleo, all the "names" in fibo, i.e. aa, bb, fib1, and fib2 are 
available in the importing env
'''
import fibo

fibo.fib1(9)
fibo.aa
#fibo.a


'''
Executing modules as scripts:

    python fibo.py <arguments>

the code in the module will be executed, just as if you imported it, but with 
the __name__ set to "__main__". 
That means that by adding this code at the end of your module:
    if __name__ == "__main__":
        import sys
        fib(int(sys.argv[1]))
you can make the file usable as a script as well as an importable module.
'''

'''
The built-in function dir() is used to find out which names a module defines.
'''


