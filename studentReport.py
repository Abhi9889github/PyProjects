from datetime import datetime
import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="98898765@123sql",
    database="studentsrecords"
)
cursor = connection.cursor()

connection.commit()

# CREATING TABLE STUDENT REPORT_CARD

# cursor.execute('''CREATE TABLE students_reportcard(
#     student_id INT AUTO_INCREMENT PRIMARY KEY,
#     first_name VARCHAR(50),
#     last_name VARCHAR(50),
#     date_of_birth DATE,
#     gender VARCHAR(10),
#     course VARCHAR(100),
#     enrollment INT,
#     grade VARCHAR(2),
#     contact_number VARCHAR(15),
#     email VARCHAR(100));''')

# Creating table students_details

# cursor.execute('''CREATE TABLE students_details(std_id INT AUTO_INCREMENT PRIMARY KEY,student_name VARCHAR(500),student_age INT, student_enroll INT,student_course VARCHAR(200))''')

# creating table student_marks

# cursor.execute(
    # '''CREATE TABLE student_marks (student_enroll INT(200),subject_1 INT(200),subject_2 INT(200),subject_3 INT(200),total_marks INT(100),grades VARCHAR(100))''')
# creating table subjects information

# cursor.execute('''CREATE TABLE subjects_information(subject_id INT AUTO_INCREMENT PRIMARY KEY,subject_name VARCHAR(200),credits INT)''')
# cursor.execute('''11
# ''')
class Student_information():

    def students_section(self):

        print(
            "Select any operation:\n1:Add Students\n2:Update Student Information\n3:Delete student record\n4:Show all student's record.")
        x = int(input("Enter the number:"))
        # Add students
        if x == 1: 
     
           student_name = input("Enter the name of the student:")
           student_age = int(input("Enter the age of the student:"))
           student_enroll = int(input("Enter the enroll number:"))
           student_course = input("Enter the course of the student:")
        
           cursor.execute('''
                            INSERT INTO students_details (student_name, student_age, student_enroll, student_course)
                                VALUES (%s, %s, %s, %s)
                                  ''', (student_name, student_age, student_enroll, student_course))
            
           connection.commit()
           print("Student data inserted successfully.")
            
        elif x == 2:
            print("Select what do you want to update:\n1:Name\n2:Age\n3:Course\n")
            y = int(input("Enter the number:"))
            if y == 1:
                student_id = int(input("Enter the id of the student:"))
                name = input("Enter the new name of the student:")
                cursor.execute('''UPDATE students_details SET student_name=%s WHERE std_id=%s''',
                               (name, student_id))
                print("Name Successfully updated.")

            elif y == 2:
                student_id = int(input("Enter the id of the student:"))
                age = int(input("Enter the new age:"))
                cursor.execute('''UPDATE students_details SET student_age=%s WHERE student_id=%s''',
                               (age, student_id))
                print("Age Successfully updated.")

            elif y == 3:
                student_id = int(input("Enter the id of the student:"))
                course = input("Enter the new course:")
                cursor.execute('''UPDATE students_details SET student_course=%s WHERE student_enroll=%s''',
                               (course, student_id))
                print("Course Successfully updated.")
        elif x == 3:
            s_id = int(input("Enter the id of the student you want to delete the record:"))
            cursor.execute('''DELETE FROM students_details WHERE std_id=%s''', (s_id,))
            connection.commit()
            print("Deleted successfully")
            
        elif x == 4:
            cursor.execute('''SELECT * FROM students_details''')
            students_details = cursor.fetchall()
            print("\n All students details in the database.")
            for student in students_details:
                print(student)

        else:
            print("Invalid selection")
        connection.commit()

    def subjects_information(self):
        print("Select operation.\n1:Add subjects.\n2:Show all subjects\n")
        a = int(input("Enter a  number:"))
        
        if a == 1:
            sub_id = int(input("Enter the id of the subject:"))
            sub_name = input("Enter the name of the subject:")
            credit = int(input("Enter credit for the subject:"))
            cursor.execute('''INSERT INTO subjects_information(subject_id,subject_name,credits) VALUES (%s,%s,%s)''',
                           (sub_id, sub_name, credit))
            print("Successfully Inserted.")

        elif a == 2:
            print("Subjects Available.")
            cursor.execute('''SELECT * FROM subjects_information''')
        connection.commit()

    def student_reportcard(self):
        print("Inserting the data:")
        std_id = int(input("Enter the id of the student:"))
        std_1_name = input("enter first name:")
        std_2_name = input("Enter second name:")
        date_of_birth = input("Enter the date of birth:")
        std_gender = input("Enter the gender:")
        std_course = input("Enter the course:")
        std_grade = input("Enter the grade:")
        phone_num = int(input("Enter the phone number:"))
        email = input("Enter email:")
        std_enroll = int(input("Enter the enrollment:"))

        cursor.execute('''INSERT INTO students_reportcard (student_id, first_name, last_name, date_of_birth, gender, course, grade,contact_number, email,enrollment)
         VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (
            std_id, std_1_name, std_2_name, date_of_birth, std_gender, std_course, std_grade, phone_num,
            email, std_enroll))
        connection.commit()

    def insert_marks(self):
        student_ennum = int(input("Enter the enroll of the student:"))
        subject_1_marks = int(input("enter the marks of the subject_1:"))
        subject_2_marks = int(input("enter the marks of the subject_2:"))
        subject_3_marks = int(input("enter the marks of the subject_3:"))
        total_marks = subject_1_marks + subject_2_marks + subject_3_marks

        if total_marks >= 90:
            grades = 'A'
        elif total_marks >= 80:
            grades = 'B'
        elif total_marks >= 70:
            grades = 'C'
        elif total_marks >= 60:
            grades = 'D'
        else:
            grades = 'F'

        cursor.execute(
            ''' INSERT INTO student_marks(student_enroll,subject_1,subject_2,subject_3,total_marks,grades)  VALUES (%s,%s,%s,%s,%s,%s)''',
            (student_ennum, subject_1_marks, subject_2_marks, subject_3_marks, total_marks, grades))
        # connection.commit()
        cursor.execute('''UPDATE student_marks SET total_marks = %s  WHERE student_enroll=%s''',
                       (total_marks, student_ennum))
        print("Successfully inserted")
        connection.commit()

while True:
    std = Student_information()
    x = int(input(
        "Enter the operation you want to perform.\n1:Student Section.\n2:Subject section\n3:Student Reports\n4:Marks Section. \n5:Exit\n"))
    if x == 1:
        std.students_section()
    elif x == 2:
        std.subjects_information()
    elif x == 3:
        std.student_reportcard()
    elif x == 4:
        std.insert_marks()
    elif x == 5:
        break
    else:
        print("Enter a valid value.")