'''
    3. Write a Python program to create a shallow copy of a given dictionary. Use copy.copy
'''
import copy
sict1 = {1:"shreya",2:"navneet"}
list2 = copy.copy(sict1)
print(list2)