print("Welcome to the simple grading system! :>")

# Define the menu
def menu():
    print("[1] Enter student names (minimum 3)")
    print("[2] Enter student grades for 3 subjects")
    print("[3] Calculate student average grades")
    print("[4] Display report for all students")
    print("[5] Exit")

# Initialize variables
students = []
student_scores = []
student_grades = []
average_marks = []

# Display the menu
menu()
option = int(input("Please enter your service option: "))

while option != 5:
    # Option 1: Enter student names
    if option == 1:
        num_students = int(input("Enter the number of students (minimum 3): "))
        while num_students < 3:
            print("You need to enter at least 3 students.")
            num_students = int(input("Enter the number of students (minimum 3): "))

        for i in range(num_students):
            name = input(f"Enter the name of student {i + 1}: ")
            students.append(name)
            student_scores.append([])  # Create a nested list to store scores for each student
            student_grades.append([])  # Create a nested list to store grades for each student

        print(f"{num_students} students added successfully.")

    # Option 2: Enter grades for each student
    elif option == 2:
        if len(students) == 0:
            print("Please enter student names first (Option 1).")
        else:
            for i, student in enumerate(students):
                print(f"Entering scores for {student}:")
                for j in range(3):
                    score = float(input(f"Enter the marks for subject {j + 1} : "))
                    student_scores[i].append(score)
                    # Determine the grade based on the score
                    if score >= 90.0:
                        grade = "A+"
                    elif score >= 80.0:
                        grade = "A"
                    elif score >= 70.0:
                        grade = "A-"
                    elif score >= 60.0:
                        grade = "B"
                    elif score >= 50.0:
                        grade = "C"
                    elif score >= 40.0:
                        grade = "PASS"
                    else:
                        grade = "FAIL"
                    student_grades[i].append(grade)
                print(f"Grades for {student} recorded successfully.")

    # Option 3: Calculate average marks for each student
    elif option == 3:
        if len(student_scores[0]) == 0:
            print("Please enter the grades first (Option 2).")
        else:
            for i in range(len(students)):
                avg = sum(student_scores[i]) / 3
                average_marks.append(avg)
                print(f"{students[i]}'s average marks: {avg:.2f}")

    # Option 4: Display report for all students
    elif option == 4:
        if len(average_marks) == 0:
            print("Please calculate the average marks first (Option 3).")
        else:
            print("Student Report:")
            for i in range(len(students)):
                print(f"\nStudent name: {students[i]}")
                print(f"Subject 1 marks: {student_scores[i][0]:.2f} | Grade: {student_grades[i][0]}")
                print(f"Subject 2 marks: {student_scores[i][1]:.2f} | Grade: {student_grades[i][1]}")
                print(f"Subject 3 marks: {student_scores[i][2]:.2f} | Grade: {student_grades[i][2]}")
                print(f"Average marks: {average_marks[i]:.2f}")

    # Handle invalid options
    else:
        print("INVALID OPTION")

    # Re-display the menu for the next action
    menu()
    option = int(input("Please enter your other service option: "))

print("Thank you for using our service :)")