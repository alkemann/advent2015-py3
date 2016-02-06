from seven import Seven


solver = Seven(open("data_seven.txt", "r").readlines())

print "*********************"
print ""
print "The output of a is [%d]" % solver.check("a")
print ""
print "*********************"
