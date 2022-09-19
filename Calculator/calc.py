#add, subtract, multiply, divide
#how do we do this? check for proper inputs or just force user to input values for any 
#   function

def add(val1, val2):
    return val1+val2

def subtract(val1, val2):
    return val1-val2

def multiply(val1, val2):
    return val1*val2

def divide(val1, val2):
    return val1 / val2


#main

#Get inputs from user
#Check to make sure inputs are valid

while(input != 5):
    input = input("Select your operation: \n1. Addition\n2. Subtraction\n3. Multiplication \n4. Divsion\n5. Quit")

    while(input != 1 or input != 2 or input != 3 or input != 4 or input != 5):
        #Force user to input valid data
        input = input("Select your operation: \n1. Addition\n2. Subtraction\n3. Multiplication \n4. Divsion\n5. Quit")

    if(input == 1)

    elif(input == 2)

    elif(input == 3)

    elif(input == 4)

    elif(input == 5)
        print("Understandable, have a nice day")
        exit()