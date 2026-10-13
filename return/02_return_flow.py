# is a number prime or not


def prime_check(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count <= 2


print(prime_check(10))
