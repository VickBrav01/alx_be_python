FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

def convert_to_celsius(fahrenheit):
    converted = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    print(f"{fahrenheit}°F is {converted}°C")

def convert_to_fahrenheit(celsius):
    converted = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {converted}°F")

if unit == 'c':
    convert_to_fahrenheit(temperature)
elif unit == 'f':
    convert_to_celsius(temperature)
else: 
    print("Invalid")