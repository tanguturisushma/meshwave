students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    student = {
        "Name": name,
        "Roll Number": roll,
        "Marks": marks
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
    else:
        for student in students:
            print(student)

def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

main()
