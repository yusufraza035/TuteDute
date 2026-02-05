def check_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
print("============================================")
print("        GRADE CHECKER PROGRAM               ")
print("============================================")
try:
    score = float(input("Enter your score (0-100): "))
    
    if score < 0 or score > 100:
        print("Error: Please enter a score between 0 and 100")
    else:
        grade = check_grade(score)
        print(f"\nScore: {score}")
        print(f"Grade: {grade}")
        print("============================================")   
except ValueError:
    print("Error: Please enter a valid number")
