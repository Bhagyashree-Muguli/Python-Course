# # addition of 2 nos:
# add =lambda a,b:a+b
# r=add(10,20)
# print(r)

# # Can you provide a lambda function to square a number in Python?
# sqr=lambda a:a*a
# r=sqr(4)
# print(r)

# # How can you create a lambda function to add two numbers in Python? Can you give an example?
# add =lambda a,b:a+b
# r=add(10,20)
# print(r)

# # How would you write a lambda function to find the maximum of two numbers in Python? Can you give an example?
# max=lambda a,b: a if a>b else b
# r=max(10,20)
# print(r) 

# # How can you create a lambda function to check if a number is even in Python? Can you provide an example?
# check=lambda a:  "even" if a%2==0 else "not even"
# print(check(9))
# print(check(4))
# # Can you demonstrate a lambda function to extract the last character from a string in Python?
# extract = lambda a: a[-1]
# print(extract("bhagi"))

# # How would you write a lambda function to sort a list of tuples based on the second element in Python?
# # Can you provide an example?
# list=[("a",8),("b",9),("c",6)]
# list.sort(key=lambda x:x[1])
# print(list)

# # How can you create a lambda function to filter even numbers from a list in Python?
# #  Can you give an example?
# n=int(input("Enter the nos:"))
# lst=[]
# c=0
# for i in range(n):
#     a=int(input("enter numbers:"))
#     lst.append(a)
# even=list(filter(lambda x: x%2==0,lst))
# even.sort()
# print(even)

# # Can you provide a lambda function with a conditional expression to categorize ages in Python?
# n=int(input("enter no:"))
# res="Postive"if n>0 else"Negative"
# print(res)

# # How can you write a lambda function to calculate the factorial of a number using recursion in Python? 
# # Can you demonstrate this with an example?
# n = int(input("Enter the no:"))
# res = lambda x: 1 if x == 0 else x * res(x-1)
# print(res(n))




# Can you demonstrate a lambda function to extract the last character from a string in Python?
# extract = lambda a: a[-1]

# print(extract("bhagi"))
