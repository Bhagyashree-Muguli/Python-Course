# # Basic Counting: Write a while loop that counts from 1 to 10 and prints each number.
# n=0
# while n<10:
#     n+=1
#     print(n)

# # Create a program that asks the user to enter a number, and then use a while loop to count
# # down from that number to 1, printing each value.
# n=int(input("Enter a number: "))
# i=n
# while i>=1:
#     print(i)
#     i-=1

# # Write a while loop that calculates the sum of even numbers from 1 to 100.
# n = 100
# i = 1
# sum = 0
#
# while i <= n:
#     if i % 2 == 0:
#         sum += i
#     i += 1
# print(sum)

# # Create a simple number guessing game using a while loop. Generate a random number and have the
# # user guess it, giving hints like "too high" or "too low" until they guess correctly
# import random
# n = random.randint(1, 10)
# guess = 0
#
# while guess != n:
#     guess = int(input("Guess a number between 1 and 10: "))
#
#     if guess > n:
#         print("Too high!")
#     elif guess < n:
#         print("Too low!")
#     else:
#         print("Correct! You guessed it!")

# # Use a while loop to calculate the factorial of a given number.
# n=int(input("Enter a number: "))
# i=1
# fact=1
# while i <= n:
#     fact = fact * i
#     i += 1
#
# print(fact)
#
# # Write a while loop that prints all even numbers between 1 and 50.
# i=1
# while i <= 50:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# # Create a program that calculates the sum of the digits of a given integer using a while loop.
# n=int(input("Enter a number: "))
# sum=0
# while n>0:
#     sum+=n %10
#     n=n//10
# print(sum)

# # Generate a multiplication table for a given number using a while loop.
# n=int(input("Enter a number: "))
# i=1
# while i>0 and i<=10:
#     print(n,"*",i,"=",n*i  )
#     i=i+1

# # Write a program to find all the factors of a given number using a while loop.
# n=int(input("Enter a number:"))
# f=1
# while f<=n:
#     if n%f==0:
#         print(f)
#     f= f+1


# # Implement a program that reverses even numbers using a while loop.
# n=int(input("Enter a number:"))
# rev=0
# while n>0:
#     i= n% 10
#     rev= rev*10+i
#     n = n // 10
# print(rev)
# # Create a program that prompts the user to enter a password. Keep asking until they enter the correct password.
# password=1234
# n=int(input("Enter a Password :"))
#
# while n!=password:
#     print("Wrong Password")
#     n = int(input("Enter a Password Again:"))
#
# else:
#   print("Password is Correct")

# # Write a program using a while loop to generate the first n terms of the Fibonacci sequence.n = 10
# n = 10
# a = 0
# b = 1
# s = 0
# i = 0
# print(a, b, end=" ")
# while i < n - 2:
#     s = a + b
#     print(s, end=" ")
#     a = b
#     b = s
#     i += 1

# # Build a program that checks if a given number is prime using a while loop.
# n = int(input("Enter a number: "))
# i = 2
# while i < n:
#     if n % i == 0:
#         print("Not Prime")
#         break
#     i += 1
# else:
#     print("Prime" if n > 1 else "Not Prime")

# # # Create a program that checks if a given word or phrase is a palindrome (reads the same forwards and backwards)
# # #  using a while loop.
# # s=input()

# # rev=""
# # for i in s:
# #     rev=i+rev
    
# # if s==rev:
# #     print("Palindrome")
# # else:
# #     print("Not")
# s=input()

# rev=""
# i=len(s)-1
# while i>=0:
#     rev+=s[i]
#     i-=1

# if s==rev:
#     print("Palindrome")
# else:
#     print("Not")

# Write a program to generate the first n rows of Pascal's Triangle using while loops.
# Create a program that converts a given integer into words (e.g., 123 -> "one hundred twenty-three") using a while loop.

# # Write a program to reverse a given string using a while loop.
# s=input()
# rev=""
# i=len(s)-1

# while i>=0:
#     rev +=s[i]
#     i-=1
# print(rev)

# # Implement a program to find the greatest common divisor of two numbers using a while loop and the Euclidean algorithm.
# a=int(input("Enter a no:"))
# b=int(input("Enter a no:"))
# while b!=0:
#     r=a%b
#     a=b
#     b=r
# print("gcd",a)


# Create a program that converts a binary number (entered as a string) to its decimal equivalent using a while loop.

# # Write a program that prints all prime numbers between 1 and 100 using a while loop.
# n = 2

# while n <= 100:
#     i = 2
#     count = 0

#     while i < n:
#         if n % i == 0:
#             count += 1
#         i += 1

#     if count == 0:
#         print(n)

#     n += 1
    

# # Implement a program to calculate the result of raising a number to a given power using a while loop, without using the built-in exponentiation operator.
# base=int(input("Enter a no:"))
# pow=int(input("Enter a no:"))
# res=1
# i=1
# while i<=pow:
#     res= res*base
#     i += 1

# print(res)



# # Create a program that calculates and prints the prime factorization of a given number using a while loop.
# n=int(input("enter a no:"))
# i=2
# while n>1:
#     if n% i ==0:
#         print(i)
#         n=n//i
#     else:
#         i=i+1


# # Build a program that searches for a specific word in a text using a while loop and prints the word's first occurrence.
# s=input("Enter text:")
# w=input("Enter word:")
# i=0
# while i <=len(s):
#     if s[i:i+len(w)]==w:
#         print(i)
#         break
#     i+=1

# Implement matrix multiplication (matrix dot product) using nested while loops.



# Given an unsorted array of integers, find the length of the longest consecutive elements sequence using a while loop.
