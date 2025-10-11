FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_fahrenheit(celsius):
            result = (celsius  * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
            return f"{celsius}°C is {result}°F"
def convert_to_celsius(fahrenheit):
            result = FAHRENHEIT_TO_CELSIUS_FACTOR  * (fahrenheit - 32)
            return f"{fahrenheit}°F is {result}°C"

try:
    Temp = float(input("Enter the tempreture to convert: "))
    Temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if Temp_type == "F":
        print(convert_to_celsius(Temp))
    elif Temp_type == "C":
        print(convert_to_fahrenheit(Temp))
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")    
    