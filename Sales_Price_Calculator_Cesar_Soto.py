# Sales Price Calculator 🧮
# Instructions:
# The script will calculate the final sales price of any item based on the following features:
# 
# Ask for the individual price of the item.
# Ask for the amount of items to be purchased.
# Calculate sales tax (I.V.A) 13% and assign it to a variable.
# Calculate a 10% discount on the total amount of the purchase and assign it to a variable.
# The unit price, price of all items, sales tax, discounted amount  and final price must all be displayed to the end user.
# Note: The tax and discount will be calculated in the order that appears in the instructions.
# 
print("=========================\nSales Price Calculator 🧮\n=========================")
itemPrice = float(input("Price of the item: "))
itemAmount = float(input("Amount of items to be purchased: "))
# 
salesTax = itemPrice * itemAmount * 0.13
discount = (( itemPrice * itemAmount ) + salesTax ) * 0.1
#
print("===============================",
      "\nI.V.A 13%:", salesTax,
      "\n10% discount:", discount,
      "\n===============================",
      "\nFinal Price:", (( itemPrice * itemAmount ) + salesTax ) - discount,
      "\n===============================",
     sep=" ")
