"""Shipping procedures for Ubermelon."""

import robots
import sys

GOURD_LIMIT = 200


class AbstractGourd(object):
    """Superclass for melons and squash"""

    def __init__(self, gourd_type):
        """Initialize gourd.

        gourd_type: type of gourd being built.
        """

        self.gourd_type = gourd_type
        self.weight = 0.0
        self.color = None
        self.stickers = []

    def prep(self):
        """Prepare the gourd."""

        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)

    def __str__(self):
        """Print out information about gourd."""

        if self.weight <= 0:
            return self.gourd_type
        else:
            return "{} {:.2f} lbs {}".format(self.color,
                                             self.weight,
                                             self.gourd_type)


class Melon(AbstractGourd):
    """Melon."""

    pass


class Squash(AbstractGourd):
    """squash."""

    pass


def show_help():

    print """
shipping_procedure.py
  Master Control Program for Automated Melon Order Fullfillment

This program processes order from an order log file and controls the
robots used to fulfill the orders.

Usage:

    python shipping_procedure.py [logfile]

Where:

    [logfile]
        The name of the log file you would like to process.
        Hint: There are two files included in this project folder.
"""


def main():
    """Assesses and packs order objects.

    Distinguishes between melons/squashes."""

    # Check to make sure we've been passed an argument on the
    # command line.  If not, display instructions.

    if len(sys.argv) < 2:
        show_help()
        sys.exit()

    # Get the name of the log file to open from the command line
    logfilename = sys.argv[1]

    # Open the log file
    f = open(logfilename)

    # Read each line from the log file and process it

    for line in f:

        # Each line should be in the format:
        # <gourd name>: <quantity>
        gourd_type, quantity = line.rstrip().split(':')
        quantity = int(quantity)

        print "\n-----"
        print "Fullfilling order of {} {}".format(quantity, gourd_type)
        print "-----\n"

        count = 0
        gourds = []

        # Pick gourds until we reach the requested quantity

        while len(gourds) < quantity:

            # Make sure we haven't reached our limit for the total
            # number of gourds we're allowed to pick

            if count > GOURD_LIMIT:
                print "\n------------------------------"
                print "ALL MELONS HAVE BEEN PICKED"
                print "ORDERS FAILED TO BE FULFILLED!"
                print "------------------------------\n"
                sys.exit()

            # Have the robot pick a 'gourd' -- check to
            # see if it is a Winter Squash or not.

            if gourd_type != "Winter Squash":
                m = Melon(gourd_type)
                color = "Green"

            else:
                m = Squash(gourd_type)
                color = "Yellow"

            robots.pickerbot.pick(m)
            count += 1

            # Prepare the gourd
            m.prep()

            # Evaluate the gourd

            presentable = robots.inspectorbot.evaluate(m, color)

            if presentable:
                gourds.append(m)

            else:
                robots.trashbot.trash(m)
                continue

        print "------"
        print "Robots Picked {} {} for order of {}".format(count, gourd_type, quantity)

        # Pack the gourds for shipping
        boxes = robots.packerbot.pack(gourds)

        # Ship the boxes
        robots.shipperbot.ship(boxes)

        print "------\n"


main()
