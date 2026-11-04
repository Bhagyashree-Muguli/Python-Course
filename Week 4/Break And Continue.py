# # Week 3 - Break and Continue Statements


# # 1. Find the first prime number greater than 100.
# n = 101

# while True:
#     prime = True
#     i = 2

#     while i < n:
#         if n % i == 0:
#             prime = False
#             break
#         i += 1

#     if prime:
#         print(n)
#         break

#     n += 1


# # 2. Sum numbers from 1 to 100, skipping multiples of 3 and 5.
# s = 0

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         continue
#     s += i

# print("Sum:", s)


# # 3. Find all factors of a given number using break.
# n = int(input("Enter a number: "))
# i = 1

# while True:
#     if n % i == 0:
#         print(i)

#     if i == n:
#         break

#     i += 1


# # 4. Calculate average, ignoring negative numbers.
# a = [10, -5, 20, 30, -2]
# s = 0
# c = 0

# for i in a:
#     if i < 0:
#         continue
#     s += i
#     c += 1

# if c > 0:
#     print("Average:", s / c)
# else:
#     print("No positive numbers")


# # 5. Basic login system with three attempts.
# username = "admin"
# password = "python123"

# for i in range(3):
#     u = input("Enter username: ")
#     p = input("Enter password: ")

#     if u == username and p == password:
#         print("Login successful")
#         break
#     else:
#         print("Incorrect details")

# else:
#     print("Maximum attempts reached")


# # 6. Find the first 10 even numbers, skipping multiples of 3.
# n = 2
# c = 0

# while c < 10:
#     if n % 3 == 0:
#         n += 2
#         continue

#     print(n)
#     c += 1
#     n += 2


# # 7. Calculate factorial using break.
# n = int(input("Enter a number: "))
# fact = 1
# i = 1

# while True:
#     if i > n:
#         break
#     fact *= i
#     i += 1

# print("Factorial:", fact)


# # 8. Print first 20 Fibonacci terms, stopping above 100.
# a = 0
# b = 1
# c = 0

# while c < 20:
#     if a > 100:
#         break

#     print(a, end=" ")
#     a, b = b, a + b
#     c += 1

# print()


# # 9. Calculate average until a negative number is entered.
# s = 0
# c = 0

# while True:
#     n = int(input("Enter number: "))

#     if n < 0:
#         break

#     s += n
#     c += 1

# if c > 0:
#     print("Average:", s / c)
# else:
#     print("No numbers entered")


# # 10. Count vowels using continue.
# s = input("Enter a string: ")
# c = 0

# for i in s:
#     if i not in "aeiouAEIOU":
#         continue
#     c += 1

# print("Vowels:", c)


# # 11. Print prime numbers between 1 and 100.
# for n in range(2, 101):
#     prime = True

#     for i in range(2, n):
#         if n % i == 0:
#             prime = False
#             break

#     if prime:
#         print(n, end=" ")

# print()


# # 12. Menu-driven application.
# while True:
#     print("1. Add")
#     print("2. View")
#     print("3. Exit")

#     ch = input("Enter choice: ")

#     if ch == "1":
#         a = int(input("Enter first number: "))
#         b = int(input("Enter second number: "))
#         print("Sum:", a + b)

#     elif ch == "2":
#         print("Welcome!")

#     elif ch == "3":
#         print("Exit")
#         break

#     else:
#         print("Invalid choice")


# # 13. Ask for a password until it has at least 8 characters.
# while True:
#     p = input("Enter password: ")

#     if len(p) < 8:
#         print("Password must have 8 characters")
#         continue

#     print("Valid password")
#     break


# # 14. Sum even numbers from 1 to 100, skipping multiples of 7.
# s = 0

# for i in range(1, 101):
#     if i % 2 == 0 and i % 7 == 0:
#         continue

#     if i % 2 == 0:
#         s += i

# print("Sum:", s)