# # 1. Print numbers from 1 to 5 using a for loop


# n = 5
# for i in range(1, n+1):
#     print(i)


# # 2. Calculate the sum of numbers from 1 to 10 using a for loop


# n = 10
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print(sum)


# # 3. Print even numbers from 1 to 10 using a for loop


# n = 10
# for i in range(1, n+1):
#     if i % 2 == 0:
#         print(i)


# # 4. Calculate the factorial of a number using a for loop


# n = 8
# f = 1
# for i in range(1, n+1):
#     f = f * i
# print(f)


# # 5. Print elements of a list using a for loop


# n = [1, 3, 5, 7, 9]
# for i in n:
#     print(i)


# # 6. Find the maximum value in two lists using a for loop


# a = [10, 20, 30, 40, 50]
# b = [5, 25, 15, 30]

# n = a[0]
# for i in a:
#     if i > n:
#         n = i
# print(n)

# m = b[0]
# for i in b:
#     if i > m:
#         m = i
# print(m)


# # 7. Print characters in a string using a for loop


# s = "python"
# for i in range(len(s)):
#     print(s[i])


# # 8. Count the number of vowels in a string using a for loop


# s = "rohan"
# c = 0
# for i in range(len(s)):
#     if s[i] in "aeiou":
#         c += 1
# print(c)


# # 9. Iterate over a dictionary and print key-value pairs using a for loop


# d = {"name": "Jani", "age": 25}
# for k, v in d.items():
#     print(k, ":", v)


# # 10. Print a pattern using nested for loops


# for i in range(1, 6):
#     for j in range(i):
#         print("B", end=" ")
#     print()


# # 11. Calculate the sum of all even numbers from 1 to 100 using a for loop


# n = 100
# s = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         s += i
# print(s)


# # 12. Print the first 10 Fibonacci numbers using a for loop


# n = 10
# a = 0
# b = 1
# s = 0

# print(a, b, end=" ")

# for i in range(n-2):
#     s = a + b
#     print(s, end=" ")
#     a = b
#     b = s


# # 13. Find and print the common elements between two lists using a for loop


# a = [12, 24, 36, 48, 65]
# b = [12, 34, 23, 65, 48]

# for i in a:
#     for j in b:
#         if i == j:
#             print(i)


# # 14. Generate a multiplication table for a given number using a for loop


# n = int(input("Enter the no: "))
# for i in range(1, 21):
#     print(n, "*", i, "=", n*i)


# # 15. Calculate the factorial of a number using a for loop with a range starting from 1


# n = int(input("Enter the no: "))
# f = 1

# for i in range(1, n+1):
#     f = f * i

# print(f)

# # 16. Print the reverse of a string using a for loop ?
# n="bhagya"
# rev=""
# for i in n:
#      rev = i + rev
# print(rev)

# # 17. Generate a list of squares for numbers from 1 to 10 using a for loop ?
# s=[]
# sqr =0
# for i in range(1,11):
#     sqr = i*i
#     s.append(sqr)
# print(s)



# # 18. Count the number of words in a sentence using a for loop ?
# s="Python is easy"
# c=1
# for i in range(len(s)):
#      if s[i] == " ":
#           c += 1
# print(c)


# # 19. Calculate the sum of digits in a number using a for loop ?
# n=int(input("Enter a number: "))
# s=0
# for i in range(len(str(n))):
#      s += n % 10
#      n = n//10
#
# print(s)

# # 20. Generate a list of prime numbers within a given range using a for loop ?
# n=[]
# for i in range(1,11):
#      c=0
#      for j in range(1,i+1):
#           if i%j == 0:
#                c+= 1
#      if c == 2:
#           n= n+[i]
# print(n)

# # 21. Calculate the power of a number using a for loop ?
# n=int(input("Enter a number: "))
# p=3
# r=1
# for i in range(p):
#      r=r*n
# # print(r)
# # 22. Reverse a list using a for loop ?
# l = input("Enter numbers: ").split()
# r = []
#
# for i in l:
#     r = [i] + r
#
# print(r)


# # 23. Find and print the largest element in a list using a for loop ?
# s=[12,24,32,10,28]
# l=s[0]
# for i in s:
#     if i > l:
#         l=i
# print (l)


# 24. Calculate the average of numbers in a list using a for loop ?


# 25. Print a countdown from a given number using a for loop ?
# 26. Generate a pattern of numbers using nested for loops ?
# 27. Calculate the product of elements in a list using a for loop ?
# 28. Find and print the position (index) of an element in a list using a for loop ?
# 29. Calculate the sum of all odd numbers from 1 to 100 using a for loop ?
# 30. Print a triangle of asterisks using a for loop ?
# 31. Calculate the LCM (Least Common Multiple) of two numbers using a for loop ?
# 32. Count the number of prime numbers in a range using a for loop ?
# 33. Reverse words in a sentence using a for loop ?
# 34. Print a diamond pattern using nested for loops ?
# 35. Print a hollow square pattern using nested for loops ?
# 36. Calculate the factorial of a number using a for loop with a specified step ?
# 37. Print a right-angled triangle pattern using a for loop ?
# 38. Generate a list of multiples of a number within a given range using a for loop ?