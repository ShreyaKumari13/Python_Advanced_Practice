'''
    4. Write a Python program to create a deep copy of a given dictionary. Use copy.copy
'''
import copy
sict1 = {1:"shreya",2:"navneet"}
list2 = copy.deepcopy(sict1)
print(list2)