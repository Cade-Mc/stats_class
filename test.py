# CSS1 = {'Name':[], 'Quiz1':[], 'Quiz2':[], 'Quiz3':[]}
#
# # Write a function - add_record(record, student_name, points).
# # This will add the details of a student(name, points for 3 quizzes) into the dictionary 'record'.
# def add_record(record, student_name, points):
#     record['Name'].append(student_name)
#     for k,v in points:
#         record[k] = v
#     return record
#
# # Use this function twice to add scores of 2 students to the dictionary CSS1
# add_record(CSS1, 'Chandra', Quiz1 = 4, Quiz2 = 3, Quiz3 = 5)
# add_record(CSS1, 'Bella', Quiz1 = 1, Quiz2 = 3.5, Quiz3 = 6)
#
# CSS1 = {'Name':[], 'Quiz1':[], 'Quiz2':[], 'Quiz3':[]}
#
# def add_record(record, student_name, *points):
#     record['Name'].append(student_name)
#     for k,v in points:
#         record[k] = v
#     return record
#
# # Use this function twice to add scores of 2 students to the dictionary CSS1
# add_record(CSS1, 'Chandra', 4, 3, 5)
# add_record(CSS1, 'Bella', 1, 3.5, 6)
