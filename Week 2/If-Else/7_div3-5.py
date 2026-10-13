x=int(input("Enter a number: "))
if x%5==0 and x%3==0:
    print(x,"is divisible by both 3 and 5")
elif x%5==0:
    print(x,"is divisible by 5")        
elif x%3==0:
    print(x,"is divisible by 3")
else:
    print(x,"is not divisible by 3 or 5")   

