# Net Salary Calculator 🧮
# Instructions:
# Create a script that will ask the user to their enter name and salary and will perform the following calculation:
#
# Calculate the 10.6% fee for CCSS and store it in a variable.
# Calculate the 1.5% fee for Banco Popular and store it in a variable.
# Calculate the net salary and store it in a variable.
# Output all the information, each amount should have a description of what it represents.
# NOTE: A percentage can be represented in Python as: percentage / 100. This way 10.6% would be represented as 0.106
#
print("======================================\nWelcome to the Net Salary Calculator\n======================================")
userName = input("What's your name?: ")
userSalary = int(input("What's your salary?: "))
#
ccss = userSalary * 0.106
bancoPopular = userSalary * 0.015
netSalary = userSalary - (ccss + bancoPopular)
#
print("===============================",
      "\nNombre:", userName,
      "\nSalario bruto:", userSalary,
      "\n===============================",
      "\nCCSS fee: ", ccss,
      "\nBanco Popular fee: ", bancoPopular,
      "\n===============================",
      "\nNet Salary: ", netSalary,
      "\n===============================",
     sep=" ")

