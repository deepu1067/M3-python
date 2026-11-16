

def sum_of_numbers(n):
    total = 0

    for i in range(n + 1):
        total = total + i

    return total


# Function call with argument
result = sum_of_numbers(10)

print("Sum of whole numbers:", result)