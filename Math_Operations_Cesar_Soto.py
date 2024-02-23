# Math Operations #️⃣
# Instructions:
#
# Create a script that will request 2 numbers and output the results of the addition, subtraction, multiplication and division of both numbers.
# Keep in mind that the user may enter a number like 0 and you cannot divide by 0, so show a message to the user asking them not to enter a 0 as the second number.
# The output should look like this:
# num1 + num2 = addition
# num1 - num2 = subtraction
# num1 * num2 = multiplication
# num1 / num2 = division
#

num1 = int(input("Type a number: "))
num2 = int(input("Type the second number: "))

while num2 == 0:
    num2 = int(input("Type a number that is not 0: "))
    
print(f"\n{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")

# longer option:
# 
# addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2
# 
# print(f"\n{num1} + {num2} = {addition}")
# print(f"{num1} - {num2} = {subtraction}")
# print(f"{num1} * {num2} = {multiplication}")
# print(f"{num1} / {num2} = {division}")