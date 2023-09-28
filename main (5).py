'''implement a function called sort_students that takes a list of
student objects an input and sorts the list based on their CGPA(Cumulative Grade Point Average) in descending order.
each student object has the following attributes:name(string),roll_number 
(string),and cgpa(float).test the function with different input lists 
 of students.'''

class Students:
  
  def __init__(self,name,roll_number,cgpa):
    self.name = name 
    self.roll_number = roll_number 
    self.cgpa = cgpa 

def sort_students(student_list):
    # Sort the list of student objects based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda x: x['cgpa'], reverse=True)
    return sorted_students
# Define a list of student objects
students = [
    {'name': 'Adhi', 'roll_number': 'A101', 'cgpa': 3.8},
    {'name': 'Banu', 'roll_number': 'B102', 'cgpa': 3.9},
    {'name': 'Chandru', 'roll_number': 'C103', 'cgpa': 3.7},
    {'name': 'Devi', 'roll_number': 'D104', 'cgpa': 3.95},
]

# Sort the students based on CGPA
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, CGPA: {student['cgpa']}")

      




