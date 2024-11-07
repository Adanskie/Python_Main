def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Input from the user
celsius = float(input("Enter the temperature in Celsius: "))

# Convert the temperature and display the result
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F.")


