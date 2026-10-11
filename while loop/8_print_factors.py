"""
Ask a number from the user and print all the factors and count
"""

number = int(input("Enter the number"))
i = 1
lsit_1 = [] 

while i <= number:
    if number % i == 0:
        lsit_1.insert(0, i)
    i += 1

print(len(lsit_1), "\n", lsit_1)
