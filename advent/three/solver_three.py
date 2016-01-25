from three import *


route = open("data_three.txt", "r").read()
print "********************************"
print " Santa visited [%d]" % how_many_houses(route)
print "********************************"
print " Santa and robot visited [%d]" % how_many_houses_with_robot(route)
print "********************************"