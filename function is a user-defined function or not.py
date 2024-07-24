'''
    1. Write a Python program to check if a function is a user-defined function or not. Use types.FunctionType, types.LambdaType()
'''
import types
def sum1(a,b):
    c = a + b
    return c
# a = int(input("Enter the number1: "))
# b = int(input("Enter the number2: "))
# print(sum1(a,b))
print(isinstance(sum1,types.FunctionType))
print(isinstance(sum1,types.LambdaType))
print(isinstance(sum,types.FunctionType))
print(isinstance(sum,types.LambdaType))