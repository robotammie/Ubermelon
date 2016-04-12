def print_report(day, file_name):
    print "Day %d" % (day)
    the_file = open(file_name)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print "Delivered {0} {1}s for total of ${2}".format(count, melon, amount)
    the_file.close()

print_report(1, "um-deliveries-20140519.txt")
print_report(2, "um-deliveries-20140520.txt")
print_report(3, "um-deliveries-20140521.txt")
