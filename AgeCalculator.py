#-----------------------Age Calculator-----------------------
from datetime import date

#--------------------------main logic------------------------
def age_calculate(name):
    print(f"******WLECOME {name} , IT IS AN AGE CALCULATOR*******")
    birth_year=int(input("Enter your birth year(e.g. 2005) : "))
    current_year=date.today().year
    return current_year-birth_year

#--------------------------function call---------------------
name=input("Enter your name : ")
print(f"your age is {age_calculate(name)}")

#--------------------------END OF PROGRAM--------------------