#Day 16: Mini-Project: Create a program that manages a to-do list using file handling.
file = open("ToDoList.txt", "w")

b=int(input("How many items on the todo list?"))

for i in range(b):
    val=input(f"Item {i+1}: ")
    file.write(f"{val} \n")
file.close()