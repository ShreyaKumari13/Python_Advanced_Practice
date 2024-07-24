'''
    4. Write a Python program to check if a given value is compiled code or not. 
    Also check if a given value is a module or not. Use types.CodeType, types.ModuleType()
'''
import types
import time 
import random
import plyer
print("Check if a given value is compiled code:")
code = compile("print('Hello')", "sample", "exec")
print(isinstance(code, types.CodeType))
print(isinstance("print(abs(-111))", types.CodeType))
print("Check if a given value is a module:")
print(isinstance(types, types.ModuleType))
print(isinstance(time, types.ModuleType))
print(isinstance(random, types.ModuleType))
print(isinstance(plyer, types.ModuleType))

