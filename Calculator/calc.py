#add, subtract, multiply, divide
#how do we do this? check for proper inputs or just force user to input values for any 
#   function

def add(val1, val2):
    return str(val1+val2)

def subtract(val1, val2):
    return str(val1-val2)

def multiply(val1, val2):
    return str(val1*val2)

def divide(val1, val2):
    if(val2 == 0):
        return "NOTHING! Hahaha, nice try buddy, you almost destroyed the space-time continuum, no div by 0"

    return str(val1 / val2)

def handleStrExcep(operStr):
    isNumber = False

    while(not(isNumber)):
        try:
            inputVal = int(input("Enter your " + operStr + " operand: "))
            isNumber = True
        except ValueError:
            print("ERROR -> Enter an appropriate value please (no words, letters, or special characters)\n", end = "")
            isNumber = False

    return inputVal


#main

#Get inputs from user
#Check to make sure inputs are valid

#Learned: input function gets a string, we need to convert it

#our input value
inputVal = -1

while(inputVal != 5 and inputVal != "n" and inputVal != "N"):

    while(inputVal != 1 and inputVal != 2 and inputVal != 3 and inputVal != 4 and inputVal != 5):
        try:
            inputVal = int(input("\nSelect your operation: \n1. Addition\n2. Subtraction\n3. Multiplication \n4. Divsion\n5. Quit\nResponse: "))
        except ValueError:
            print("Enter an appropriate value please (no words, letters, or special characters)\n")

        if(inputVal == 5):
            print("Understandable, have a nice day")
            exit()

    operand1 = handleStrExcep("first")
    operand2 = handleStrExcep("second")

#Learned, you can't concat integers without modifying

    if(inputVal == 1):
        print("Your result of adding " + str(operand1) + " to " + str(operand2) + " is " + add(operand1, operand2))
    elif(inputVal == 2):
        print("Your result of subtracting " + str(operand1) + " from " + str(operand2) + " is " + subtract(operand1, operand2))
    elif(inputVal == 3):
        print("Your result of multiplying " + str(operand1) + " by " + str(operand2) + " is " + multiply(operand1, operand2))
    elif(inputVal == 4):
        print("Your result of dividing " + str(operand1) + " by " + str(operand2) + " is " + divide(operand1, operand2))
    

    inputVal = input("Would you like to continue? (y/n)")