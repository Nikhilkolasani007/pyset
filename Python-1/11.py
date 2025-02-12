'''11)Write a program that finds the common elements between two lists and stores them in a new list. Input : [1,2,3,4,5] , [1,5,6,7,8] Output : [1,5]'''
a = [1,2,3,4,5]
b = [1,5,6,7,8]
c = [x for x in a if x in b]
print(c)