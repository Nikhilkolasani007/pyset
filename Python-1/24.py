'''Write a program that generate the output in a way that if there is a digit after a character it will convert the digit into number of character of precedence character Input: a4b3c2 Output: aaaabbbcc'''

a = 'a4b3c2'
c = ""
for i in range(0,len(a),2):
    char = a[i]
    num = int(a[i+1])
    c += char * num
print(c)