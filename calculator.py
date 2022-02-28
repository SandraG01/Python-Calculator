
number1 = int(input("Pick a number: "))
number2 = int(input("Pick a second number: "))
decision_number = int(input("1) Addition \n2) Subtraction \n3) Multiplication \n4) Division \n Pick a number: "))

if decision_number == 1:
    sum = number1 + number2
    print(f"{number1} + {number2} = {sum}")
elif decision_number == 2:
    subtraction = number1 - number2
    print(subtraction)
elif decision_number == 3:
    multiplication = number1 * number2
    print(multiplication)
elif decision_number == 4:
    division = number1 / number2
    print(division)
else:
    print("You chose to leave")
