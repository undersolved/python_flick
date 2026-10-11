# Sum of all the numbers from 1 to 100 divisible by 2 and 7

i = 1
total = 0

while i <= 100:
    if i % 2 == 0 and i % 7 == 0:
        print(i, end="-")
        total = total + i
    i += 1

print("\n",total)
