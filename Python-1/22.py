'''22) Program to reverse order of words. Input: Learning Python is Very Easy Output: Easy Very is Python Learning'''

a = "Learning Python is Very Easy"
b = a.split()
c = b[::-1]
d = " ".join(c)
print(d)