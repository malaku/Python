#Day 4: Create a program that checks whether a number is positive, negative, or zero
print("Please input your number:")

a=input()
a=int(a)
if a>0:
    print(f"{a} is positive")
elif a==0:
    print(f"{a} is zero")
else:
    print(f"{a} is negative")



