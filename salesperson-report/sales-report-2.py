"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

# Initialize empty dictionary to hold data
sales = {}


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
    sales[salesperson] = sales.get(salesperson, 0)

    sales[salesperson] += melons

    # Faster, but prints sales stats out unordered
    #print "{} sold {} melons".format(salesperson, sales[salesperson])

sales = sorted(sales.items())

# Prints sales alphabetically by salesperson first name
for sale in sales:
    print "{} sold {} melons".format(sale[0], sale[1])
