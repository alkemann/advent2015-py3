from seven import Seven


solver = Seven(open("data_seven.txt", "r").readlines())

print "*********************"
print ""
print "The output of a is [%d]" % solver.check("a")
print ""
# print "*********************"
# print ""
# print "You need [%d] feet of ribbon" % how_much_ribbon_in_bag(bag)
# print ""
print "*********************"
