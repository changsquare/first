#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:53:16 2019

@author: chang2
"""

'''
PACKAGE: a collection of modules. See example below

sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py

The __init__.py files are required to make Python treat directories containing
the file as packages. 
In the simplest case, __init__.py can just be an empty file, but it can also 
execute initialization code for the package or set the __all__ variable, 
described later.

Note that when using 
from package import item, 
the item can be either a submodule (or subpackage) of the package, or some 
other name defined in the package, like a function, class or variable. 

Contrarily, when using syntax like 
import item.subitem.subsubitem, 
each item except for the last must be a package; 
the last item can be a module or a package but can’t be a class or function or 
variable defined in the previous item.
'''
import fibo #works fine
#import fibo.fib1 #fails! 
from fibo import fib1 #works fine

'''
if a package’s __init__.py code defines a list named __all__, it is taken to be
the list of module names that should be imported when 
from package import * is encountered. 

If __all__ is not defined, the statement from sound.effects import * does not 
import all submodules from the package sound.effects into the current 
namespace; it only ensures that the package sound.effects has been imported 
(possibly running any initialization code in __init__.py).
This includes any names defined (and submodules explicitly loaded) by 
__init__.py.

Remember, from package import specific_submodule, is the recommended notation 
unless the importing module needs to use submodules with the same name from 
different packages.
'''

'''
You can also write relative imports, with the from module import name form of 
import statement. 
These imports use leading dots to indicate the current and parent packages 
involved in the relative import. From the surround module for example, 
you might use:
    
from . import echo
from .. import formats
from ..filters import equalizer
'''    
