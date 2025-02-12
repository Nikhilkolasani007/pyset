'''12)Write a program that checks if a given list is sorted in ascending order or not. Input : [-10,2,5,6,8,90] Output : 'Yes List is Sorted in Ascending Order'''
a = [-10,2,5,6,8,90]
if a == sorted(a):
    print('Yes List is Sorted in Ascending Order')
elif a == sorted(a,reverse=True):
    print("DESC")
else:
    print("not sorted")