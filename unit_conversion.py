# ================================================================
#              UNIT CONVERSION APPLICATION
# ================================================================
# This program is a menu-driven unit conversion application.
# It supports multiple types of unit conversions.
#
# Conversion Categories:
# 1. Length
# 2. Weight / Mass
# 3. Temperature
# 4. Time
# 5. Area
# 6. Volume
# 7. Speed
# 8. Digital Storage
# 9. Data Rate
# 10. Pressure
# 11. Energy

# The program also contains:
# - Input validation
# - Error handling
# - Repeated conversion option
# - Main menu
# - Comments for easy understanding
# ================================================================


# ------------------------------------------------
# FUNCTION: Display application heading
# ------------------------------------------------
def show_heading():
    print("\n" + "=" * 60)
    print("              UNIT CONVERSION APPLICATION")
    print("=" * 60)


# ------------------------------------------------
# FUNCTION: Display main menu
# ------------------------------------------------
def main_menu():
    show_heading()
    print("\nChoose a Conversion:")
    print("1.  Length")
    print("2.  Weight / Mass")
    print("3.  Temperature")
    print("4.  Time")
    print("5.  Area")
    print("6.  Volume")
    print("7.  Speed")
    print("8.  Digital Storage")
    print("9.  Data Rate")
    print("10. Pressure")
    print("11. Energy")
    print("0.  Exit")
    print("-" * 60)


# ------------------------------------------------
# FUNCTION: Get a valid number from user
# ------------------------------------------------
def get_number(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("Invalid input! Please enter a number.")


# ------------------------------------------------
# FUNCTION: Display result
# ------------------------------------------------
def display_result(value, from_unit, result, to_unit):
    print("\n" + "-" * 60)
    print(f"Result: {value:g} {from_unit} = {result:.6f} {to_unit}")
    print("-" * 60)


# ================================================================
#                       LENGTH CONVERSION
# ================================================================

def length_conversion():
    print("\n========== LENGTH CONVERSION ==========")
    print("1. Meter")
    print("2. Kilometer")
    print("3. Centimeter")
    print("4. Millimeter")
    print("5. Mile")
    print("6. Yard")
    print("7. Foot")
    print("8. Inch")

    units = {
        "1": ("Meter", 1),
        "2": ("Kilometer", 1000),
        "3": ("Centimeter", 0.01),
        "4": ("Millimeter", 0.001),
        "5": ("Mile", 1609.344),
        "6": ("Yard", 0.9144),
        "7": ("Foot", 0.3048),
        "8": ("Inch", 0.0254)
    }

    from_choice = input("Enter source unit: ")
    if from_choice not in units:
        print("Invalid unit!")
        return

    to_choice = input("Enter target unit: ")
    if to_choice not in units:
        print("Invalid unit!")
        return

    value = get_number("Enter value: ")

    from_name, from_factor = units[from_choice]
    to_name, to_factor = units[to_choice]

    meters = value * from_factor
    result = meters / to_factor

    display_result(value, from_name, result, to_name)


# ================================================================
#                    WEIGHT / MASS CONVERSION
# ================================================================

def weight_conversion():
    print("\n========== WEIGHT / MASS CONVERSION ==========")
    print("1. Kilogram")
    print("2. Gram")
    print("3. Milligram")
    print("4. Tonne")
    print("5. Pound")
    print("6. Ounce")

    units = {
        "1": ("Kilogram", 1),
        "2": ("Gram", 0.001),
        "3": ("Milligram", 0.000001),
        "4": ("Tonne", 1000),
        "5": ("Pound", 0.45359237),
        "6": ("Ounce", 0.0283495231)
    }

    from_choice = input("Enter source unit: ")
    if from_choice not in units:
        print("Invalid unit!")
        return

    to_choice = input("Enter target unit: ")
    if to_choice not in units:
        print("Invalid unit!")
        return

    value = get_number("Enter value: ")

    from_name, from_factor = units[from_choice]
    to_name, to_factor = units[to_choice]

    kilograms = value * from_factor
    result = kilograms / to_factor

    display_result(value, from_name, result, to_name)


# ================================================================
#                    TEMPERATURE CONVERSION
# ================================================================

def temperature_conversion():
    print("\n========== TEMPERATURE CONVERSION ==========")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")

    units = {
        "1": "Celsius",
        "2": "Fahrenheit",
        "3": "Kelvin"
    }

    from_choice = input("Enter source unit: ")
    if from_choice not in units:
        print("Invalid unit!")
        return

    to_choice = input("Enter target unit: ")
    if to_choice not in units:
        print("Invalid unit!")
        return

    value = get_number("Enter temperature: ")

    from_name = units[from_choice]
    to_name = units[to_choice]

    # First convert source temperature to Celsius.
    if from_choice == "1":
        celsius = value
    elif from_choice == "2":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    # Then convert Celsius to target unit.
    if to_choice == "1":
        result = celsius
    elif to_choice == "2":
        result = (celsius * 9 / 5) + 32
    else:
        result = celsius + 273.15

    display_result(value, from_name, result, to_name)


# ================================================================
#                       TIME CONVERSION
# ================================================================

def time_conversion():
    print("\n========== TIME CONVERSION ==========")
    print("1. Second")
    print("2. Minute")
    print("3. Hour")
    print("4. Day")
    print("5. Week")

    units = {
        "1": ("Second", 1),
        "2": ("Minute", 60),
        "3": ("Hour", 3600),
        "4": ("Day", 86400),
        "5": ("Week", 604800)
    }

    from_choice = input("Enter source unit: ")
    if from_choice not in units:
        print("Invalid unit!")
        return

    to_choice = input("Enter target unit: ")
    if to_choice not in units:
        print("Invalid unit!")
        return

    value = get_number("Enter value: ")

    from_name, from_factor = units[from_choice]
    to_name, to_factor = units[to_choice]

    seconds = value * from_factor
    result = seconds / to_factor

    display_result(value, from_name, result, to_name)


# ================================================================
#                       AREA CONVERSION
# ================================================================

def area_conversion():
    print("\n========== AREA CONVERSION ==========")
    print("1. Square Meter")
    print("2. Square Kilometer")
    print("3. Square Centimeter")
    print("4. Square Foot")
    print("5. Square Inch")
    print("6. Acre")
    print("7. Hectare")

    units = {
        "1": ("Square Meter", 1),
        "2": ("Square Kilometer", 1000000),
        "3": ("Square Centimeter", 0.0001),
        "4": ("Square Foot", 0.09290304),
        "5": ("Square Inch", 0.00064516),
        "6": ("Acre", 4046.8564224),
        "7": ("Hectare", 10000)
    }

    from_choice = input("Enter source unit: ")
    if from_choice not in units:
        print("Invalid unit!")
        return

    to_choice = input("Enter target unit: ")
    if to_choice not in units:
        print("Invalid unit!")
        return

    value = get_number("Enter value: ")

    from_name, from_factor = units[from_choice]
    to_name, to_factor = units[to_choice]

    square_meters = value * from_factor
    result = square_meters / to_factor

    display_result(value, from_name, result, to_name)


# ================================================================
#                       VOLUME CONVERSION
# ================================================================

def volume_conversion():
    print("\n========== VOLUME CONVERSION ==========")
    print("1. Liter")
    print("2. Milliliter")
    print("3. Cubic Meter")
    print("4. Cubic Centimeter")
    print("5. Gallon")
    print("6. Quart")
    print("7. Pint")

    units = {
        "1": ("Liter", 1),
        "2": ("Milliliter", 0.001),
        "3": ("Cubic Meter", 1000),
        "4": ("Cubic Centimeter", 0.001),
        "5": ("Gallon", 3.785411784),
        "6": ("Quart", 0.946352946),
        "7": ("Pint", 0.473176473)
    }

    from_choice = input("Enter source unit: ")
    if from_choice not in units:
        print("Invalid unit!")
        return

    to_choice = input("Enter target unit: ")
    if to_choice not in units:
        print("Invalid unit!")
        return

    value = get_number("Enter value: ")

    from_name, from_factor = units[from_choice]
    to_name, to_factor = units[to_choice]

    liters = value * from_factor
    result = liters / to_factor

    display_result(value, from_name, result, to_name)


# ================================================================
#                       SPEED CONVERSION
# ================================================================

def speed_conversion():
    print("\n========== SPEED CONVERSION ==========")
    print("1. Meter/Second")
    print("2. Kilometer/Hour")
    print("3. Mile/Hour")
    print("4. Knot")
    print("5. Foot/Second")

    units = {
        "1": ("Meter/Second", 1),
        "2": ("Kilometer/Hour", 1000 / 3600),
        "3": ("Mile/Hour", 1609.344 / 3600),
        "4": ("Knot", 1852 / 3600),
        "5": ("Foot/Second", 0.3048)
    }

    from_choice = input("Enter source unit: ")
    if from_choice not in units:
        print("Invalid unit!")
        return

    to_choice = input("Enter target unit: ")
    if to_choice not in units:
        print("Invalid unit!")
        return

    value = get_number("Enter value: ")

    from_name, from_factor = units[from_choice]
    to_name, to_factor = units[to_choice]

    meters_per_second = value * from_factor
    result = meters_per_second / to_factor

    display_result(value, from_name, result, to_name)


# ================================================================
#                   DIGITAL STORAGE CONVERSION
# ================================================================

def storage_conversion():
    print("\n========== DIGITAL STORAGE CONVERSION ==========")
    print("1. Bit")
    print("2. Byte")
    print("3. Kilobyte")
    print("4. Megabyte")
    print("5. Gigabyte")
    print("6. Terabyte")

    units = {
        "1": ("Bit", 1),
        "2": ("Byte", 8),
        "3": ("Kilobyte", 8 * 1024),
        "4": ("Megabyte", 8 * 1024 ** 2),
        "5": ("Gigabyte", 8 * 1024 ** 3),
        "6": ("Terabyte", 8 * 1024 ** 4)
    }

    from_choice = input("Enter source unit: ")
    if from_choice not in units:
        print("Invalid unit!")
        return

    to_choice = input("Enter target unit: ")
    if to_choice not in units:
        print("Invalid unit!")
        return

    value = get_number("Enter value: ")

    from_name, from_factor = units[from_choice]
    to_name, to_factor = units[to_choice]

    bits = value * from_factor
    result = bits / to_factor

    display_result(value, from_name, result, to_name)


# ================================================================
#                       DATA RATE CONVERSION
# ================================================================

def data_rate_conversion():
    print("\n========== DATA RATE CONVERSION ==========")
    print("1. Bit/Second")
    print("2. Kilobit/Second")
    print("3. Megabit/Second")
    print("4. Gigabit/Second")
    print("5. Byte/Second")
    print("6. Kilobyte/Second")
    print("7. Megabyte/Second")

    units = {
        "1": ("Bit/Second", 1),
        "2": ("Kilobit/Second", 1000),
        "3": ("Megabit/Second", 1000000),
        "4": ("Gigabit/Second", 1000000000),
        "5": ("Byte/Second", 8),
        "6": ("Kilobyte/Second", 8000),
        "7": ("Megabyte/Second", 8000000)
    }

    from_choice = input("Enter source unit: ")
    if from_choice not in units:
        print("Invalid unit!")
        return

    to_choice = input("Enter target unit: ")
    if to_choice not in units:
        print("Invalid unit!")
        return

    value = get_number("Enter value: ")

    from_name, from_factor = units[from_choice]
    to_name, to_factor = units[to_choice]

    bits_per_second = value * from_factor
    result = bits_per_second / to_factor

    display_result(value, from_name, result, to_name)


# ================================================================
#                       PRESSURE CONVERSION
# ================================================================

def pressure_conversion():
    print("\n========== PRESSURE CONVERSION ==========")
    print("1. Pascal")
    print("2. Kilopascal")
    print("3. Bar")
    print("4. Atmosphere")
    print("5. PSI")
    print("6. Torr")

    units = {
        "1": ("Pascal", 1),
        "2": ("Kilopascal", 1000),
        "3": ("Bar", 100000),
        "4": ("Atmosphere", 101325),
        "5": ("PSI", 6894.757293),
        "6": ("Torr", 101325 / 760)
    }

    from_choice = input("Enter source unit: ")
    if from_choice not in units:
        print("Invalid unit!")
        return

    to_choice = input("Enter target unit: ")
    if to_choice not in units:
        print("Invalid unit!")
        return

    value = get_number("Enter value: ")

    from_name, from_factor = units[from_choice]
    to_name, to_factor = units[to_choice]

    pascals = value * from_factor
    result = pascals / to_factor

    display_result(value, from_name, result, to_name)


# ================================================================
#                       ENERGY CONVERSION
# ================================================================

def energy_conversion():
    print("\n========== ENERGY CONVERSION ==========")
    print("1. Joule")
    print("2. Kilojoule")
    print("3. Calorie")
    print("4. Kilocalorie")
    print("5. Watt Hour")
    print("6. Kilowatt Hour")

    units = {
        "1": ("Joule", 1),
        "2": ("Kilojoule", 1000),
        "3": ("Calorie", 4.184),
        "4": ("Kilocalorie", 4184),
        "5": ("Watt Hour", 3600),
        "6": ("Kilowatt Hour", 3600000)
    }

    from_choice = input("Enter source unit: ")
    if from_choice not in units:
        print("Invalid unit!")
        return

    to_choice = input("Enter target unit: ")
    if to_choice not in units:
        print("Invalid unit!")
        return

    value = get_number("Enter value: ")

    from_name, from_factor = units[from_choice]
    to_name, to_factor = units[to_choice]

    joules = value * from_factor
    result = joules / to_factor

    display_result(value, from_name, result, to_name)


# ================================================================
#                       ABOUT PROGRAM
# ================================================================

def about_program():
    print("\n" + "=" * 60)
    print("                 ABOUT THIS PROGRAM")
    print("=" * 60)
    print("Unit Conversion Application")
    print("Developed using Python")
    print("Designed for beginners and students.")
    print("This program demonstrates:")
    print("- Functions")
    print("- Dictionaries")
    print("- Loops")
    print("- Conditional statements")
    print("- Exception handling")
    print("- User input")
    print("- Mathematical calculations")
    print("=" * 60)


# ================================================================
#                       MAIN PROGRAM
# ================================================================

def main():
    # Display welcome message.
    print("\n" + "*" * 60)
    print("        WELCOME TO UNIT CONVERSION APPLICATION")
    print("*" * 60)

    # Main loop keeps the application running.
    while True:

        # Display the main menu.
        main_menu()

        # Ask user to select a category.
        choice = input("Enter your choice: ").strip()

        # Select conversion according to user's choice.
        if choice == "1":
            length_conversion()

        elif choice == "2":
            weight_conversion()

        elif choice == "3":
            temperature_conversion()

        elif choice == "4":
            time_conversion()

        elif choice == "5":
            area_conversion()

        elif choice == "6":
            volume_conversion()

        elif choice == "7":
            speed_conversion()

        elif choice == "8":
            storage_conversion()

        elif choice == "9":
            data_rate_conversion()

        elif choice == "10":
            pressure_conversion()

        elif choice == "11":
            energy_conversion()

        elif choice == "12":
            power_conversion()

        elif choice == "13":
            angle_conversion()

        elif choice == "0":
            print("\nThank you for using Unit Conversion Application!")
            print("Program ended successfully.")
            break

        else:
            print("\nInvalid choice!")
            print("Please select a number from 0 to 13.")

        # Ask whether the user wants another conversion.
        if choice != "0":
            print("\nConversion completed.")
            again = input("Press Enter to continue or type N to exit: ")

            if again.lower() == "n":
                print("\nThank you for using the application!")
                break


# ================================================================
#                       PROGRAM START
# ================================================================

if __name__ == "__main__":
    main()


# ================================================================
#                       END OF PROGRAM
# ================================================================