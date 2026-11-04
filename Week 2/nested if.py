# # 1. Check whether x is greater than y and also greater than 15.

# x = 10
# y = 5

# if x > y:
#     if x > 15:
#         print("Greater than 15")
#     else:
#         print("Not greater than 15")
# else:
#     print("x is not greater than y")


# # 2. Check grade and print failed message if marks are below 70.

# m = int(input("Enter marks:"))

# if m >= 70:
#     if m >= 90:
#         print("A Grade")
#     else:
#         print("B Grade")
# else:
#     print("You failed")


# # 3. Check credit card eligibility using age and income.

# age = int(input("Enter age:"))
# inc = int(input("Enter income:"))

# if age >= 18:
#     if inc >= 30000:
#         print("Eligible for credit card")
#     else:
#         print("Income is too low")
# else:
#     print("You are underage")


# # 4. Check whether a number is even and greater than 10.

# n = int(input("Enter number:"))

# if n % 2 == 0:
#     if n > 10:
#         print("Even and greater than 10")
#     else:
#         print("Even but not greater than 10")
# else:
#     print("Odd")


# # 5. Calculate theme park ticket price.

# age = int(input("Enter age:"))
# h = float(input("Enter height in feet:"))

# if age < 12:
#     if h < 4:
#         print("Ticket price: 10")
#     else:
#         print("Ticket price: 15")
# else:
#     if h < 4:
#         print("Ticket price: 15")
#     else:
#         print("Ticket price: 20")


# # 6. User authentication.

# u = input("Enter username:")
# p = input("Enter password:")

# if u == "admin":
#     if p == "1234":
#         print("Access granted")
#     else:
#         print("Incorrect password")
# else:
#     print("Invalid username")


# # 7. Food ordering program.

# food = input("Choose Burger or Pizza:")

# if food == "Burger":
#     f = input("Do you want fries? yes/no:")
#     if f == "yes":
#         print("Burger with fries")
#     else:
#         print("Burger")
# elif food == "Pizza":
#     c = input("Do you want extra cheese? yes/no:")
#     if c == "yes":
#         print("Pizza with extra cheese")
#     else:
#         print("Pizza")
# else:
#     print("Invalid choice")


# # 8. Check positive, negative or zero and even or odd.

# n = int(input("Enter number:"))

# if n > 0:
#     if n % 2 == 0:
#         print("Positive Even")
#     else:
#         print("Positive Odd")
# elif n < 0:
#     print("Negative")
# else:
#     print("Zero")


# # 9. Check driving eligibility using age and license.

# age = int(input("Enter age:"))
# lic = input("Do you have a license? yes/no:")

# if age >= 18:
#     if lic == "yes":
#         print("Eligible to drive")
#     else:
#         print("Not eligible to drive")
# else:
#     print("Not eligible to drive")


# # 10. Check voting eligibility using age and citizenship.

# age = int(input("Enter age:"))
# c = input("Are you a citizen? yes/no:")

# if age >= 18:
#     if c == "yes":
#         print("Eligible to vote")
#     else:
#         print("Not eligible to vote")
# else:
#     print("Not eligible to vote")