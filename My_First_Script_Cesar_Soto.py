# My First Script 😃
# Instructions:
# Create a script that takes the following data as input:
# First name
# Last name
# Age
# 
# Once the user enters the data, your script should output the user's full name and the year he/she was born.

from datetime import datetime  # import the datetime module

firstName = input("What's your first name?: ")
lastName = input("What's your last name?: ")
age = int(input("What's your age?: "))
currentYear = datetime.now().year
print(firstName, lastName, "you were born on", currentYear-age, "\n", sep=" ")
