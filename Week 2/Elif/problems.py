# Write a Python program that converts a temperature in Celsius to Fahrenheit or vice versa based on user input.
# t=float(input("Enter the temperature:"))
# choice=input("C for Celsius or F for Fahrenheit: ")
# if choice=="C":
#     t=t*9/5 + 32
#     print(t)
# elif choice == "F":
#     t= (t-32) * 5/9
#     print(t)
# else:
#     print("Invaid choice")


# Write a simple calculator program that performs basic arithmetic operations 
# (addition, subtraction, multiplication, division) based on user input.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


# Write a Python program for a simple "Guess the Number" game. Generate a random number, and let the user guess it.
import random

n = random.randint(1, 10)

while True:
    guess = int(input("Guess the number: "))

    if guess == n:
        print("Correct!")
        break
    elif guess < n:
        print("Too low")
    else:
        print("Too high")

# Write a Python program that checks the strength of a user's password based on certain criteria.
p = input("Enter password: ")

if len(p) < 8:
    print("Weak")
elif p.isalnum():
    print("Add special character")
else:
    print("Strong")

# Write a Python program that calculates the final price of an item after applying a discount based on the purchase amount.
amt = int(input("Enter amount: "))

if amt >= 5000:
    amt = amt * 0.8
elif amt >= 2000:
    amt = amt * 0.9

print("Final price:", amt)

# Write a Python program that simulates an ATM machine, allowing users to check their balance and withdraw money.
balance = 10000
amt = int(input("Enter withdrawal amount: "))

if amt <= balance and amt > 0:
    balance = balance - amt
    print("Balance:", balance)
else:
    print("Invalid amount")

# Write a Python program that greets the user differently based on the time of day.
h = int(input("Enter hour: "))

if h < 12:
    print("Good morning")
elif h < 17:
    print("Good afternoon")
elif h < 21:
    print("Good evening")
else:
    print("Good night")
# Write a Python program that calculates the final price of an item after applying a discount coupon code.
price = int(input("Enter price: "))
c = input("Enter coupon: ")

if c == "SAVE10":
    price = price * 0.9
elif c == "SAVE20":
    price = price * 0.8

print("Final price:", price)

# Write a Python program that calculates and prints the grade based on a given score, but also validates the input score.
s = int(input("Enter score: "))

if s < 0 or s > 100:
    print("Invalid score")
elif s >= 90:
    print("A")
elif s >= 80:
    print("B")
elif s >= 70:
    print("C")
elif s >= 60:
    print("D")
else:
    print("F")

# Write a Python program that acts as a simple calculator and allows the user to choose
#  the operation (addition, subtraction, multiplication, division).
a = int(input("Enter a: "))
b = int(input("Enter b: "))
ch = int(input("1.Add 2.Sub 3.Mul 4.Div: "))

if ch == 1:
    print(a + b)
elif ch == 2:
    print(a - b)
elif ch == 3:
    print(a * b)
elif ch == 4 and b != 0:
    print(a / b)
else:
    print("Invalid choice")

# Write a Python program that determines the number of days in a given month.
m = int(input("Enter month: "))

if m == 2:
    print(28)
elif m in [4, 6, 9, 11]:
    print(30)
elif 1 <= m <= 12:
    print(31)
else:
    print("Invalid month")

# Write a Python program that calculates a person's Body Mass Index (BMI) and categorizes
#  it into different categories (underweight, normal weight, overweight, obese).
w = float(input("Enter weight: "))
h = float(input("Enter height: "))
bmi = w / (h * h)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

# Write a Python program that converts letter grades (A, B, C, D, F) to their equivalent GPA values.
g = input("Enter grade: ").upper()

if g == "A":
    print(4)
elif g == "B":
    print(3)
elif g == "C":
    print(2)
elif g == "D":
    print(1)
elif g == "F":
    print(0)
else:
    print("Invalid grade")

