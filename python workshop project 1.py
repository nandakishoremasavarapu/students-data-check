students = {}   
sections = set()  


def add_student():
    try:
        roll = int(input("Enter Roll Number: "))
        if roll in students:
            print(" Roll number already exists !!")
            return

        name = input("Enter the Name: ")
        age = int(input("Enter Age: "))

        m1 = int(input("Enter marks of Maths : "))
        m2 = int(input("Enter marks of physics : "))
        m3 = int(input("Enter marks of chemistry : "))

        marks = (m1, m2, m3)   

        section = input("Enter Section: ").upper()
        sections.add(section)  

        students[roll] = {
            "Name": name,
            "Age": age,
            "Marks": marks,
            "Section": section
        }

        print(" Student added successfully !!")

    except ValueError:
        print(" Invalid input! Please enter numbers for Roll, Age, and Marks.")


def display_students():
    if not students:
        print("No students found.")
        return

    for roll, data in students.items():
        print(f"\nRoll No: {roll}")
        print(f"Name: {data['Name']}")
        print(f"Age: {data['Age']}")
        print(f"Marks: {data['Marks']}")
        print(f"Section: {data['Section']}")


def search_student():
    try:
        roll = int(input("Enter Roll Number to search: "))
        if roll in students:
            data = students[roll]
            print("\nStudent Found:")
            print(f"Name: {data['Name']}")
            print(f"Age: {data['Age']}")
            print(f"Marks: {data['Marks']}")
            print(f"Section: {data['Section']}")
        else:
            print(" Student not found.")
    except ValueError:
        print(" Please enter a valid roll number.")


def remove_student():
    try:
        roll = int(input("Enter Roll Number to remove: "))
        if roll in students:
            del students[roll]
            print(" Student removed successfully.")
        else:
            print(" Student not found.")
    except ValueError:
        print(" Please enter a valid roll number.")


def class_topper():
    if not students:
        print("No students available.")
        return

    topper_roll = None
    highest_total = 0

    for roll, data in students.items():
        total = sum(data["Marks"])
        if total > highest_total:
            highest_total = total
            topper_roll = roll

    topper = students[topper_roll]
    print("\n Class Topper:")
    print(f"Roll No: {topper_roll}")
    print(f"Name: {topper['Name']}")
    print(f"Total Marks: {highest_total}")


def show_sections():
    if not sections:
        print("No sections available.")
    else:
        print(" Unique Sections:", sections)


while True:
    print("\n!-------- School Data Management System -------!")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Roll Number")
    print("4. Remove Student by Roll Number")
    print("5. Show Class Topper")
    print("6. Show Unique Sections")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            display_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            remove_student()
        elif choice == 5:
            class_topper()
        elif choice == 6:
            show_sections()
        elif choice == 7:
            print(" Exiting program. Bye!")
            break
        else:
            print("Invalid choice. Please select between 1 to 7.")

    except ValueError:
        print(" Please enter a number between 1 to 7.")