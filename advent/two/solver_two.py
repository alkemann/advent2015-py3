from two import how_much_paper_in_bag, how_much_ribbon_in_bag


bag = open("two_input.txt", "r").readlines()
print "*********************"
print ""
print "You need [%d] feet of paper" % how_much_paper_in_bag(bag)
print ""
print "*********************"
print ""
print "You need [%d] feet of ribbon" % how_much_ribbon_in_bag(bag)
print ""
print "*********************"
