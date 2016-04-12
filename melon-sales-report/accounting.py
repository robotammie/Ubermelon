SALESPERSON_INDEX = 0
INTERNET_INDEX = 1
DORKY_LINE_LENGTH = 80

def section_break():
    """prints a line of '*' to denote section breaks"""

    print '*' * 60
    return




section_break()

orders_by_type = open("orders-by-type.txt")
melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}

for line in orders_by_type:
    data = line.split("|")
    melon_type = data[1]
    melon_count = int(data[2])
    melon_tallies[melon_type] += melon_count

orders_by_type.close()

melon_prices = {"Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00}

total_revenue = 0

for melon_type in melon_tallies:
    price = melon_prices[melon_type]
    revenue = price * melon_tallies[melon_type]
    total_revenue += revenue
    print "We sold {:,} {} melons at ${:,.2f} each for a total of ${:,.2f}".format(melon_tallies[melon_type], melon_type, price, revenue)

section_break()

orders_with_sales = open("orders-with-sales.txt")

sales = [0, 0]

for line in orders_with_sales:
    d = line.split("|")
    if d[1] == "0":
        sales[0] += float(d[3])
    else:
        sales[1] += float(d[3])

print "Salespeople generated ${:,.2f} in revenue.".format(sales[1])

print "Internet sales generated ${:,.2f} in revenue.".format(sales[0])

if sales[1] > sales[0]:
    print "Guess there's some value to those salespeople after all."
else:
    print "Time to fire the sales team! Online sales rule all!"

section_break()
