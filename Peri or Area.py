#Perimeter/Area of Square/Rectangle
#Perimeter of Square= Side*4       Area of Square= Side*Side
#Perimeter of Rectangle= 2*(l+b)   Area of Rectangle= l*b
print("===================================")
print("Perimeter/Area of Square/Rectangle \n=================================== \n1. Square \n2. Rectangle")
shp=input("Select a Shape: ")
if shp=='1' or shp=='Square':
    print("1. Perimeter \n2. Area")
    oper=input("Select Operation: ")
    if oper=='1' or oper=='Perimeter':
        side=int(input("Enter the side of Square: "))
        print("Perimeter of Square with side",side,"is",4*side,)
    elif oper=='2' or oper=='Area':
        side=int(input("Enter the side of Square: "))
        print("Area of Square with side",side,"is",side*side,)
elif shp=='2' or shp=="Rectangle":
    print("1. Perimeter \n2. Area")
    oper=input("Select Operation: ")
    if oper=='1' or oper=='Perimeter':
        l=int(input("Enter length of the Rectangle: "))
        b=int(input("Enter breadth of the Rectangle: "))
        print("Perimeter of Rectangle with length",l,"and breadth",b,"is",2*(l+b))
    elif oper=='2' or oper=='Area':
        l=int(input("Enter length of the Rectangle: "))
        b=int(input("Enter breadth of the Rectangle: "))
        print("Area of Rectangle with length",l,"and breadth",b,"is",l*b,)