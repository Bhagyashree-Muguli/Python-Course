# # 1. Convert Celsius to Fahrenheit or Fahrenheit to Celsius
# ch = input("Enter C for Celsius or F for Fahrenheit:")

# if ch == "C":
#     c = float(input("Enter Celsius:"))
#     f = (c * 9/5) + 32
#     print("Fahrenheit:", f)
# elif ch == "F":
#     f = float(input("Enter Fahrenheit:"))
#     c = (f - 32) * 5/9
#     print("Celsius:", c)
# else:
#     print("Invalid choice")


# # 2. Simple calculator
# a = float(input("Enter a:"))
# b = float(input("Enter b:"))
# op = input("Enter operator (+,-,*,/):")

# if op == "+":
#     print(a + b)
# elif op == "-":
#     print(a - b)
# elif op == "*":
#     print(a * b)
# elif op == "/" and b != 0:
#     print(a / b)
# else:
#     print("Invalid operation")


# # 3. Guess the number game
# import random
# n = random.randint(1, 10)
# g = int(input("Guess a number between 1 and 10:"))

# if g == n:
#     print("Correct guess")
# elif g > n:
#     print("Too high")
# else:
#     print("Too low")

# print("Number was:", n)


# # 4. Check password strength
# p = input("Enter password:")

# if len(p) >= 8 and any(i.isdigit() for i in p) and any(i.isalpha() for i in p):
#     print("Strong password")
# elif len(p) >= 6:
#     print("Medium password")
# else:
#     print("Weak password")


# # 5. Calculate discount based on purchase amount
# amt = float(input("Enter purchase amount:"))

# if amt >= 5000:
#     d = amt * 0.20
# elif amt >= 3000:
#     d = amt * 0.10
# elif amt >= 1000:
#     d = amt * 0.05
# else:
#     d = 0

# print("Final price:", amt - d)


# # 6. Simple ATM machine
# bal = 10000
# print("1. Check Balance")
# print("2. Withdraw Money")
# ch = int(input("Enter choice:"))

# if ch == 1:
#     print("Balance:", bal)
# elif ch == 2:
#     amt = int(input("Enter amount:"))
#     if amt <= bal and amt > 0:
#         bal = bal - amt
#         print("Remaining balance:", bal)
#     else:
#         print("Insufficient balance or invalid amount")
# else:
#     print("Invalid choice")


# # 7. Greet user based on time
# t = int(input("Enter hour (0-23):"))

# if t < 0 or t > 23:
#     print("Invalid time")
# elif t < 12:
#     print("Good Morning")
# elif t < 17:
#     print("Good Afternoon")
# else:
#     print("Good Evening")


# # 8. Calculate price using coupon code
# amt = float(input("Enter amount:"))
# code = input("Enter coupon code:")

# if code == "SAVE20":
#     amt = amt - amt * 0.20
# elif code == "SAVE10":
#     amt = amt - amt * 0.10
# else:
#     print("Invalid coupon")

# print("Final price:", amt)


# # 9. Calculate grade and validate score
# m = int(input("Enter marks:"))

# if m < 0 or m > 100:
#     print("Invalid marks")
# elif m >= 90:
#     print("Grade A")
# elif m >= 80:
#     print("Grade B")
# elif m >= 70:
#     print("Grade C")
# elif m >= 60:
#     print("Grade D")
# else:
#     print("Fail")


# # 10. Calculator using user choice
# a = int(input("Enter a:"))
# b = int(input("Enter b:"))

# print("1.Add  2.Subtract  3.Multiply  4.Divide")
# ch = int(input("Enter choice:"))

# if ch == 1:
#     print(a + b)
# elif ch == 2:
#     print(a - b)
# elif ch == 3:
#     print(a * b)
# elif ch == 4 and b != 0:
#     print(a / b)
# else:
#     print("Invalid choice")


# # 11. Find number of days in a month
# m = int(input("Enter month number:"))

# if m == 2:
#     print("28 or 29 days")
# elif m in [4, 6, 9, 11]:
#     print("30 days")
# elif m in [1, 3, 5, 7, 8, 10, 12]:
#     print("31 days")
# else:
#     print("Invalid month")


# # 12. Calculate BMI and category
# w = float(input("Enter weight in kg:"))
# h = float(input("Enter height in meters:"))

# bmi = w / (h * h)

# print("BMI:", bmi)

# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal weight")
# elif bmi < 30:
#     print("Overweight")
# else:
#     print("Obese")


# # 13. Convert letter grade to GPA
# g = input("Enter grade (A, B, C, D, F):")

# if g == "A":
#     print("GPA: 4.0")
# elif g == "B":
#     print("GPA: 3.0")
# elif g == "C":
#     print("GPA: 2.0")
# elif g == "D":
#     print("GPA: 1.0")
# elif g == "F":
#     print("GPA: 0.0")
# else:
#     print("Invalid grade")