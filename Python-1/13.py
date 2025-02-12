'''13) Write a Python program to count the occurrences of each element in each list. Input [1,3,4,1,1,1,3] Output : Count of 1 is 4 Count of 3 is 2 Count of 4 is 1
'''
from collections import Counter
a = [1,3,4,1,1,1,3]
unique_list = list(set(a))
for i in unique_list:
    print(f'count of {i} is {a.count(i)}')

c = Counter(a)
for j,k in c.items():
    print(f'{j} and {k}')