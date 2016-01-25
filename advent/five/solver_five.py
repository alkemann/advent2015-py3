from five import is_nice, is_nice_improved


good_count = 0
very_good_count = 0
for s in open("data_five.txt", "r").readlines():
    if is_nice(s):
        good_count += 1
    if is_nice_improved(s):
        very_good_count += 1

print "*********************"
print " Good [%d]" % good_count
print " Very good [%d]" % very_good_count
print "*********************"