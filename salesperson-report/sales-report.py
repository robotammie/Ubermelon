"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

# Initialize empty lists to hold a) the list of salespeople and b) the number of melons
# Code could be made more user-friendly by creating a dictionare instead
salespeople = []
melons_sold = []


# opens the sales report file
f = open("sales-report.txt")

# iterates over the file, line by line (one sale at a time)
for line in f:
    line = line.rstrip()  # removes newline character from the end of the line
    entries = line.split("|")  # splits each line at the pipe delimeter

    # Pulls the salesperson name and number of melons sold from each transaction
    salesperson = entries[0]
    melons = int(entries[2])

    # Adds the melons sold in each transaction to the salesperson's total
    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
    else:  # Adds salesperson to list of salespeople, if not already there
        salespeople.append(salesperson)
        melons_sold.append(melons)

# Prints list of salespeople with thier melon sales totals
# Could be moved inside the for loop to save time
for i in range(len(salespeople)):
    print "{} sold {} melons".format(salespeople[i], melons_sold[i])
