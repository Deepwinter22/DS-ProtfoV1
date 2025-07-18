#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Jaxon Dierker 
Date: 07/17/2023
Description: Generates student transcript.
    
"""

import csv
from GPA import * 

student_fileCreate = student_name_in + '.csv' #Creates student file 

while True:
    new_existing_query = input('Would you like to add a new student, append course to existing student, report on student, or quit?\nPlease type "new","existing","report", or "quit": ').lower()
    if new_existing_query == 'new':
        
            student_id_in = input('Enter student ID number : ')
            student_name_in = input('Enter student first and last name : ')
            student_info = ('Student_type', student_id_in,student_name_in)
            
            print('Here is the info you entered:',student_info)
            
            with open(student_fileCreate,'a',newline='') as student_csv_file: #Creates new student csv 
                fieldnames = ['Type','Semester','Course abbreviation','Course Number','Course Name','Credits','Grade','Quality Points']
                writer = csv.writer(student_csv_file)
                writer.writerow(student_info)
                writer.writerow(fieldnames)
                student_csv_file.close()
    
    elif new_existing_query == 'existing': #Loop opens file on existing student to add course info 
            
            semester_taken = input('Enter semester course was taken in year/season(20/FA): ')
            department_abbreviation = input('Enter department abbreviation : ')
            course_number = input('Enter course number : ')
            course_name = input('Enter the full course name : ')
            course_credits = float(input('Enter credit number for course : '))
            letter_grade = input('Enter letter grade achieved in course: ').upper()
            
            with open(student_fileCreate, 'a', newline='') as student_csv_file: #Writes existing student course info to csv
                writer = csv.writer(student_csv_file)
                gpa = GPA(department_abbreviation, course_number, course_name, course_credits, semester_taken, letter_grade)
                writer.writerow(('Course_type', semester_taken, department_abbreviation, course_number, course_name, course_credits, letter_grade, gpa.getQualitypoints()))
   
    elif new_existing_query == 'report': #Provides info on student transcript(called csv)
        total_qualpts = 0
        total_credits = 0 
        semesters=set() #Unique to set is it will only store one copy
        with open(student_fileCreate,'r', newline='') as student_csv_file: #Reads student csv and prints
            reader = csv.reader(student_csv_file)
            for row in reader:
                if row[0]== 'Course_type' : 
                    total_qualpts += float(row[7])
                    total_credits += float(row[5])
                    semesters.add(row[1])
        cumulative_gpa = total_qualpts/total_credits
        print('Cumulative GPA:',round(cumulative_gpa,2),'Total Credits:',total_credits, 'Total Quality Points:',round(total_qualpts,2))
        for semester in semesters: #orders semesters in the set()
            with open(student_fileCreate, 'r', newline='') as student_csv_file:
                reader = csv.reader(student_csv_file)
                for row in reader: 
                    if row[0] == 'Course_type' and row[1] == semester: #Finds alike semesters and groups them 
                        print(row)
    elif new_existing_query == 'quit':
        student_csv_file.close()
        break
    else:
        print('Please type new, existing, report, or quit')
        continue 

'''
runfile('/Users/jaxondierker/Documents/DS510 /DSProj1.py', wdir='/Users/jaxondierker/Documents/DS510 ')
Reloaded modules: Course, GPA
Would you like to add a new student, append course to existing student, report on student, or quit?
Please type "new","existing","report", or "quit": existing
Enter semester course was taken in year/season(20/FA): 19/FA
Enter department abbreviation : TH
Enter course number : 213
Enter the full course name : Theater
Enter credit number for course : 3
Enter letter grade achieved in course: A
Would you like to add a new student, append course to existing student, report on student, or quit?
Please type "new","existing","report", or "quit": existing
Enter semester course was taken in year/season(20/FA): 19/FA
Enter department abbreviation : CH
Enter course number : 314
Enter the full course name : Chemistry Fundamentals
Enter credit number for course : 3
Enter letter grade achieved in course: B
Would you like to add a new student, append course to existing student, report on student, or quit?
Please type "new","existing","report", or "quit": existing
Enter semester course was taken in year/season(20/FA): 19/SP
Enter department abbreviation : BO
Enter course number : 496
Enter the full course name : Proteomics
Enter credit number for course : 4
Enter letter grade achieved in course: B-
Would you like to add a new student, append course to existing student, report on student, or quit?
Please type "new","existing","report", or "quit": existing
Enter semester course was taken in year/season(20/FA): 20/FA
Enter department abbreviation : CS
Enter course number : 560
Enter the full course name : Python II
Enter credit number for course : 3
Enter letter grade achieved in course: A-
Would you like to add a new student, append course to existing student, report on student, or quit?
Please type "new","existing","report", or "quit": existing
Enter semester course was taken in year/season(20/FA): 20/FA
Enter department abbreviation : GH
Enter course number : 213
Enter the full course name : Drama
Enter credit number for course : 3
Enter letter grade achieved in course: A

Would you like to add a new student, append course to existing student, report on student, or quit?
Please type "new","existing","report", or "quit": report

Cumulative GPA: 3.3 Total Credits: 30.0 Total Quality Points: 98.86

['Course_type', '19/SP', 'BMB', '230', 'Molecular Cell Biology', '4', 'B-', '10.64']
['Course_type', '19/SP', 'BMB', '480', 'Immunology', '3', 'A-', '10.98']
['Course_type', '19/SP', 'BO', '496', 'Proteomics', '4.0', 'B-', '10.64']
['Course_type', '19/FA', 'DS', '510', 'Computer Science Fundamentals', '4', 'A-', '14.64']
['Course_type', '19/FA', 'TH', '213', 'Theater', '3.0', 'A', '12.0']
['Course_type', '19/FA', 'CH', '314', 'Chemistry Fundamentals', '3.0', 'B', '9.0']
['Course_type', '20/FA', 'DS', '512', 'Computer', '3', 'B-', '7.98']
['Course_type', '20/FA', 'CS', '560', 'Python II', '3.0', 'A-', '10.98']
['Course_type', '20/FA', 'GH', '213', 'Drama', '3.0', 'A', '12.0']
Would you like to add a new student, append course to existing student, report on student, or quit?
Please type "new","existing","report", or "quit": quit

'''
