'''1)Write a Python program that accepts your date of birth as a parameter and prints your age.'''

def dob(dt,mon,yr):
    yr25 = 2025 - yr
    print(f'Your Age is {yr25}')
dt = int(input("Enter Date "))
mon = int(input("Enter Month "))
yr = int(input("Enter Year : "))
dob(dt,mon,yr)