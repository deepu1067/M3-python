def calculator(num1, num2, operator):

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero!"

    else:
        return "Invalid operator!"


# Function calls
print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))