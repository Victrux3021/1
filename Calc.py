#Addition or Subtraction
print("Add or Subract \n======================= \n1. Additon \n2. Subraction \n3. Multiplication \n4. Division")
oper=input("Select Operation: ")
if oper=='1' or oper=='Addition':
    num1=int(input("Enter 1st Number: "))
    num2=int(input("Enter 2nd Number: "))
    print("Sum of",num1,"and",num2,"is",num1+num2,)
    
elif oper=='2' or oper=='Subtraction':
    num1=int(input("Enter 1st Number: "))
    num2=int(input("Enter 2nd Number: "))
    print("Difference between",num1,"and",num2,"is",num1-num2,)

elif oper=='3' or oper=='Multiplication':
    num1=int(input("Enter 1st Number: "))
    num2=int(input("Enter 2nd Number: "))
    print("Product of",num1,"and",num2,"is",num1*num2,)

elif oper=='4' or oper=='Division':
    num1=int(input("Enter The Dividend: "))
    num2=int(input("Enter The Divisor: "))
    print("Quotient of",num1,"and",num2,"is",num1/num2,)