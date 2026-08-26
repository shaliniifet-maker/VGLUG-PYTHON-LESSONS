a, b, c = map(int, input().split())
if a > b and a > c:
    print(a, "is the largest number")
elif b > a and b > c:
    print(b, "is the largest number")
elif c > a and c > b:
    print(c, "is the largest number")
elif a == b and a > c:
    print(a, "and", b, "are the largest numbers")
elif a == c and a > b:
    print(a, "and", c, "are the largest numbers")
elif b == c and b > a:
    print(b, "and", c, "are the largest numbers")
elif a == b == c:
    print("All three numbers are equal")
