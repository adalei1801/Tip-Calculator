#  Ashley King

# This line asks the total bill
bill = input("How much is the bill? $ ")

# This line asks what percentage you would like to tip.
tipcent = input("How much would you like to tip? (in percentage) ")

# This divides the percentage the user put in by 100 to convert it into a float and stores it in a variable.
tipquo = int(tipcent) / 100

# This code multiples the quotient from the last line by the  bill in order to get  the dollar amount the person wants to tip and stores the answer.
tipam = tipquo * int(bill)

# This adds the product from last line to the bill to get the total amount the person wants to tip and store the answer.
fintotal = int(tipam) + int(bill)

# Tells person the final total
print("Your total is $ ", fintotal)

# Asks how many ways the  bill should be split and stores  answer.
peeps = input("How many people does the bill need to be split between? ")

# Divides final bill by amount of people splitting the bill and stores the answer.
split = int(fintotal)/int(peeps)

# Tells person how much each person should pay.
print("Each person should pay $ ", split)
