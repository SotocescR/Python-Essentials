# Check Triangle Type 📐
# Instructions:
# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Ask the user for the measures of each side.
# Note:
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
# Example Expected Output:
# Input lengths of the triangle sides:                                    
# x: 6                                                                    
# y: 8                                                                    
# z: 12                                                                   
# Result: Scalene triangle  

print("\n======================================\nCheck Triangle Type 📐\n======================================\n")

print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("Result: Equilateral triangle\n")

elif x == y != z or x != y == z or x == z != y:
    print("Result: Isosceles triangle\n")

else:
    print("Result: Scalene triangle\n")