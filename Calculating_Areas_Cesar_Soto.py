# Create a script that performs the following operations:
#
#   Take the radius and output the area of the circle.
#   Take the side of a square and output the area of the square.
#   Take the base and height of a triangle and output the area of the triangle.
#   Take the radius of a sphere and output the volume of the sphere.
#   The measures should be taken from the user each time.

import math

while True:  # This will create an infinite loop
    
    #Main Menu
    print("\n", 
    "======================================",
    "---*** WELCOME TO THE MATH TOOL***---",
    "==============MAIN MENU===============",
    "1. Calculate the area of a circle.", 
    "2. Calculate the area of a square.", 
    "3. Calculate the area of a triangle.", 
    "4. Calculate the volume of a sphere.", 
    "e. Exit", 
    "==============MAIN MENU===============", 
        sep="\n")

    #Main Menu input
    option = input("\nEnter the number for the option you wish to use:")

    if option == '1':
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius * radius
        print("The area of the circle is: ", area)
    
    elif option == '2':
        side = float(input("Enter the side of the square: "))
        area = side * side
        print("The area of the square is: ", area)
    
    elif option == '3':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print("The area of the triangle is: ", area)
    
    elif option == '4':
        radius = float(input("Enter the radius of the sphere: "))
        volume = 4/3 * math.pi * radius * radius * radius
        print("The volume of the sphere is: ", volume)
    
    elif option.lower() == 'e':
        print("Exiting...")
        break  # This will break the loop and end the program

    else:
        print("Invalid option. Please enter a number from 1 to 4 or 'e' to exit.")
      
        
    