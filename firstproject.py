import csv

student_major_list = "StudentsMajorsList.csv"
student_gpa = "GPAList.csv"
grad_date = "GraduationDatesList.csv"

student_record = []

with open(student_major_list, 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        temp_dictionary = {"id": row[0], "last_name": row[1], "first_name": row[2], "major": row[3]}
        if row[4] != "":
            temp_dictionary["action"] = "YES"
        else:
            temp_dictionary["action"] = "NO"

        student_record.append(temp_dictionary)

with open(student_gpa, 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        student_id = row[0]
        gpa = row[1]

        for student in student_record:
            if student['id'] == student_id:
                student['gpa'] = row[1]

with open(grad_date, 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        for student in student_record:
            if student['id'] == row[0]:
                student['grad_date'] = row[1]


def get_last_name(person):
    return person['last_name']


sorted_student_record_by_last_name = sorted(student_record, key=get_last_name)

# for student in sorted_student_record_by_last_name:
#     print(student)

fieldnames = ['id', 'major', 'first_name', 'last_name', 'gpa', 'grad_date', 'action']
with open('FullRoster.csv', 'w', newline='') as csv_file:
    # Create a DictWriter object
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writerows(sorted_student_record_by_last_name)
    print(sorted_student_record_by_last_name)

# =============================================================================================================
"""
List per major, i.e ComputerInformationSystemsStudents.csv -- there should be a file for
each major and the major needs to be in the file name, the spaces in the major name
should be eliminated for the file name. Each row of the file should contain student ID,
last name, first name, graduation date, and indicate if disciplinary action was taken. The
students should be sorted by their student ID.
"""


# step 1: sorting the student records
def get_id(person):
    return person['id']


sorted_student_record_by_id = sorted(student_record, key=get_id)

# step 2: from the sorted student records, we make another dictionary by the major name
# where {key: major_name, Value: student_record_list}

student_by_major = {}
for student in sorted_student_record_by_id:
    if student['major'] not in student_by_major:
        student_by_major[student['major']] = [student]
    else:
        student_by_major[student['major']].append(student)

# step3: from the new dictionary we need to write student records to different files

# the column names according to questions requirements
column_for_per_major = ['id', 'last_name', 'first_name', 'grad_date', 'action']

# need to iterate through the dictionary of student_by_major
for key, value in student_by_major.items():
    # generates file name
    major_file_name = key.replace(" ", "") + "Students.csv"

    # Since we need do not need all the information from the records, we need to make another
    # student records per major with the required column name

    per_major_student_record = []
    for student in value:
        temp_dictionary = {}
        for column in column_for_per_major:
            temp_dictionary[column] = student[column]
        per_major_student_record.append(temp_dictionary)

    with open(major_file_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=column_for_per_major)
        writer.writerows(per_major_student_record)

# =============================================================================================================
"""
ScholarshipCandidates.csv – should contain a list of all eligible students with GPAs > 3.8.
Students who have graduated or have had disciplinary action taken are not eligible.
Each row should contain: student ID, last name, first name, major, and GPA.
The students must appear in the order of GPA from highest to lowest.
"""


def get_gpa(person):
    return float(person['gpa'])


sorted_student_record_by_gpa = sorted(student_record, key=get_gpa, reverse=True)

scholarship_column = ['id', 'last_name', 'first_name', 'major', 'gpa']
scholarship_student_record = []

for student in sorted_student_record_by_gpa:
    if student['action'] != 'YES' and float(student['gpa']) > 3.8:
        temp_dictionary = {}
        for column in scholarship_column:
            temp_dictionary[column] = student[column]
        scholarship_student_record.append(temp_dictionary)

with open('ScholarshipCandidates.csv', 'w', newline='') as csv_file:
    # Create a DictWriter object
    writer = csv.DictWriter(csv_file, fieldnames=scholarship_column)

    writer.writerows(scholarship_student_record)

# =============================================================================================================
"""
DisciplinedStudents.csv –all students that have been disciplined. Each row should
contain: student ID, last name, first name, and graduation date. The students must
appear in the order of graduation date from oldest to most recent.
"""


def get_grad_date(person):
    return person['grad_date']


sorted_student_record_by_grad_date = sorted(student_record, key=get_grad_date, reverse=False)

disciplined_column = ['id', 'last_name', 'first_name', 'grad_date']
disciplined_student_record = []

for student in sorted_student_record_by_grad_date:
    if student['action'] == 'YES':
        temp_dictionary = {}
        for column in disciplined_column:
            temp_dictionary[column] = student[column]
        disciplined_student_record.append(temp_dictionary)

with open('DisciplinedStudents.csv', 'w', newline='') as csv_file:
    # Create a DictWriter object
    writer = csv.DictWriter(csv_file, fieldnames=disciplined_column)

    writer.writerows(disciplined_student_record)
