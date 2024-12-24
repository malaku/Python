#Day 6: Write a program that generates a multiplication table for a user-defined number.
while 1:

    print("Please input your number:")

    a=input()
    a=int(a)
    if a==0:
        break
    if a <0:
        print("Enter a Valid Number")
        continue
    b=[]

    for i in range(1,((a)//2)+1):
        if a%i==0:
            b.append(i)
        else:
            continue

    b.append(a)
    print(b)