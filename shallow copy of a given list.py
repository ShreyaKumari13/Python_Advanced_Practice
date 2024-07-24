'''
    1. Write a Python program to create a shallow copy of a given list. Use copy.copy
'''
import copy
list1 = [1,2,3,4,5]
list2 = copy.copy(list1)
print(list2)