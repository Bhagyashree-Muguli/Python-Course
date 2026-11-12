# # 1. Check whether a year is a leap year
# y = int(input("Enter year:"))

# if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
#     print("Leap year")
# else:
#     print("Not a leap year")


# # 2. Check whether a character is vowel or consonant
# ch = input("Enter character:")

# if ch in "aeiouAEIOU":
#     print("Vowel")
# else:
#     print("Consonant")


# # 3. Check whether a year is a century year
# y = int(input("Enter year:"))

# if y % 100 == 0:
#     print("Century year")
# else:
#     print("Not a century year")


# # 4. Check whether a number is prime
# n = int(input("Enter number:"))
# c = 0

# for i in range(1, n + 1):
#     if n > 1 and n % i == 0:
#         c += 1

# if c == 2:
#     print("Prime")
# else:
#     print("Not prime")


# # 5. Check voting eligibility
# age = int(input("Enter age:"))

# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible")


# # 6. Check positive or non-positive
# n = int(input("Enter number:"))

# if n > 0:
#     print("Positive")
# else:
#     print("Non-positive")


# # 7. Find the larger of two numbers
# a = int(input("Enter a:"))
# b = int(input("Enter b:"))

# if a > b:
#     print(a)
# else:
#     print(b)


# # 8. Check whether a character is a letter
# ch = input("Enter character:")

# if ch.isalpha():
#     print("Letter")
# else:
#     print("Not a letter")


# # 9. Find the smallest of three numbers
# a = int(input("Enter a:"))
# b = int(input("Enter b:"))
# c = int(input("Enter c:"))

# if a <= b and a <= c:
#     print(a)
# elif b <= c:
#     print(b)
# else:
#     print(c)


# # 10. Check whether a string is palindrome
# s = input("Enter string:")

# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# # 11. Find the largest of four numbers
# a = int(input("Enter a:"))
# b = int(input("Enter b:"))
# c = int(input("Enter c:"))
# d = int(input("Enter d:"))

# if a >= b and a >= c and a >= d:
#     print(a)
# elif b >= c and b >= d:
#     print(b)
# elif c >= d:
#     print(c)
# else:
#     print(d)


# # 12. Find the sign of the difference
# a = int(input("Enter a:"))
# b = int(input("Enter b:"))

# d = a - b

# if d > 0:
#     print("Positive")
# elif d < 0:
#     print("Negative")
# else:
#     print("Zero")


# # 13. Check leap year using alternative method
# y = int(input("Enter year:"))

# if y % 4 == 0:
#     if y % 100 == 0:
#         if y % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")


# # 14. Check whether a number is a multiple of 7
# n = int(input("Enter number:"))

# if n % 7 == 0:
#     print("Multiple of 7")
# else:
#     print("Not a multiple of 7")


# # 15. Find the absolute value
# n = int(input("Enter number:"))

# if n < 0:
#     n = -n

# print("Absolute value:", n)