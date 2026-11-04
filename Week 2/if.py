# 1. Check whether a number is positive.

n = int(input("Enter number:"))

if n > 0:
    print("Positive")


# 2. Check whether a string is empty.

s = input("Enter string:")

if s == "":
    print("Empty string")


# 3. Check positive, negative or zero using only if.

n = int(input("Enter number:"))

if n > 0:
    print("Positive")

if n < 0:
    print("Negative")

if n == 0:
    print("Zero")


# 4. Check whether a number is a multiple of both 3 and 5.

n = int(input("Enter number:"))

if n % 3 == 0 and n % 5 == 0:
    print("Multiple of 3 and 5")


# 5. Check whether a number is a perfect square.

n = int(input("Enter number:"))

for i in range(n + 1):
    if i * i == n:
        print("Perfect Square")


# 6. Check whether a number is divisible by both 2 and 3.

n = int(input("Enter number:"))

if n % 2 == 0 and n % 3 == 0:
    print("Divisible by both 2 and 3")


# 7. Check whether a number is a perfect cube.

n = int(input("Enter number:"))

for i in range(-abs(n), abs(n) + 1):
    if i * i * i == n:
        print("Perfect Cube")


# 8. Check whether a number is a multiple of 4.

n = int(input("Enter number:"))

if n % 4 == 0:
    print("Multiple of 4")