"""Write a Python function called sum_even_numbers that takes a list of integers as an argument and returns the sum of all the even numbers in the list.
For example, if the input list is [1, 2, 3, 4, 5, 6], the function should return 12, because 2 + 4 + 6 = 12."""


def sum_even_numbers(numbers):

    even = 0
    for i in numbers:
        if i % 2 == 1:
            even = even + i
    return even


print(sum_even_numbers([1, 2, 3, 4, 5, 6]))  # Should print 12
print(sum_even_numbers([2, 4, 6, 8, 10]))  # Should print 30
print(sum_even_numbers([1, 3, 5, 7, 9]))  # Should print 0
