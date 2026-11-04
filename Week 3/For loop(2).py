# Week 3 - For Loop (Questions 26 to 38)


# 26. Generate a pattern of numbers using nested for loops.
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# 27. Calculate the product of elements in a list.
a = [2, 3, 4, 5]
p = 1
for i in a:
    p *= i
print("Product:", p)


# 28. Find the position (index) of an element in a list.
a = [10, 20, 30, 40]
n = int(input("Enter element: "))
for i in range(len(a)):
    if a[i] == n:
        print("Index:", i)
        break
else:
    print("Element not found")


# 29. Calculate the sum of odd numbers from 1 to 100.
s = 0
for i in range(1, 101, 2):
    s += i
print("Sum:", s)


# 30. Print a triangle of asterisks.
for i in range(1, 6):
    print("*" * i)


# 31. Calculate the LCM of two numbers using a for loop.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == 0 or b == 0:
    print("LCM: 0")
else:
    for i in range(max(abs(a), abs(b)), abs(a * b) + 1):
        if i % abs(a) == 0 and i % abs(b) == 0:
            print("LCM:", i)
            break


# 32. Count the number of prime numbers in a range.
a = int(input("Enter start: "))
b = int(input("Enter end: "))
c = 0

for n in range(a, b + 1):
    if n > 1:
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        if prime:
            c += 1

print("Prime count:", c)


# 33. Reverse words in a sentence using a for loop.
s = input("Enter a sentence: ")
a = s.split()
rev = []

for i in range(len(a) - 1, -1, -1):
    rev.append(a[i])

print(" ".join(rev))


# 34. Print a diamond pattern using nested for loops.
n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()


# 35. Print a hollow square pattern using nested for loops.
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 36. Calculate factorial using a for loop with a specified step.
n = int(input("Enter a number: "))
f = 1

for i in range(1, n + 1, 1):
    f *= i

print("Factorial:", f)


# 37. Print a right-angled triangle pattern.
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# 38. Generate multiples of a number within a given range.
n = int(input("Enter a number: "))
a = int(input("Enter start: "))
b = int(input("Enter end: "))

if n != 0:
    for i in range(a, b + 1):
        if i % n == 0:
            print(i)
else:
    print("Enter a non-zero number")