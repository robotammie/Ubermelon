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

print_melon(all_melons)









# def print_melon(name, seedless, price):
#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print "{}s {} seeds and are ${:.2f}".format(name, have_or_have_not, price)


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
