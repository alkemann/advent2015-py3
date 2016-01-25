from one import *


plan = open("one_input.txt", "r").read()
print "*********************"
print "You are now on floor [%d]" % ends_on_floor(plan)
print "*********************"
print "You took [%d] steps to reach the basement" % enters_basement_after_how_many_steps(plan)
print "*********************"
