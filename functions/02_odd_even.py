"""
Write a function that ask a number from user and prints if that number is odd or even.
"""


def odd_even():
    num = int(input("Enter your number"))

    if num % 2 == 0:
        print(f"The number {num} is EVEN")
    else:
        print(f"The number {num} is ODD")


odd_even()
