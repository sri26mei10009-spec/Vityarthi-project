def display_menu():
    """Displays the interactive menu and captures user choice."""
    print("\n" + "="*35)
    print("    ELECTRICITY BILL CALCULATOR")
    print("="*35)
    print("1. Enter to calculate bill")
    print("2. Exit")
    
    choice = input("Enter your choice (1 or 2): ")
    return choice
