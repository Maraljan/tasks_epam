"""
File `data/students.csv` stores information about students in CSV format.
This file contains the student’s names, age and average mark.

1. Implement a function get_top_performers which receives file path and
returns names of top performer students.
Example:
def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))

Result:
['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia',
'Joseph Head']

2. Implement a function write_students_age_desc which receives the file path
with students info and writes CSV student information to the new file in
descending order of age.
Example:
def write_students_age_desc(file_path, output_file):
    pass

Content of the resulting file:
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
"""
import csv


class Student:
    def __init__(self, name: str, age: int, mark: float):
        self.name = name
        self.age = age
        self.mark = mark

    def __repr__(self):
        return f'({self.name}, {self.age}, {self.mark})'


def get_list_students(file_path: str):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        list_students = []
        for one_student in reader:
            student = Student(
                name=one_student['student name'],
                age=int(one_student['age']),
                mark=float(one_student['average mark']),
            )
            list_students.append(student)
        return list_students


# print(get_list_students('students.csv'))


def get_top_performers(file_path, number_of_top_students=5):
    top_students = get_list_students(file_path)
    sorted_students = sorted(top_students, key=lambda x: x.mark, reverse=True)
    return [student.name for student in sorted_students[:number_of_top_students]]


# print(get_top_performers('students.csv', 5))


def write_students_age_desc(file_path, output_file):
    top_students = get_list_students(file_path)
    sorted_students = sorted(top_students, key=lambda x: x.age, reverse=True)

    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['student name', 'age', 'average mark'])
        writer.writeheader()
        for student in sorted_students:
            writer.writerow({'student name': student.name, 'age': student.age, 'average mark': student.mark})


print(write_students_age_desc('students.csv', 'new_students.csv'))
