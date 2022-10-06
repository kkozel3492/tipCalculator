# Todays application will work as a tip calculator, it will take the total
# bill amount, figure out the tip percentage, and split it amongst serveral diners.

# Print Message to user
print("Welcome to the tip calculator!")

# Find and assign total bill to float variable
totalBill = input("What was the total bill?\n")
totalBill = float(totalBill)
# Ask the user what percentage they would like to leave
userTip = input("What percentage tip would you like to leave?\n")
# Change the user input into a percentage
userTip = float(userTip) / 100
# Find how many people will be splitting the tab
splitCheck = input("How many people will be splitting the tab?\n")
splitCheck = float(splitCheck)
# Perform calculation to find total cost of bill divided by how many people are paying
billWithTip = totalBill + totalBill * userTip
eachPays = billWithTip / splitCheck
eachPays = round(eachPays,2)
# Print out results
print(f"Each person should pay: ${eachPays}")