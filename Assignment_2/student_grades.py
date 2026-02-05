student_grades = {}

def display_menu():
    print("\n================================")
    print("STUDENT GRADES MANAGER")
    print("================================")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")
    print("================================")

def add_student(student_dict):
    name = input("Enter student name: ").strip()
    if name in student_dict:
        print(f"Error: {name} already exists!")
        return
    try:
        grade = float(input(f"Enter {name}'s grade (0-100): "))
        if 0 <= grade <= 100:
            student_dict[name] = grade
            print(f"Successfully added {name} with grade {grade}")
        else:
            print("Error: Grade must be between 0 and 100")
    except ValueError:
        print("Error: Please enter a valid number")

def update_student(student_dict):
    # Update an existing student's grade
    if not student_dict:
        print("No students in the system yet!")
        return
    
    name = input("Enter student name to update: ").strip()
    
    if name not in student_dict:
        print(f"Error: {name} not found in the system!")
        return
    
    try:
        grade = float(input(f"Enter new grade for {name} (0-100): "))
        if 0 <= grade <= 100:
            student_dict[name] = grade
            print(f"Successfully updated {name}'s grade to {grade}")
        else:
            print("Error: Grade must be between 0 and 100")
    except ValueError:
        print("Error: Please enter a valid number")

def print_all_students(student_dict):
    # Print all student grades
    if not student_dict:
        print("No students in the system yet!")
        return
    
    print("\n" + "-" * 50)
    print("STUDENT GRADES LIST")
    print("-" * 50)
    for name, grade in student_dict.items():
        print(f"{name}: {grade}")
    print("-" * 50)


while True:
    display_menu()
    choice = input("Choose an option (1-4): ").strip()
    
    if choice == "1":
        add_student(student_grades)
    elif choice == "2":
        update_student(student_grades)
    elif choice == "3":
        print_all_students(student_grades)
    elif choice == "4":
        print("Thank you for using Student Grades Manager!")
        break
    else:
        print("Invalid choice! Please select 1-4")
