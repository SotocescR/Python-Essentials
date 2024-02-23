# Pair/Odd Script 🔢
# Instructions: 
# Create a script that checks if a number is pair or odd.
# 
# Ask the user to input a number.
# Check if the number is positive or negative
# If it is positive, output pair if the number is pair and odd if the number is odd.
# If it is negative, output a message saying that the number is negative.
print("\n======================================\nPair/Odd Script 🔢\n======================================\n")
num = int(input("Please type a number: "))
if num > 0:
    if num % 2 == 0:
        print("The number is pair")
    else:
        print("The number is odd")
else:
    print("The number is negative")