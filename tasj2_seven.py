from openpyxl import Workbook
grades={
    'student':['Samiksha', 'Shristi', 'Khubsu', 'Sabikshya'],
    'Grade':[100,80,90,90] 
}
workbook=Workbook()
sheet=workbook.active
sheet.title="Grades"
sheet.append(['Student', 'Grades'])
for student, grade in zip(grades['student'], grades['Grade']):
    sheet.append([student, grade])

workbook.save('student_grade.xlsx')











from openpyxl import Workbook

# Sample data
grades = {
    'Student': ['Alice', 'Bob', 'Charlie'],
    'Grade': [88, 92, 79]
}

# Create a new workbook and select the active worksheet
workbook = Workbook()
sheet = workbook.active
sheet.title = "Grades"

# Write headers
sheet.append(['Student', 'Grade'])

# Write data
for student, grade in zip(grades['Student'], grades['Grade']):
    sheet.append([student, grade])

# Save the workbook
workbook.save('student_grades.xlsx')
