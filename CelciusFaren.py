#   Blank line

# Define first.

def calculate_wind_chill(temperature, wind_speed):
    if wind_speed < 3:
        return temperature
    else:
        wind_chill = 35.74 + (0.6215 * temperature) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temperature * (wind_speed ** 0.16))
        return wind_chill

def celsius_to_fahrenheit(celsius_temp):
    return (celsius_temp * (9/5)) + 32

# I take help for a friend with some codes definitions...
# Now the main program starts here.

def main():
    while True:
        try:
            temperature_str = input("Enter the temperature, write a number first, then in the write 'F' if it's Fahrenheit or 'C' if Celsius (e.g., 25C or 77F): ")
            if temperature_str[-1].lower() == 'c':
                temperature = celsius_to_fahrenheit(float(temperature_str[:-1]))
            elif temperature_str[-1].lower() == 'f':
                temperature = float(temperature_str[:-1])
            else:
                raise ValueError("Invalid input. Please provide temperature in Celsius (e.g., 25C) or Fahrenheit (e.g., 77F).")
            break
        except ValueError as e:
            print(e)

# The user set the values, then:

    print("\nWind Speed (mph)\tWind Chill")
    print("-----------------------------------")
    for wind_speed in range(5, 61, 5):
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(f"{wind_speed}\t\t\t{wind_chill:.2f}")

if __name__ == "__main__":
    main()