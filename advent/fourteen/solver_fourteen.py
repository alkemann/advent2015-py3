from SolutionFourteen import SolutionFourteen
from Reindeer import Reindeer


solver = SolutionFourteen()
descriptions = open("input_fourteen.txt", "r").readlines()

deers = []
for d in descriptions:
    deers.append(Reindeer(d))

solver.run_deers(deers, 2503)

distance_winner = solver.which_deer_traveled_furthest(deers)
print "*********************"
print " %s traveled %d kms and got the farthest " % (distance_winner.name, distance_winner.distance)
print "  %s" % distance_winner
print "*********************"

winner = solver.whch_deer_scored_most(deers)
print "*********************"
print " Winner is %s!" % winner.name
print "  %s" % winner
print " %s traveled %d kms " % (winner.name, winner.distance)
print " and got %d points" % winner.score
print "*********************"
