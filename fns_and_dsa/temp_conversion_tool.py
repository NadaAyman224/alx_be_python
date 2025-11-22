# Global variables:
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


# User inputs:
temp = float(input("Enter the temperature to convert: "))
type_temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()


# Conversion Functions:
def convert_to_celsius(fahrenheit):
    celsius_temp = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius_temp}°C")

    #return celsius_temp

def convert_to_fahrenheit(celsius):
    fahrenheit_temp = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    print(f"{celsius}°C is {fahrenheit_temp}°F")

    #return fahrenheit_temp


# Main Body:
if type_temp == 'F' :
    convert_to_celsius(temp)

elif type_temp == 'C' :
    convert_to_fahrenheit(temp)

else:
    print("Invalid temperature. Please enter a numeric value.")


