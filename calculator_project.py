running = True
while running == True:
    operation = input("Enter mathematical operation: ")
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    if operation == "Multiplication":
        sum = num_1 * num_2
        print("The answer is" + str(sum))
    elif operation == "Division":
        sum = num_1 / num_2
        print("The answer is" + str(sum))
    elif operation == "Addition":
        sum = num_1 + num_2
        print("The answer is" + str(sum))
    elif operation == "Subtraction":
        sum = num_1 - num_2
        print("The answer is" + str(sum))
    elif operation == "Exponents":
        sum = num_1 ** num_2
        print("The answer is" + str(sum))
    print("That's everything, Goodbye!")
