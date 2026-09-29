def get_valid_units():
    try:
        units = float(input("\nEnter the number of units consumed: "))
        if units < 0:
            print("Error: Units cannot be negative. Please try again.")
            return None
        return units
    except ValueError:
        print("Error: Invalid input! Please enter a valid numerical value.")
        return None
