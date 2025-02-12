'''25) Write a program to find the number of occurrences of each character present in the given String. Input: ABCABCABBCDE Output: A-3,B-4,C-3,D-1,E-1'''
from collections import Counter
a = "ABCABCABBCDE"
b = {}
for char in sorted(set(a)):
    b = {char : a.count(char)}
    for k,v in b.items():
        print(f'{k} - {v}')
