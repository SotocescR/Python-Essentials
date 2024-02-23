# Basic Login Script 🔐
# Instructions:
# Create a login prompt that will request username and password.
# Define a username and password variables to compare with the user input.
# Script should verify if they are correct and output a success message.
# The user should receive an error message telling them which one is wrong if the login is incorrect.

import getpass

print(
    "=================================",
    "---**Basic Login Script 🔐**---",
    "=================================",
    "*default credentials: user/password",
    sep="\n")

# Create a login prompt that will request username and password.
username = input("Username: ")
password = getpass.getpass("Password: ")

# Define a username and password variables to compare with the user input.
defaultUsername ="user"
defaultPassword = "password"

# Script should verify if they are correct and output a success message.
# The user should receive an error message telling them which one is wrong if the login is incorrect.
if username == defaultUsername and password == defaultPassword:
    print(f"Welcome, {username}!")
elif username != defaultUsername and password != defaultPassword:
    print("Wrong username and password!")
elif username != defaultUsername:
    print("Wrong username!")
else:
    print("Wrong password!")
