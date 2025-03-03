
import unittest

def subtraction(a =None,b= None):
    if not a or not b:
        return False
    else:
        return a-b
print(subtraction(10,5))
print(subtraction(5,10))
print(subtraction(-8,-7))
print(subtraction(6,-7))
print(subtraction(-13,8))
