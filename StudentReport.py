#--------***-----Student Marks Report-----***---------

def calculate_grade(avg):
    if avg>=90:
        return 'O'
    elif avg>=80:
        return 'A+'
    elif avg>=70:
        return 'A'
    elif avg>=60:
        return 'B'
    elif avg>=50:
        return 'C'
    elif avg>=40:
        return 'P'
    else:
        return 'F'
    
#------------------input number of student----------------------

sNum=int(input("Enter Number of Students="))
subjects=["Physics","Chemistry","Maths"]
students={}

#-------------------------data collection-------------------------

for _ in range(sNum):
    name=input("Enter student name=")
    marks=[]
    for subject in subjects:
        score=int(input(f"Enter score of {subject} out of 100 ="))
        marks.append(score)

    total=sum(marks)
    avg=total/len(subjects)
    grade = calculate_grade(avg)

    students[name]={
        'Marks': dict(zip(subjects,marks)),
        'Total':total,
        'Average':avg,
        'Grade':grade   
    }

#--------------------------Report display--------------------------

print("------Student Marks Report-----")
for name,data in students.items():
    print(f"\nName={name}")
    for subject,score in data["Marks"].items():
        print(f"{subject}={score}")
    print(f"Total= {data['Total']}")
    print(f"Average={data['Average']:.2f}")
    print(f"Grade= {data['Grade']}")

#----------------------------END OF PROGRAM-------------------------






    