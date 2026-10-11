# Take numbers as input from the user one by one. Skip negative numbers and keep adding the positive ones. Stop when the user enters O and print the total. (Uses both continue and break.)
count = 0
while True:
    a = int(input("Enter the number"))
    if a < 0:
        continue
    if a == 0:
        print(count)
        break
    count = count + a
