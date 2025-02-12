'''10)Given the following list with values and keys, write a program to convert it into the form of a list of dictionaries with key-value pairs, sort on id, and print. Input_list = ["'morning", 1, "evening", 3, "afternoon", 2] key_list = ["phase", "id"]'''
from collections import Counter
a = ["morning", 1, "evening", 3, "afternoon", 2]
b = ["phase", "id"]
d = []
for i in range(0,len(a),2):
    c = {b[0]:a[i],b[1]:a[i+1]}
    d.append(c)
d.sort(key=lambda x: x["id"])

# Printing result
print(d)
