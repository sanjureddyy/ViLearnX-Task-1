# Student Grade Tracker

# Dictionary to store grades for subjects
student_grades = {}

# Function to input grades
def input_grades():
    num_subjects = int(input("Enter the number of subjects: "))
    for _ in range(num_subjects):
        subject = input("Enter the subject name: ")
        grade = float(input(f"Enter the grade for {subject}: "))
        student_grades[subject] = grade

# Function to calculate average grade
def calculate_average():
    if not student_grades:
        return 0
    return sum(student_grades.values()) / len(student_grades)

# Function to determine letter grade
def calculate_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

# Function to calculate GPA
def calculate_gpa(average):
    return average / 25  # Simplified GPA calculation for demonstration

# Function to display results
def display_results():
    average = calculate_average()
    letter_grade = calculate_letter_grade(average)
    gpa = calculate_gpa(average)
    
    print("\n--- Grade Summary ---")
    for subject, grade in student_grades.items():
        print(f"{subject}: {grade}")
    print(f"Average Grade: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa:.2f}")

# Main function to run the program
def main():
    input_grades()
    display_results()

# Run the program
if __name__ == "__main__":
    main()
