# # Week 3 - While Loop (Questions 1 to 15)


# # 1. Count from 1 to 10.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# # 2. Count down from a given number to 1.
# n = int(input("Enter a number: "))
# while n >= 1:
#     print(n)
#     n -= 1


# # 3. Find the sum of even numbers from 1 to 100.
# i = 1
# s = 0
# while i <= 100:
#     if i % 2 == 0:
#         s += i
#     i += 1
# print("Sum:", s)


# # 4. Number guessing game using while loop.
# import random

# n = random.randint(1, 100)
# guess = 0

# while guess != n:
#     guess = int(input("Guess the number: "))
#     if guess > n:
#         print("Too high")
#     elif guess < n:
#         print("Too low")
#     else:
#         print("Correct!")


# # 5. Calculate factorial of a number.
# n = int(input("Enter a number: "))
# fact = 1
# i = 1

# while i <= n:
#     fact *= i
#     i += 1

# print("Factorial:", fact)


# # 6. Print even numbers between 1 and 50.
# i = 1
# while i <= 50:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# # 7. Find the sum of digits of a number.
# n = abs(int(input("Enter a number: ")))
# s = 0

# while n > 0:
#     s += n % 10
#     n //= 10

# print("Sum of digits:", s)


# # 8. Print multiplication table of a number.
# n = int(input("Enter a number: "))
# i = 1

# while i <= 10:
#     print(n, "x", i, "=", n * i)
#     i += 1


# # 9. Find all factors of a number.
# n = int(input("Enter a number: "))
# i = 1

# while i <= n:
#     if n % i == 0:
#         print(i)
#     i += 1


# # 10. Reverse an even number.
# n = int(input("Enter an even number: "))

# if n % 2 == 0:
#     rev = 0
#     temp = abs(n)

#     while temp > 0:
#         rev = rev * 10 + temp % 10
#         temp //= 10

#     if n < 0:
#         rev = -rev

#     print("Reverse:", rev)
# else:
#     print("Enter an even number")


# # 11. Keep asking for password until it is correct.
# password = "python123"
# p = ""

# while p != password:
#     p = input("Enter password: ")

# print("Access granted")


# # 12. Generate first n Fibonacci terms.
# n = int(input("Enter number of terms: "))
# a = 0
# b = 1
# i = 0

# while i < n:
#     print(a, end=" ")
#     a, b = b, a + b
#     i += 1

# print()


# # 13. Check whether a number is prime.
# n = int(input("Enter a number: "))
# i = 2
# prime = True

# if n <= 1:
#     prime = False

# while i < n:
#     if n % i == 0:
#         prime = False
#         break
#     i += 1

# if prime:
#     print("Prime number")
# else:
#     print("Not a prime number")


# # 14. Check whether a word or phrase is a palindrome.
# s = input("Enter a word or phrase: ").lower()
# s = s.replace(" ", "")

# i = 0
# j = len(s) - 1
# palindrome = True

# while i < j:
#     if s[i] != s[j]:
#         palindrome = False
#         break
#     i += 1
#     j -= 1

# if palindrome:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# # 15. Generate Pascal's Triangle using while loops.
# n = int(input("Enter number of rows: "))
# i = 0

# while i < n:
#     value = 1
#     j = 0

#     while j <= i:
#         print(value, end=" ")
#         value = value * (i - j) // (j + 1)
#         j += 1

#     print()
#     i += 1