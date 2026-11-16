import random
import math

def mathematical_operation():

    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    print("First Number:", num1)
    print("Second Number:", num2)

    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)
    print("Division:", num1 / num2)

    print("Square Root of First Number:", math.sqrt(num1))
    print("Power:", math.pow(num1, 2))
    print("Factorial of First Number:", math.factorial(num1))


# Function call
mathematical_operation()