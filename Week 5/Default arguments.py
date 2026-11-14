# # How do you define a function with a default argument in Python?
# def student(name="raju"):
#     print(name)
# student()
 
# # How can you define a function with multiple default arguments in Python?
# def employee(name="abhi",id=101,department="tech",sal=500000):
#      print(name)
#      print(id)
#      print(sal)
#      print(department)
# employee()

# # How do you handle default arguments with lists in Python?
# def ages(a=[12,13,15,16,24,18]):
#     print(a)
# ages()

# How do you use None as a default argument in Python to avoid issues with mutable default arguments?
n = int(input("Enter no:"))

def no(a=None):
    if a is None:
        a = [121, 123, 142, 135, 156]

    a.append(n)
    print(a)

no()

        
 



