# Vowel or Consonant Script 🔡
# Instructions:
# Write a Python program to check whether a letter is a vowel or consonant and print the result.
# The letter will be obtained as a user input.
# If the user enters something other than a letter output a warning message.
print("\n======================================\nVowel or Consonant Script 🔡\n======================================\n")
letter = input("Please type a letter: ").lower()
letter = letter[0]

if letter.isalpha():
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        print("The letter is a vowel")
    else:
        print("The letter is a consonant")
else:
        print("A warning message!")