"""
Python program to interchange first and last elements in a list
Given a list, write a Python program to swap first and last element of the list.

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
"""


def swaper(lst):
    
    lst[0], lst[-1] = lst[-1], lst[0]

    return lst


input = [12, 35, 9, 56, 24]
print(swaper(input))

input = [1, 2, 3]
print(swaper(input))