'''2)Write a program using the for loop to print all the prime numbers less than 100. Rewrite the same program using a while loop.'''
for i in range(2,101):   # The range() function does not include the last number (the ending number). Only numbers from 2 to 100 are counted.
    for j in range(2,101):
        if i%j == 0:
            break
    if i == j:
        print(i,end=",")


for i in range(2, 101):   # Loop through numbers from 2 to 100
    is_prime = True       # Assume `i` is prime
    for j in range(2, int(i ** 0.5) + 1):  # Check divisibility up to sqrt(i)
        if i % j == 0:    # If `i` is divisible by any number, it's not prime
            is_prime = False
            break
    if is_prime:
        print(i, end=",")  # Print prime numbers
