'''23)Program to reverse internal content of each word. Input: Learning Python is Very Easy Output: gninreaL nohtyP si yreV ysaE'''
a = "Learning Python is Very Easy"
b = a.split()
c = b[::-1]
d = " ".join(c)
print(d[::-1])