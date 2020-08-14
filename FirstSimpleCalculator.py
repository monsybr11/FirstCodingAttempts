from math import *

number1 = input("input the first number: \n")
number2 = input("input the second number: \n")
choice = input("what do you want to do with them? [add/subtract/multiply/divide/squareroot/exponentiate]\n")

if number1.isnumeric() is False and number2.isnumeric() is False:
    print("both inputs are not numbers or contain a space.")
    exit()

if number1.isnumeric() is False:
    print("the first input is not a number or contains a space.")     # The 3 if statements check if
    exit()                                                            # the inputs are numeric to not cause errors

if number2.isnumeric() is False:
    print("the second input is not a number or contains a space.")
    exit()

number1 = int(number1)
number2 = int(number2)  # Changing the variables from strings into integers to make the math functions possible.

added = number1+number2
subtracted = number1-number2
multiplied = number1*number2
divided = number1/number2                  # These are just variables that i want to use
sqrootedA = sqrt(number1)                  # in later code not to make mess.
sqrootedB = sqrt(number2)
exponentiated = pow(number1, number2)


if choice == "add":
    print(str(number1) + " + " + str(number2) + " = " + str(added))
    exit()

if choice == "subtract":
    print(str(number1) + " - " + str(number2) + " = " + str(subtracted))
    exit()

if choice == "multiply":
    print(str(number1) + " * " + str(number2) + " = " + str(multiplied))
    exit()

if choice == "divide":
    print(str(number1) + " / " + str(number2) + " = " + str(divided))
    exit()

if choice == "squareroot":
    print(str(number1) + " square rooted is " + str(sqrootedA))
    print(str(number2) + " square rooted is " + str(sqrootedB))
    exit()

if choice == "exponantiate":
    print(str(number1) + " ^ " + str(number2) + " = " + str(exponentiated))
    exit()
