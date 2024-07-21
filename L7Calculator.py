#CALCULATOR

a=int(input("ENTER FIRST NUMBER:"))
b=int(input("ENTER FIRST NUMBER:"))
c=int(input("Press 1 for Addition \nPress 2 for subtraction\nPress 3 for Division \nPress 4 for Multiplication\nPress 5 for Modlues"))
print(" ")

if c == 1:
    print("Addition of a given number is:" ,a+b)
elif c == 2:
    print("Subtraction of a given number is:", a-b)
elif c ==3:
    print("Division of a given number is:", a/b)
elif c ==4:
    print("Multiplication of a given number is:", a*b)
elif c ==5:
    print("Modulues of a given number is:",a%b )
else:
    print("Please Choose the  Number  From the given option") 
