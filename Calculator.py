#Calcultor using fundamentals of Python
print("Press '1' for Addition")
print("Press '2' for Subtraction")
print("Press '3' for Multiplication")
print("Press '4' for Division")
print("Press '5' for Exit")

#logic
while True:

    #input from user
    op=int(input("choose operation : "))
    if(op==4):
        print("Keep in mind second number not be zero(0)")
    if(op!=5):
        num1=float(input("Enter first number="))
        num2=float(input("Enter second number="))
   
    match op:
        
        case 1:
            print("Addition of two numbers is ",num1+num2)

        case 2:
            print("Subtraction of two numbers is ",num1-num2)

        case 3:
            print("Multiplication of two numbers is ",num1*num2)

        case 4:
            if(num2==0):
                print("ERROR:A Number can not be divide by Zero(0) ")
                continue
            print("Division of two numbers is ",num1/num2)

        case 5:
            print("---EXIT---")
            break

        case _:
            print("Invalid Operation")

#---------------------End of Program----------------------------
