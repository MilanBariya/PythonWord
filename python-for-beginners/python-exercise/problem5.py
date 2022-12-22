"""Write a Python function called count_vowels that takes a string as an argument and returns the number of vowels (a, e, i, o, u) in the string. The function should be case-insensitive, meaning that it should count both upper and lower case vowels.
For example, if the input string is 'Hello World', the function should return 3, because there are three vowels in the string (two e's and one o).
"""

def count_vowels(string):
    vowels = ("a", "e", "i", "o", "u")
    return sum(count_vowels.lower() in vowels for count_vowels in string)
        

print(count_vowels('Hello World')) # Should print 3
print(count_vowels('aeiouAEIOU')) # Should print 10
print(count_vowels('This is a test')) # Should print 4
