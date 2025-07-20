import math
import time
# 
def countdown(end , start = 0):
    print(f"Opening your Calculator in {end} seconds")
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("HERE IS YOUR CALCULATOR.....")
    
countdown(10)

# 
def display_menu():
    """Displays the main menu of the calculator."""
    print("\n--- Advanced Calculator Menu ---")
    print("1. Basic Arithmetic Operations")
    print("2. Trigonometric Functions")
    print("3. Trigonometric Conversions")
    print("4. Measurement Conversions")
    print("5. Number Base Conversions")
    print("6. Other Conversions")
    print("7. exit")
    print("------------------------------")

def basic_arithmetic():
    print("\n--- Basic Arithmetic ---")
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /, %, mod): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operator.")
            
            return
        print(f"Result: {num1} {operator} {num2} = {result}")
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

def trigonometric_functions():
    print("\n--- Trigonometric Functions ---")
    print("1. Sine (sin)")
    print("2. Cosine (cos)")
    print("3. Tangent (tan)")
    print("4. ITF")
    
    
    choice = input("Enter your choice: ")

    try:
        angle_deg = float(input("Enter angle in degrees: "))
        angle_rad = math.radians(angle_deg) # Convert to radians for math functions
        if choice == '1':
            result = math.sin(angle_rad)
            print(f"sin({angle_deg}°) = {result}")
        
        elif choice == '2':
           result = math.cos(angle_rad)
           print(f"cos({angle_deg}°) = {result}")

        elif choice == '3':
    # Check for angles where tan is undefined (90
            if abs(math.cos(angle_rad)) < 1e-9: # Check i
                print(f"tan({angle_deg}°) is undefined.")
            else:
                result = math.tan(angle_rad)
                print(f"tan({angle_deg}°) = {result}")
        
        elif choice == '4':
            print("INVERSE TRIGNO FUNCTIONS WILL BE INTRODUCED SOON....")
        
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def trigonometric_conversions():
    """Handles conversions between degrees and radians."""
    print("\n--- Trigonometric Conversions ---")
    print("1. Degrees to Radians")
    print("2. Radians to Degrees")
    choice = input("Enter your choice: ")

    try:
        if choice == '1':
            degrees = float(input("Enter angle in degrees: "))
            radians = math.radians(degrees)
            print(f"{degrees}° = {radians} radians")
        elif choice == '2':
            radians = float(input("Enter angle in radians: "))
            degrees = math.degrees(radians)
            print(f"{radians} radians = {degrees}°")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")
  
def measurement_conversions():
    """Handles basic measurement conversions."""
    print("\n--- Measurement Conversions ---")
    print("1. Centimeters to Inches")
    print("2. Inches to Centimeters")
    print("3. Kilograms to Pounds")
    print("4. Pounds to Kilograms")
    print("5. Meters to Feet")
    print("6. Feet to Meters")
    choice = input("Enter your choice: ")
  
    try:
        if choice == '1':
            cm = float(input("Enter length in centimeters: "))
            inches = cm / 2.54
            print(f"{cm} cm = {inches:.2f} inches")
        elif choice == '2':
            inches = float(input("Enter length in inches: "))
            cm = inches * 2.54
            print(f"{inches} inches = {cm:.2f} cm")
        elif choice == '3':
            kg = float(input("Enter mass in kilograms: "))
            lbs = kg * 2.20462
            print(f"{kg} kg = {lbs:.2f} lbs")
        elif choice == '4':
            lbs = float(input("Enter mass in pounds: "))
            kg = lbs / 2.20462
            print(f"{lbs} lbs = {kg:.2f} kg")
        elif choice == '5':
            meters = float(input("Enter length in meters: "))
            feet = meters * 3.28084
            print(f"{meters} m = {feet:.2f} ft")
        elif choice == '6':
            feet = float(input("Enter length in feet: "))
            meters = feet / 3.28084
            print(f"{feet} ft = {meters:.2f} m")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def number_base_conversions():
    """Handles decimal to binary and binary to decimal conversions."""
    print("\n--- Number Base Conversions ---")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    choice = input("Enter your choice: ")

    try:
        if choice == '1':
            decimal = int(input("Enter a decimal number: "))
            binary = bin(decimal).replace("0b", "")
            print("Converting decimal to binary...")
            print(f"Decimal {decimal} = Binary {binary}")
        elif choice == '2':
            binary = input("Enter a binary number: ")
            decimal = int(binary)
            if not all(c in '01' for c in binary_str):
                print("Invalid binary number. Please use only 0s and 1s.")
                return
            decimal = int(binary_str, 2)
            print(f"Binary {binary_str} = Decimal {decimal}")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a valid integer or binary string.")
    except Exception as e:
        print(f"An error occurred: {e}")

def other_conversions():
    print("\n--- Other Conversions ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter your choice: ")

    try:
        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F = {celsius:.2f}°C")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function to run the calculator."""
    while True:
        display_menu()
        main_choice = input("Enter your choice (1-8): ") # Updated range
        if main_choice == '1':
            basic_arithmetic()
        elif main_choice == '2':
            trigonometric_functions()
        elif main_choice == '3':
            trigonometric_conversions()
        elif main_choice == '4':
            measurement_conversions()
        elif main_choice == '5':
            number_base_conversions()
        elif main_choice == '6':
            other_conversions()
    
        
        elif main_choice == '7': # Updated exit option
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
 