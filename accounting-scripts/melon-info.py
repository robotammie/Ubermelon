"""
Prints out all the melons in our inventory
"""

from melons import all_melons


def print_melon(melons):
    """Print the name and attributes of melons on offer at Ubermelon"""

    for name in melons:

        seeds = "have"
        if melons[name]["seedless"]:
            seeds = "do not have"

        price = melons[name]["price"]

        print "{}s {} seeds and are ${:.2f}".format(name, seeds, price)


def add_attribute(attribute):
    """Inable seamless addition of new attributes to our master melon list"""

    print "Please enter new data for each melon:"

    for melon in all_melons:
        new_fact = raw_input("{}: ".format(melon))

        all_melons[melon][attribute] = new_fact
