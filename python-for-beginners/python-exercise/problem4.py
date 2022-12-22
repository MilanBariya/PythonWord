"""Write a Python function called longest_word that takes a list of words as an argument and returns the longest word in the list. If there is a tie for the longest word, the function should return the first word that ties for longest.
For example, if the input list is ['cat', 'dog', 'elephant', 'mouse'], the function should return 'elephant'.
"""


def longest_word(words):
    return max(words, key=len)


print(longest_word(["cat", "dog", "elephant", "mouse"]))  # Should print 'elephant'
print(longest_word(["a", "ab", "abc", "abcd"]))  # Should print 'abcd'
print(longest_word(["short", "longer", "longest"]))  # Should print 'longest'
