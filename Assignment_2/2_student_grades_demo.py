print("=" * 60)
print("STUDENT GRADES MANAGER - DEMONSTRATION")
print("=" * 60)

# Create a dictionary to store student grades
student_grades = {}

print("\n--- STEP 1: Adding Students ---")
print("Adding Alice with grade 95...")
student_grades["Alice"] = 95
print("Adding Bob with grade 87...")
student_grades["Bob"] = 87
print("Adding Charlie with grade 76...")
student_grades["Charlie"] = 76
print("Adding Diana with grade 82...")
student_grades["Diana"] = 82

print("\n--- STEP 2: Printing All Student Grades ---")
print("-" * 60)
print("STUDENT GRADES LIST")
print("-" * 60)
for name, grade in student_grades.items():
    print(f"{name}: {grade}")
print("-" * 60)

print("\n--- STEP 3: Updating Diana's Grade ---")
print(f"Diana's current grade: {student_grades['Diana']}")
student_grades["Diana"] = 89
print(f"Diana's updated grade: {student_grades['Diana']}")

print("\n--- STEP 4: Adding New Student ---")
print("Adding Edward with grade 91...")
student_grades["Edward"] = 91

print("\n--- STEP 5: Final Student Grades List ---")
print("-" * 60)
print("FINAL STUDENT GRADES LIST")
print("-" * 60)
for name, grade in student_grades.items():
    print(f"{name}: {grade}")
print("-" * 60)

print("\n--- STEP 6: Checking if Student Exists ---")
if "Alice" in student_grades:
    print(f"Alice found in records with grade: {student_grades['Alice']}")
if "Frank" not in student_grades:
    print("Frank not found in records")

print("\n--- STEP 7: Getting Total and Average Grade ---")
total = sum(student_grades.values())
average = total / len(student_grades)
print(f"Total students: {len(student_grades)}")
print(f"Total grades: {total}")
print(f"Average grade: {average:.2f}")

print("\n" + "=" * 60)
print("DEMONSTRATION COMPLETE!")
print("=" * 60)
