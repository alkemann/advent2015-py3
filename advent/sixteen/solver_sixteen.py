from sixteen import who_is_sue, Sue, who_is_she_really


sues = []
lines = open("data_sixteen.txt", "r").readlines()
for description in lines:
    sues.append(Sue(description))

print "********************************"
print " Sue is [%d]" % who_is_sue(sues)
print "********************************"
print " Real Sue is one of"
potential = who_is_she_really(sues)
for sue in potential:
    print sue
print "********************************"