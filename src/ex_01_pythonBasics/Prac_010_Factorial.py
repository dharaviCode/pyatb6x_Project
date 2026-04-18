try:
    input_num = int(input("Enter a number: "))

    if input_num < 0:
        print("Negative number", input_num)
    else:
        fact = 1
        for i in range(1, input_num + 1):
            fact = i * fact

        print("factorial of", input_num, "is", fact)

except ValueError:
        print("Invalid input")
