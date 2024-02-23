# Distance Converter Script 📏
# Instructions:
# Create a script that asks the user if he wants to convert inch -> cm or cm -> inch.
# The script should convert from inch -> cm or cm -> inch depending on the user's request.
# The user will input the distance to convert.
# Note: There are 2.54 cm in 1 inch and 0.39 inches in 1 cm

while True:  # This will create an infinite loop
    
    #Main Menu
    print(
        "======================================",
        "---**Distance Converter Script 📏**---",
        "==============MAIN MENU===============",
        "1. Convert inch -> cm", 
        "2. Convert cm -> inch.", 
        "e. Exit", 
        "==============MAIN MENU===============", 
        sep="\n")

    #Main Menu input
    option = input("\nEnter the number for the option you wish to use:")

    if option == '1':
        distance = float(input("Enter distance in inches: "))
        print(f"{distance} inches is equal to {distance*2.54} cm\n")
    
    elif option == '2':
        distance = float(input("Enter distance in centimeters: "))
        print(f"{distance} cm is equal to {distance*0.39} inches\n")
    
    elif option.lower() == 'e':
        print("Exiting...")
        break  # This will break the loop and end the program

    else:
        print("Invalid option. Please enter a number from 1 to 2 or 'e' to exit.")