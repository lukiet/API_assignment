# creating a class student with attributes name and grades
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    # adding a grade to a student
    def add_grade(self, subject, grade):
        self.grades[subject] = grade
        print(f"Grade {grade} added for {subject}")

    # getting average grade for a student
    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

# creating a class classroom with an attribute students


class Classroom:
    def __init__(self):
        self.students = []

    # adding a new student to the classroom
    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} has been successfully added to the classroom")

    # displaying all students in the classroom
    def display_students(self):
        if not self.students:
            print("No student is registered")
        else:
            for student in self.students:
                print(f"Name : {student.name}, Grades : {student.grades}")

    # getting student average grade
    def get_student_average_grade(self, student_name):
        for student in self.students:
            if student.name.lower() == student_name.lower():
                return student.get_average_grade()
        return 0

    # getting class average for subject
    def get_class_average(self, subject):
        class_total = 0
        class_count = 0
        for student in self.students:
            if subject in student.grades:
                class_total += student.grades[subject]
                class_count += 1
        if class_count == 0:
            return 0
        return class_total / class_count

# Using an instance of the Classroom class to demonstrate these functionalities.


def main():
    classroom = Classroom()

    while True:
        print("Welcome to SchooliYetu")
        print("1.Add student")
        print("2.Display students")
        print("3.Add grade to student")
        print("4.Get student average grade")
        print("5.Get class average grade")
        print("6.Exit")

        choice = input("Enter your choice : ")

        if choice == '1':
            name = input("Enter student name : ")
            student = student(name, {})
            classroom.add_student(student)
        elif choice == '2':
            classroom.display_students()
        elif choice == '3':
            student_name = input("Enter student name : ")
            subject = input("Enter subject : ")
            grade = int(input("Enter grade : "))
            for student in classroom.students:
                if student.name.lower() == student_name.lower():
                    student.add_grade(subject, grade)
                    break
            else:
                print(f"{student_name} is not available")
        elif choice == '4':
            student_name = input("Enter student name : ")
            average_grade = classroom.get_student_average_grade(
                student_name)
            print(f"{student_name}'s average grade is {average_grade}")
        elif choice == '5':
            subject = input("Enter subject : ")
            average_grade = classroom.get_class_average(subject)
            print(f"Class average for {subject} is {average_grade}")
        elif choice == '6':
            print("Exiting, Thank you for using SchooliYetu")
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
