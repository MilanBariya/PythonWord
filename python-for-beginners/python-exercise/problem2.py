"""
Python program to swap two elements in a list
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2] 
"""

def swaper(lst, pos1, pos2):
    
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    
    return lst

input = [23, 65, 19, 90]
pos1 = 1
pos2 = 3
print(swaper(input, pos1-1, pos2-1))

input = [1, 2, 3, 4, 5]
pos1 = 2
pos2 = 5
print(swaper(input, pos1-1, pos2-1))