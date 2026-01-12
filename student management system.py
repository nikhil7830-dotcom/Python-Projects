students = {}

def add_student():
    student_id = input("Enter ID: ")
    name = input("Enter Name: ")
    students[student_id] = {"name": name, "grades": []}
    print(f"Student {name} added.")

def view_students():
    print("Student List:")
    for sid, info in students.items():
        print(f"ID: {sid}, Name: {info['name']}")

while True:
    choice = input("1-Add 2-View 3-Exit: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
