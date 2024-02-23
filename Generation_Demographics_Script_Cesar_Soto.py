# Generation Demographics Script 👶👨👴
# Instructions: 
# Create a script that takes the following data as input:
# First name.
# Last name.
# Age.
# Once the user enters the data, your script should output the user's full name and the year he/she was born.
# In addition, depending on the year of birth the script should also print the corresponding Generation Demographic:
# If the person was born between 1940 and 1965: Baby Boomer.
# From 1966 to 1980: Generation X.
# From 1981 to 1996: Millenials.
# From 1997 to 2012: Generation Z.
# 2013 or after: Too young!
#from datetime import datetime  # import the datetime module
#
print("\n======================================\nGeneration Demographics Script 👶👨👴\n======================================\n")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
current_year = 2024
year_of_birth = current_year - age

print(f"Full Name: {first_name} {last_name}")
print(f"Year of Birth: {year_of_birth}")

if year_of_birth in range(1940, 1966):
    print("Generation: Baby Boomer")
elif year_of_birth in range(1966, 1981):
    print("Generation: Generation X")
elif year_of_birth in range(1981, 1997):
    print("Generation: Millenials")
elif year_of_birth in range(1997, 2013):
    print("Generation: Generation Z")
else:
    print("Generation: Too young!")

##########################################################
#currentYear = datetime.now().year
#firstName = input("What's your first name?: ")
#lastName = input("What's your last name?: ")
#age = int(input("What's your age?: "))
#
##user's full name and the year he/she was born
#print(f"{firstName} {lastName} was born on {currentYear-age}")
#
##Generation Demographic:
#if currentYear-age >= 1940 and currentYear-age <= 1965:
#    print("Generation Demographic: Baby Boomer")
#elif currentYear-age >= 1966 and currentYear-age <= 1980:
#    print("Generation Demographic: Generation X")
#elif currentYear-age >= 1981 and currentYear-age <= 1996:
#    print("Generation Demographic: Millenials")
#elif currentYear-age >= 1997 and currentYear-age <= 2012:
#    print("Generation Demographic: Generation Z")
#elif currentYear-age >= 2013 and currentYear-age <= currentYear:
#    print("Generation Demographic: Too young!")
#else:
#    print("Generation Demographic: Mummy")
##########################################################