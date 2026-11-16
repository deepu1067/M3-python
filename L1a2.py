def check_weather(condition):

    if condition == "sunny":
        print("It's a sunny day! Enjoy the sunshine.")

    elif condition == "rainy":
        print("It's raining! Don't forget your umbrella.")

    elif condition == "cloudy":
        print("It's cloudy today. It might rain.")

    elif condition == "windy":
        print("It's a windy day! Be careful outside.")

    elif condition == "snowy":
        print("It's snowing! Stay warm.")

    else:
        print("Unknown weather condition.")


# Function calls
check_weather("sunny")
check_weather("rainy")
check_weather("cloudy")