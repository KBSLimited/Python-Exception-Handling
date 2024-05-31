#Task 1: Start

def get_temperature():
    while True:
        try:
            temperature = float(input("Enter the temperature in Fahrenheit: "))
            return temperature
        except ValueError:
            print("Error: Please enter a valid numerical value for temperature.")

temperature_fahrenheit = get_temperature()
print("Temperature entered:", temperature_fahrenheit, "F")

#Task 2: Temperature Conversion

def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    except ZeroDivisionError:
        print("Error: Division by zero occurred during the conversion.")
        return None
    except OverflowError:
        print("Error: Overflow occurred during the conversion.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return None

# Test the function with a Fahrenheit temperature
temperature_fahrenheit = 72  # Example Fahrenheit temperature
temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
if temperature_celsius is not None:
    print(f"{temperature_fahrenheit} Fahrenheit is equal to {temperature_celsius:.2f} Celsius.")

#Task 3: User Experience

def get_temperature():
    while True:
        try:
            temperature = float(input("Enter the temperature in Fahrenheit: "))
            return temperature
        except ValueError:
            print("Error: Please enter a valid numerical value for temperature.")

def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5 / 9
    except ZeroDivisionError:
        print("Error: Division by zero occurred during the conversion.")
        return None
    except OverflowError:
        print("Error: Overflow occurred during the conversion.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return None
    else:
        print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")
        return celsius
    finally:
        print("Thank you for using the weather forecast application!")

temperature_fahrenheit = get_temperature()
print("Temperature entered:", temperature_fahrenheit, "F")
fahrenheit_to_celsius(temperature_fahrenheit)