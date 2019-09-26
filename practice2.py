# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def fib(n):
    """Print Fibonicci until n."""
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a+b
        
def fib2(n):
    """Return a Fabonacci series up to n"""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
 
def fib3(n):
    """Return a Fabonacci series up to n"""
    result = [0, 1]
    while result[-1]< n:
        result.append(result[-1] + result[-2])
    return result



# Function, mutable, immutable
'''
https://learnandlearn.com/python-programming/python-how-to/python-function-arguments-mutable-and-immutable
Immutable variables: the function will make a copy inside the function
Mutable variables: the function just keeps using the same object as the caller
'''
'''
Immutable
'''
def foo1(a):
    print('id of a - preop:', id(a))
    a += 1
    print('id of a - postop:', id(a))
    return a

x = 14
print('id of x - preop: ', id(x))
x = foo1(x)
y = foo1(x)

print('x: ',x, ',' 'y: ',y)

print('id of x - postop: ', id(x))
print('id of y: ', id(y))

'''
Immutable
'''
def foo2(mylist):
    mylist.append(20)
    
def foo3(mylist):
    del mylist[1]
    
def foo4(mylist):
    mylist[0] = 10

list1 = [1, 2]
list2 = list1

print('list1 content - pre: ', list1)
print('list2 content - pre: ', list2)
print('list1 id - pre: ', id(list1))
print('list2 id - pre: ', id(list2))

foo2(list1)
print('list1 content - post: ', list1)
print('list2 content - post: ', list2)
print('list1 id - post: ', id(list1))
print('list1 id - post: ', id(list1))

foo3(list2)
print('list1 content - post: ', list1)
print('list2 content - post: ', list2)
print('list1 id - post: ', id(list1))
print('list1 id - post: ', id(list1))



    