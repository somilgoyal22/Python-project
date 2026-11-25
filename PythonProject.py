import csv
import matplotlib.pyplot as plt
def load_data():
    students = []
    try:
        with open ("students.csv") as file:
            read = csv.reader(file)
            next(read)
            for row in read:
                roll = row[0]
                name = row[1]
                marks = row[2:]
                
                newMarks = []
                for mark in marks:
                    newMarks.append(float(mark))
                students.append({"roll" : roll, "name" : name, "marks" : newMarks})
    except StopIteration:
         print("CSV file is Empty")
    return students
    
def save_data(students):
    with open("students.csv", "w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["roll", "name", "Maths", "Physics", "Python"])
        for student in students:
            writer.writerow([student["roll"], student["name"]] + student["marks"])
        
def add_students(students):
    roll = input("Enter the roll number: ")
    name = input("Enter the student name: ")
    maths = float(input("Enter maths marks: "))
    physics = float(input("Enter physics marks: "))
    python = float(input("Enter python marks: "))
    new_students = {
        "roll" : roll, "name" : name, "marks" : [maths, physics, python]
    
    }
    students.append(new_students)
    save_data(students)
def search_student(students):
    roll = input("Enter the roll number to search: ")
    for student in students:
        if student["roll"] == roll:
            print(student)
def student_report(students):
    roll = input("Enter the roll number: ")
    for student in students:
        if student["roll"] == roll:
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            total = sum(student["marks"])
            print("Total marks", total)
            average = total/len(student["marks"])
            print("Average: ", average)

def all_students_report(students):
    for student in students:
        print("Roll:", student["roll"])
        print("Name:", student["name"])
        total = sum(student["marks"])
        average = total / len(student["marks"])

        print("Average:", average)
        print("----------------")
def how_many_students(students):
    total_students = len(students)
    print("Total Students:", total_students)
def show_chart(students):
    names= []
    averages = []
    for student in students:
        names.append(student["name"])
        average = sum(student["marks"]) / len(student["marks"])
        averages.append(average)
    plt.bar(names,averages)
    plt.ylabel("Average Marks")
    plt.xlabel("Names")
    plt.title("Student Performance")
    plt.show()


def menu(students):
    while True:
        print("-------- Student Management System -------")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Student Report")
        print("4. Show All Students")
        print("5. Total Students")
        print("6. Show Performance Chart")
        print("7. Exit")
        user = int(input("Enter your choice: "))
        print("You selected:", user)

        if user == 1:
            add_students(students)
        elif user == 2:
            search_student(students)
        elif user == 3:
                student_report(students)
        elif user == 4:
                all_students_report(students)
        elif user == 5:
                how_many_students(students)
        elif user == 6:
                show_chart(students)
        elif user == 7:
             print("Exiting !!!")
             break
        else:
            print("Invalid Choice")

students = load_data()
menu(students)