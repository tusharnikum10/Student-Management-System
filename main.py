students = {}

while True:
    choice = input("1.Add 2.View 3.Exit: ")
    if choice == "1":
        name = input("Name: ")
        marks = input("Marks: ")
        students[name] = marks
    elif choice == "2":
        print(students)
    else:
        break
