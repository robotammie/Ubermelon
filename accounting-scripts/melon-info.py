"""
Prints out all the melons in our inventory
"""

from melons import all_melons


def print_melon(melons):
    """Print the name and attributes of melons on offer at Ubermelon"""

    for name in melons:

        print "{}:".format(name)
        print "Price: {}".format(melons[name]["price"])
        print "Seedless?: {}".format(melons[name]["seedless"])
        print "Rind Color: {}".format(melons[name]["rind color"])
        print "Flesh Color: {}".format(melons[name]["flesh color"])
        print "Weight: {} lbs\n".format(melons[name]["weight"])


def add_attribute(attribute):
    """Inable seamless addition of new attributes to our master melon list"""

    print "Please enter new data for each melon:"

    for melon in all_melons:
        new_fact = raw_input("{}: ".format(melon))

        all_melons[melon][attribute] = new_fact
