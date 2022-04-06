#  Dictionary Comprehension.
# Format #1 is: new_dic = {new_key:new_value for item in list}
# Format #2 is: new_dic = {new_key:new_value for (key,value) in dict.items()}

#  Conditional Dictionary Comprehension.
# Format is: new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random

#  CHALLENGE 1, we have a list of students name,
#   we want to add a random score(number) on each student by Dictionary Comprehension.
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_score = {student:random.randint(1, 100) for student in names}
print(students_score)
# OUTOUT: {'Alex': 91, 'Beth': 39, 'Caroline': 88, 'Dave': 24, 'Eleanor': 62, 'Freddie': 55}

# CHALLENGE 2, now we have to make a new dict of PASSED_STUDENTS, who's got more than or equal 60.
passed_students = {student:score for (student,score) in students_score.items() if score >= 60}
print(passed_students)
# OUTOUT: {'Alex': 91, 'Caroline': 88, 'Eleanor': 62}
