# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e
# result is "true"

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    '''
    keyword arguments must follow positional arguments.
    keyward args and position args are essentially the same, ie
    they all have a "name/keyword" so that you can call them by 'keyword/name'
    or you can call them by position too if you don't specify their keyword/name when you call
    It's just that when you define the function, you need to put those with default values in the back, 
    and as a result, those without a default value become position arg and must be called in sequence!
    '''
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
'''
#parrot()                     # required argument missing
#parrot(type='bird', 'four')  # non-keyword argument after a keyword argument
#parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
#parrot(110, voltage=220)     # duplicate value for the same argument
#parrot(actor='John Cleese')  # unknown keyword argument
'''

"""
'Default' values are how a function is defined.
'Keyword' arguments are how you call a function.
Two completely different concepts used at different situations. 
Do not mix them up
"""


'''
Use *arg and **arg to store optional variables
*arg must occur before **arg.
cs1(): puts all postional arg in the front, then optional position arg, then optional keyword arg
cs2(): positional arg in the front, optional positional arg, keyword args, optional keyword args
'''

def cs1(kind, number=2, *tuple_name,   **dict_name):
    '''
    2 position args, and the rest (number is a position arg! Although it has a default value! NOT a keyword arg)
    *tuple_name: groups non-keyword args beyond "formal" args (both position and keyword args) into a tuple
    **dict_name: groups all keyword args into a dictionary (with keywords included)
    *tuple_name MUST be BEFORE **dict_name!! to make this work
    '''
    print("-- Do you have any", kind, "?")
    print("-- I have ", number, ' .')
    for arg in tuple_name:
        print(arg)
    print("-" * 40)
    for kw in dict_name:
        print(kw, ":", dict_name[kw])
        
def cs2(kind, *tuple_name, number=2,  **dict_name):
    '''
    1 position arg, other, 
    *tuple_name: groups non-keyword args beyond formal args (both position and keyword args) into a tuple
    **dict_name: groups all keyword args into a dictionary (with keywords included)
    *tuple_name MUST be BEFORE **dict_name!! to make this work
    '''
    print("-- Do you have any", kind, "?")
    print("-- I have ", number, ' .')
    for arg in tuple_name:
        print(arg)
    print("-" * 40)
    for kw in dict_name:
        print(kw, ":", dict_name[kw])

'''
#cs1('blue','one hundred','abc','def', number=3) 
# Fail: multiple definition of number.
cs2('blue','one hundred','abc','def', number=3) 
# Success! number = 3 is a keyward arg
cs2('blue','one hundred','abc','def', hello=3)
# Success! number=2 is the default. hello is put into the optional dictoonary
#cs1,2('blue','one hundred',world='tiny','abc','def', hello=3)
# Fail: positional arg after keyword arg
#cs1('blue','one hundred',world='tiny',number=9, hello=3)
#Fail: multiple values of number
cs2('blue','one hundred',world='tiny',number=9, hello=3)
# Success! number=9
cs1('blue','one hundred',world='tiny', hello=3)
# Success! number='one hundred'
cs2('blue','one hundred',world='tiny', hello=3) 
# Success! number=2 (default)
'''

"""
CONCLUSION:
    cs2() is better!!
    Because as long as you follow the simple rule: position arg BEFORE keyword arg,
    there is no fail.
    In addition, in the last two examples, cs2() is more intuitive, i.e.
    number is not specifically specified/keyword'ed, and cs2() keeps the default value, while cs1() treats number as a position arg and changed its default

Quoting Section 4.7.3:
    "Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments, 
    meaning that they can only be used as keywords rather than positional arguments."
    For example, number in cs2() is a 'keyword-only' arg!
    On the contrary, number in cs1() can be either a position or a keyword arg (e.g. cs1(number=99,kind='red'), cs1('blue',number=5), cs1('blue',66), ...). But cs1('blue','eleven', number=5) will fail!!
"""
def concat(*args, sep="/."):
    return sep.join(args)

def concat2(sep="/.", *args):
    return sep.join(args)

concat('I','really','do','care')
concat2('I','really','do','care') #'I' becomes the separator
