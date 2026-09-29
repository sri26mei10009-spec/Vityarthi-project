from program.menu import menu
from program.validators import get_valid_units
from program.calculator import calculate_bill

def main():
    print("\n" + "="*35)
    print("    ELECTRICITY BILL CALCULATOR")
    print("="*35)
    while True:
        choice = menu()
        
        if choice == '1':
            units = get_valid_units()
            # Only proceed to calculate if a valid number was returned
            if units is not None:
                total, breakdown = calculate_bill(units)
                print("\n--- Bill Summary ---")
                print(f"Cost breakdown per slab: {breakdown}")
                print(f"Total Electricity Bill: Rs {total}")
                
        elif choice == '2':
            print("\nExiting the program. Thank you for using the calculator!")
            break
            
        else:
            print("\nInvalid choice! Please enter '1' to calculate or '2' to exit.")

if __name__ == "__main__":
    main()
