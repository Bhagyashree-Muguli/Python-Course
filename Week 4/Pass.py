# # Week 3 - Pass Statement


# # 1. Print even numbers and use pass for odd numbers.
# a = [1, 2, 3, 4, 5, 6]

# for i in a:
#     if i % 2 != 0:
#         pass
#     else:
#         print(i)


# # 2. Print prime numbers from a list.
# a = [2, 3, 4, 5, 6, 7, 8, 9]

# for n in a:
#     prime = True

#     if n <= 1:
#         prime = False

#     for i in range(2, n):
#         if n % i == 0:
#             prime = False
#             break

#     if prime:
#         print(n)
#     else:
#         pass


# # 3. Create a Shape class using pass.
# class Shape:
#     pass


# s = Shape()
# print("Shape class created")


# # 4. Count lines containing the word apple.
# f = open("sample.txt", "r")
# c = 0

# for line in f:
#     if "apple" in line.lower():
#         c += 1
#     else:
#         pass

# f.close()
# print("Lines containing apple:", c)


# # 5. Check whether a number is a perfect square.
# n = int(input("Enter a number: "))
# i = 1
# found = False

# while i * i <= n:
#     if i * i == n:
#         found = True
#         break
#     i += 1

# if found:
#     print("Perfect square")
# else:
#     pass


# # 6. Check completed tasks.
# tasks = ["Completed", "Pending", "Completed", "Pending"]

# for i in tasks:
#     if i == "Completed":
#         print("Task completed")
#     else:
#         pass


# # 7. Create an Employee class using pass.
# class Employee:
#     pass


# e = Employee()
# print("Employee class created")


# # 8. Print sentences ending with a question mark.
# a = ["How are you?", "Hello", "What is Python?", "Good morning"]

# for i in a:
#     if i.endswith("?"):
#         print(i)
#     else:
#         pass