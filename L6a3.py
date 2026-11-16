import datetime
import time
import calendar

def trip_expenditure():

    print("===== TRIP EXPENDITURE CALCULATOR =====")

    # Get trip information
    destination = input("Enter destination: ")

    start_date = input("Enter starting date (YYYY-MM-DD): ")
    end_date = input("Enter ending date (YYYY-MM-DD): ")

    # Convert input into date format
    start = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

    # Calculate trip duration
    duration = (end - start).days

    if duration < 0:
        print("Error! Ending date cannot be before starting date.")
        return

    # Get expenditure
    transport = float(input("Enter transportation cost: "))
    hotel = float(input("Enter hotel cost: "))
    food = float(input("Enter food cost: "))
    shopping = float(input("Enter shopping cost: "))
    other = float(input("Enter other expenses: "))

    # Calculate total expenditure
    total = transport + hotel + food + shopping + other

    # Display current date and time
    current = datetime.datetime.now()

    print("\n===== TRIP SUMMARY =====")

    print("Destination:", destination)
    print("Starting Date:", start)
    print("Ending Date:", end)
    print("Trip Duration:", duration, "days")

    print("\n===== EXPENDITURE =====")

    print("Transportation:", transport)
    print("Hotel:", hotel)
    print("Food:", food)
    print("Shopping:", shopping)
    print("Other Expenses:", other)

    print("-----------------------------")
    print("Total Expenditure:", total)

    # Calculate daily expenditure
    if duration > 0:
        print("Average Daily Cost:", round(total / duration, 2))

    print("\nCurrent Date:", current.date())
    print("Current Time:", current.strftime("%I:%M:%S %p"))

    # Display travel month calendar
    print("\n===== TRAVEL MONTH CALENDAR =====")
    print(calendar.month(start.year, start.month))


# Function call
trip_expenditure()