import csv
import openpyxl
import numpy as np

file_csv="student_score.csv"

def create_csv():
    headers=["Name","Subject","Scores"]
    with open(file_csv,mode="w",newline="") as file:
        writer=csv.writer(file)
        writer.writerow(headers)
    print("CSV file created.")
    
def add_data(name,subject,score):
    with open(file_csv,mode="a",newline="")as file:
        writer=csv.writer(file)
        writer.writerow([name,subject,score])
    print("Data added.")
    

def calculation():
    with open(file_csv, mode="r") as file:
        reader = csv.DictReader(file)
        std_data = []
        for row in reader:
            row["Scores"] = float(row["Scores"])
            std_data.append(row)

    std_avg = {}  
    for row in std_data:
        student = row["Name"]
        if student not in std_avg.keys():
            std_avg[student] = [float(row["Scores"])]
        else:
            std_avg[student].append(float(row["Scores"]))

    sub_avg = {}
    for row in std_data:
        subject = row["Subject"]
        if subject not in sub_avg.keys():
            sub_avg[subject] = [float(row["Scores"])]
        else:
            sub_avg[subject].append(float(row["Scores"]))
            
    workbook=openpyxl.Workbook()
    sheet1=workbook.active
    sheet1.title="Student Averages"
    
    sheet1.append(["Name","Average Score"])
    for student, scores in std_avg.items():
        print(f"The mean of {student} is {np.mean(scores)}")
        sheet1.append([student,np.mean(scores)])
        print("Added to xlsx.")
    
    sheet2=workbook.create_sheet(title="Subject Averages")
    sheet2.title="Subject Averages"
    
    sheet2.append(["Subject","Average Score"])
    x={}
    for subject, scores in sub_avg.items():
        print(f"The mean of {subject} is {np.mean(scores)}")
        sheet2.append([subject,np.mean(scores)])
        x[subject]=np.mean(scores)
        print("Added to xlsx.")
                 
    workbook.save("results.xlsx")
    print("Saved in xlsx.")
    print(f"The subject with max average value is {max(x,key=lambda y:x[y])}") 
    
create_csv()
add_data("Alice","Math",85)
add_data("Bob","Math",90)
add_data("Alice","Science",95)
add_data("Bob","Science",80)
add_data("Charlie","Math",70)
add_data("Charlie","Science",75)
calculation()