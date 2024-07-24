'''
    2. Write a Python program to create a deep copy of a given list. Use copy.copy
'''
import copy
list1 = [1,2,3,4,5]
list2 = copy.deepcopy(list1)
print(list2)