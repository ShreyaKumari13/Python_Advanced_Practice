'''
1. Write a Python program to construct a Decimal from a float and a Decimal from a string. 
    Also represent the Decimal value as a tuple. Use decimal.Decimal
'''
import decimal 
a = decimal.Decimal(2.51)
print(a)
print(a.as_tuple())
print()
b = decimal.Decimal('2.51')
print(b)
print(b.as_tuple())

















