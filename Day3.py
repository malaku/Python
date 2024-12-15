#Day 3: Build a program that asks for a user's name,
# age, and favorite color, and prints a formatted summary.

print("Please input your name, age, and favorite color: ")

name, age , color= input().split()
age=int(age)
print("Your name is %s, your age is %2d, and you favourite color is %s"%(name, age, color))
