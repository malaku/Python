#Day 4: Write a simple program that collects a user's
# personal data, processes it, and outputs a summary with properly formatted strings.

print("Please input your name, age, what university you went to, and what your favourite hobby is: ")

[name, age , university, hobby]= input().split()
age=int(age)
print(f"Your name is {name}, you are {age} years old, you go to {university}, and you love playing {hobby}")
