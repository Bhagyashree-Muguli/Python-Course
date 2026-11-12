# # Week 3 - While Loop (Questions 16 to 25)


# # 16. Convert an integer into words.
# ones = ["zero", "one", "two", "three", "four",
#         "five", "six", "seven", "eight", "nine"]

# teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
#          "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

# tens = ["", "", "twenty", "thirty", "forty",
#         "fifty", "sixty", "seventy", "eighty", "ninety"]

# n = int(input("Enter a number (0-999): "))
# words = ""

# if n == 0:
#     words = "zero"
# elif n < 0 or n > 999:
#     words = "Number out of range"
# else:
#     if n >= 100:
#         words += ones[n // 100] + " hundred"
#         n %= 100

#         if n > 0:
#             words += " "

#     if n >= 20:
#         words += tens[n // 10]
#         n %= 10

#         if n > 0:
#             words += "-" + ones[n]

#     elif n >= 10:
#         words += teens[n - 10]

#     elif n > 0:
#         words += ones[n]

# print(words)


# # 17. Reverse a given string using a while loop.
# s = input("Enter a string: ")
# rev = ""
# i = len(s) - 1

# while i >= 0:
#     rev += s[i]
#     i -= 1

# print("Reverse:", rev)


# # 18. Find GCD using Euclidean algorithm.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# a = abs(a)
# b = abs(b)

# while b != 0:
#     a, b = b, a % b

# print("GCD:", a)


# # 19. Convert binary number into decimal.
# b = input("Enter binary number: ")
# decimal = 0
# i = 0
# valid = True

# while i < len(b):
#     if b[i] != "0" and b[i] != "1":
#         valid = False
#         break

#     decimal = decimal * 2 + int(b[i])
#     i += 1

# if valid and len(b) > 0:
#     print("Decimal:", decimal)
# else:
#     print("Invalid binary number")


# # 20. Print all prime numbers between 1 and 100.
# n = 2

# while n <= 100:
#     i = 2
#     prime = True

#     while i < n:
#         if n % i == 0:
#             prime = False
#             break
#         i += 1

#     if prime:
#         print(n)

#     n += 1


# # 21. Calculate power without using ** operator.
# n = int(input("Enter base: "))
# p = int(input("Enter power: "))
# result = 1
# i = 0

# while i < p:
#     result *= n
#     i += 1

# print("Result:", result)


# # 22. Find prime factorization of a number.
# n = int(input("Enter a number greater than 1: "))
# i = 2

# while i <= n:
#     if n % i == 0:
#         print(i, end=" ")
#         n //= i
#     else:
#         i += 1

# print()


# # 23. Search for a word in a text and print its first occurrence.
# text = input("Enter a sentence: ")
# word = input("Enter word to search: ")

# a = text.split()
# i = 0
# found = False

# while i < len(a):
#     if a[i].lower() == word.lower():
#         print("Word found at position:", i)
#         found = True
#         break
#     i += 1

# if not found:
#     print("Word not found")


# # 24. Matrix multiplication using nested while loops.
# a = [[1, 2], [3, 4]]
# b = [[5, 6], [7, 8]]

# r = len(a)
# c = len(b[0])
# n = len(b)

# result = []
# i = 0

# while i < r:
#     row = []
#     j = 0

#     while j < c:
#         s = 0
#         k = 0

#         while k < n:
#             s += a[i][k] * b[k][j]
#             k += 1

#         row.append(s)
#         j += 1

#     result.append(row)
#     i += 1

# print("Result:")
# for row in result:
#     print(row)


# # 25. Find the length of the longest consecutive sequence.
# a = [100, 4, 200, 1, 3, 2]
# longest = 0
# i = 0

# while i < len(a):
#     if a[i] - 1 not in a:
#         count = 1
#         num = a[i]

#         while num + 1 in a:
#             num += 1
#             count += 1

#         if count > longest:
#             longest = count

#     i += 1

# print("Longest sequence length:", longest)