"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""
# Creating empty lists to append all the data to from sales-report.txt
salespeople = []
melons_sold = []

# Open data file & bind contents to variable "f" (not a great variable name)
f = open("sales-report.txt")
# Loop over each line, remove line breaks, split on |, and bind resulting
# list to the variable name "entries"
for line in f:
    line = line.rstrip()
    entries = line.split("|")
    # Assigns index[0] of entries to variable "salesperson"
    # Assigns index[2] of entries to variable "melons", and typecasts to int
    salesperson = entries[0]
    melons = int(entries[2])

    # Check if "salesperson" variable is in list "salespeople"
    # If it is, get the index in the list where "salesperson" is located
    # and increment the matching index in "melons_sold"
    # by the value of "melons"
    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
    # If "salesperson" is NOT in "salespeople", append the value of
    # "salesperson" to the end of the "salespeople" list, and correspondingly
    # append the matching "melons" value to the end of the "melons_sold" list
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# Looping through the range of the length of the "salespeople" list, print
# a string with .format method, populating the blanks with the matching indices
# of the "salespeople" and "melons_sold" lists. This code is a dumb.
for i in range(len(salespeople)):
    print "{} sold {} melons".format(salespeople[i], melons_sold[i])
