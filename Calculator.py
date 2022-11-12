from sympy import Symbol, solve
import math
print("Hello,and welcome to this simple usage calculator,here is the available math operations:")
print("1)Addition")
print("2)Substraction")
print("3)Multiplication")
print("4)Devision")
print("5)Power")
print("6)No floating points")
print("7)Square root")
print("8)Solving equations ")
print('''ATTENTION!: -Only equations from the first degree are solved and with x as an variable  ''')

choice = input("Enter your choice : ")

if choice == "1":
    num1 = float(input("Enter Number 1 : "))
    num2 = float(input("Enter Number 2 : "))
    print(num1, "+", num2, "=", (num1+num2))
    
elif choice == "2":
    num1 = float(input("Enter Number 1 : "))
    num2 = float(input("Enter Number 2 : "))
    print(num1, "-", num2, "=", (num1-num2))
    
elif choice == "3":
    num1 = float(input("Enter Number 1 : "))
    num2 = float(input("Enter Number 2 : "))
    print(num1, "*", num2, "=", (num1*num2))
    
elif choice == "4":
    num1 = float(input("Enter Number 1 : "))
    num2 = float(input("Enter Number 2 : "))
    if num2 == 0.0:
        print("Divide by 0 Error")
    else:
        print(num1, "/", num2, "=", (num1/num2)) 
    
elif choice == "5":
    num = float(input("Enter Number  : "))
    power = float(input("Enter the power  : "))
    print(num, "**",power, "=", (num**power))

elif choice == "6":
    num1 = float(input("Enter Number 1 : "))
    num2 = float(input("Enter Number 2 : "))
    if num2 == 0.0:
        print("Divide by 0 Error")
    else:
        print(num1, "/", num2, "=", (num1//num2))
        
elif choice == "7":
    num = float(input("Enter Number : "))
    print("√", num, "=", (math.sqrt(num)))        

elif choice == "8":
    exp = input("Enter the equation to be solved: ")
    x = Symbol('x')
    solution = solve (exp)
    print("The solution is: x= ",solution)
    
else:
    print("invalic choice")

feedback = input("Are you satisfied with this calculator((Y)Yes or (N)No): ")
if feedback == "Y":
    print("Thanks for your feedback")
elif feedback == "N":
    print("We're so sorry,we're going to improve our calculator")

else:
    print("Invalic Choice")

