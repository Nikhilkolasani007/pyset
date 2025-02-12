'''17)Write a Python program that counts the number of occurrences of each character in each string using a Dictionary.'''
from collections import Counter

a = "asglasdg"
c = Counter(a)  # Efficient internal C implementation

print(dict(c))
