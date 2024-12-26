def count_students():
    print("Welcome to the Student Count Program!")
    student_list = []

    while True:
        student_name = input("Enter the name of the student (or type 'done' to finish): ")
        
        if student_name.lower() == 'done':
            break
        elif student_name.strip() == "":
            print("Please enter a valid name.")
        else:
            student_list.append(student_name)

    # Count the number of students
    total_students = len(student_list)
    
    print(f"\nTotal number of students in class: {total_students}")
    print("List of students:")
    for student in student_list:
        print(student)

# Start the program
count_students()
s