#Day 6: Write a program to print numbers from 1 to i, skipping multiples of 3
print("Please input your number:")

a=input()
a=int(a)
for a in range(0,a):
    if a%3 == 0:
        continue
    else:
        print(a)


