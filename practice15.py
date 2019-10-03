# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 14:00:59 2019

@author: cchang
"""

x = 0
print("Initialization: ", x)
def f1():
    x = 1
    print("In f1 before f2:", x)
    def f2():
        #global x
        #nonlocal x
        x = 2
        print( "In f2:          ", x)
    f2()
    print("In f1 after f2: ", x)
f1()
print("Final:          ", x)

print('--------------------------------------------------------')

'''
nonlocal only breaks ONE level up! e.g. from g3() to g2()
global in only binds it to ouside the oveall function (g1() here)

IF you use nonlocal in BOTH g3() and g2(), then the answer is 0123330, 
since it breaks from g3() to g3(), and then again to g1().

You cannot use nonlocal in g1(). y becomes ambiguous. 

If y global in g1(), only g1() and outside are binded, ie. 0123211
If y global in g2(), only g2() and outside are binded, ie. 0123212
If y global in g3(), only g3() and outside are binded, ie. 0123213

If y global in g1() and g2(), then g1() g2() and outside are binded, ie. 0123222
If y global in g2() and g3(), then g1() g2() and outside are binded, ie. 0123313
If y global in g1() and g3(), then g1() g2() and outside are binded, ie. 0123233

If y global in g1() g2() and g3(), then all are binded, ie. 0123333

If y global in g1(), you cannot use nonlocal in g2(). The y in g1() is ambiguous this way.

If y global in g1() and y nonlocal in g3(), then no conflict with g1()==outside, g2()==g3(). 0123311

Without using any global and nonlocal: 
If you comment out 'y = 3' inside g3(), then g3() sees the y in g2(). 0122210
If you comment out both 'y = 3' inside g3(), and 'y = 2' inside g2(), then g2() and g3() sees the y in g1(). 0111110
If you comment out 'y = 3', 'y = 2' and 'y = 1', g3() sees the y outside . 0000000

This is the same concept as we learned in Function!
The enclosed fxn can definitely "see" the variables in the enclosing fxn. 
But depending on whether the variable is mutable or immutable, handling is different!
If mutable, you can just change its value without problem, e.g. mylist[0] = newItem, 
    and the enclosing fxn can see the new value!!
If immutable, reassignment like 'y = 3' will bind the to a new local name y to 3. 
    But if we replace 'y=3' with 'y=y+1' here, then it will cause error "local 
    variable 'xxx' referenced before assignment". This is because y's assignment 
    in the enclosing fxn is to an integer (immutable!), and 'y=y+1' is causing 
    the local variable/name y to be re-assigned! So this local y is brand new (in the enclosed fxn)!
    Now you cannot do 'y=y+1' on a brand new variable (you don't even have the value to y on the RHS! Can't add 1 to it!)!
    Now if you declare it nonlocal in g3(), then you CAN do 'y=y+1' because now 
    the y in g3() is the same name/address/reference as the y in g2()!! (0123310)

'''
y = 0
print("Initialization:  ", y)
def g1():
    #global y
    y = 1
    print("In g1 before g2: ", y)
    def g2():
        #global y
        #nonlocal y
        y = 2
        print( "In g2 before g3: ", y)
        def g3():
            #global y    
            #nonlocal y 
            y = 3
            #y = y + 1 # MUST have nonlcal in g3()
            print("In g3:           ", y)
        g3()
        print( "In g2 after g3:  ", y)
    g2()
    print("In g1 after g2:  ", y)
g1()
print("Final:           ", y)

print('=============================================')


'''
Here we declare z as a list! Which is mutable and try it again!
z is MUTABLE! Therefore, enclosed fxn can change it and the enclosing fxn can SEE it!
    There is no need to give z a new address/refernce (ie. no need to re-bind) in the
    enclosed fxn like we did for the immutable objects. 

The enclosed fxn can always SEE the variable in the enclosing fxn.
It's just tricky when you try to WRITE to it, esp when it is IMMUTABLE.
'''
z = [0]
print('Z address/reference: {}'.format(id(z)))
print("Initialization:  ", z)
def h1():
    #global y
    z[0] = 1
    print("In h1 before h2: ", z)
    def h2():
        #global y
        #nonlocal y
        z[0] = 2
        print( "In h2 before h3: ", z)
        def h3():
            #global y    
            #nonlocal y 
            #z[0] = 3
            z[0] = z[0] + 1 # This will work since z[] is mutable!
            print("In h3:           ", z)
        h3()
        print( "In h2 after h3:  ", z)
    h2()
    print("In h1 after h2:  ", z)
h1()
print("Final:           ", z)
print('Z address/reference: {}'.format(id(z)))
