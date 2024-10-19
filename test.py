import math
def calc(num1, op, num2): #created a function for basic calculator
    operators = ['+', '-', '*', '/', '%', 'sqrt', 'sqr'] #list of the known operators used in maths on the calculator

    while op in operators:
        if op == "+": #addition
            return num1 + num2
        elif op == "-": #subtraction
            return num1 - num2
        elif op == "*": #multiplication
            return num1 * num2
        elif op == "/": #divison
            return num1 / num2
        elif op == "%": #modulus
            return num1 % num2
        elif op == "sqrt":
            return math.sqrt(num1)
        else:
            return "Nothing."
    else: #for if the "operator" provided by the user is not among the list
        return "Error occured in the calculation. " + op + " is an Invalid Operator"

num1 = float(input("Enter the first number: ")) #for the user to input the first number
op = input("Enter the operator: ") #for the user to input the operator
num2 = float(input("Enter the second number: ")) #for the user to input the second number

print(calc(num1, op, num2))