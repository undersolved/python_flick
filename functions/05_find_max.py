def find_max(a, b, c):
    if a > b and a > c:
        print(a, "is largest")
    elif b > a and b > c:
        print(b, "is largest")
    else:
        print(c, "is largest")


find_max(10, 20, 30)
