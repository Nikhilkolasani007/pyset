'''16) Create a program that checks if two sets have any elements in common'''
a = {1,2,3,4,5,6}
b = {2,3,4,5}
c = [x for x in a if x in b]
print(c)