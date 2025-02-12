'''5)Create a loop that prints the first 10 even numbers.'''
a = int(input("Enter the num : "))
for i in range(a):
    if i % 2 == 0:
        print("Even",i)
    else:
        print("Odd",i)