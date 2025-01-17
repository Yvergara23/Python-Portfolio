#Simple Calculator
#Yareli Vergara


#Initialize

#Functions
#Adds 2 numbers together and prints the result
def add (num1, num2):
    result = num1 + num2 #stored in variable called result
    print (result)
def subtract (num1, num2):
    result = num1 - num2
    print (result)
def multiply (num1, num2):
    result = num1 * num2
    print (result)
def divide (num1, num2):
    result = num1/num2
    print (result)

def simpleCalculator():
    print ("Welcome to simple calculator")
    while True:
        print ("""
    Please select an operation: """)
        print ("""
        1. Add
        2. Subtract 
        3. Multiply 
        4. Divide 
        5. Quit
        """)
        operation = int(input ("(1-5) Option: "))
                    #^^ turned into an integer
        if operation == 1: # Will always be false because it needs to be a string
            # When using input, it collects string by default.
            # It automatically stores 1 as a string. Convert to an integer.
            int1 = int(input ("Enter the first number: "))
            int2 = int(input ("Enter the second number: "))
            add (int1, int2)
        if operation == 2:
            int1 = int(input ("Enter the first number: "))
            int2 = int(input ("Enter the second number: "))
            subtract (int1, int2)
        if operation == 3:
            int1 = int(input ("Enter the first number: "))
            int2 = int(input ("Enter the second number: "))
            multiply (int1, int2)
        if operation == 4:
            int1 = int(input ("Enter the first number: "))
            int2 = int(input ("Enter the second number: "))
            divide (int1, int2)
        if operation == 5:
            break

#Main
simpleCalculator()