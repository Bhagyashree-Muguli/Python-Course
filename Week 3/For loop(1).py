# Week 3 - For Loop (Questions 1 to 25)


# 1. Print numbers from 1 to 5.
for i in range(1, 6):
    print(i)


# 2. Calculate the sum of numbers from 1 to 10.
s = 0
for i in range(1, 11):
    s += i
print("Sum:", s)


# 3. Print even numbers from 1 to 10.
for i in range(1, 11):
    if i % 2 == 0:
        print(i)


# 4. Calculate the factorial of a number.
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)


# 5. Print elements of a list.
a = [10, 20, 30, 40]
for i in a:
    print(i)


# 6. Find the maximum value in a list.
a = [10, 45, 20, 75, 30]
m = a[0]
for i in a:
    if i > m:
        m = i
print("Maximum:", m)


# 7. Print characters in a string.
s = input("Enter a string: ")
for i in s:
    print(i)


# 8. Count the number of vowels in a string.
s = input("Enter a string: ").lower()
c = 0
for i in s:
    if i in "aeiou":
        c += 1
print("Vowels:", c)


# 9. Print dictionary key-value pairs.
d = {"name": "Ravi", "age": 21, "course": "Python"}
for k, v in d.items():
    print(k, ":", v)


# 10. Print a pattern using nested for loops.
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()


# 11. Find the sum of even numbers from 1 to 100.
s = 0
for i in range(2, 101, 2):
    s += i
print("Sum:", s)


# 12. Print the first 10 Fibonacci numbers.
a, b = 0, 1
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()


# 13. Find common elements between two lists.
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
for i in a:
    if i in b:
        print(i)


# 14. Generate a multiplication table.
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# 15. Calculate factorial using range starting from 1.
n = int(input("Enter a number: "))
f = 1
for i in range(1, n + 1, 1):
    f *= i
print("Factorial:", f)


# 16. Print the reverse of a string.
s = input("Enter a string: ")
rev = ""
for i in s:
    rev = i + rev
print("Reverse:", rev)


# 17. Generate squares from 1 to 10.
a = []
for i in range(1, 11):
    a.append(i * i)
print(a)


# 18. Count the number of words in a sentence.
s = input("Enter a sentence: ")
c = 0
for i in s.split():
    c += 1
print("Words:", c)


# 19. Calculate the sum of digits in a number.
n = input("Enter a number: ")
s = 0
for i in n:
    if i.isdigit():
        s += int(i)
print("Sum of digits:", s)


# 20. Generate prime numbers within a given range.
a = int(input("Enter start: "))
b = int(input("Enter end: "))
for n in range(a, b + 1):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    if c == 2:
        print(n)


# 21. Calculate the power of a number using a for loop.
n = int(input("Enter base: "))
p = int(input("Enter power: "))
r = 1
for i in range(p):
    r *= n
print("Result:", r)


# 22. Reverse a list using a for loop.
a = [1, 2, 3, 4, 5]
rev = []
for i in range(len(a) - 1, -1, -1):
    rev.append(a[i])
print(rev)


# 23. Find the largest element in a list.
a = [12, 45, 7, 89, 23]
m = a[0]
for i in a:
    if i > m:
        m = i
print("Largest:", m)


# 24. Calculate the average of numbers in a list.
a = [10, 20, 30, 40]
s = 0
for i in a:
    s += i
print("Average:", s / len(a))


# 25. Print countdown from a given number.
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i)