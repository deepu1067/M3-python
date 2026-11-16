def age_calculator(birth_year):
    current_year = 2026
    age = current_year - birth_year
    return age


try:
    year = int(input("Enter your birth year: "))

    age = age_calculator(year)

    print("Your age is:", age)

except ValueError:
    print("Invalid input! Please enter a valid year.")