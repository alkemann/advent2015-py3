from advent.eight.eight import total


total, encoded = total(open("data_eight.txt", "r").readlines())

print("*********************")
print(" Difference between code and content [%d]" % total)
print(" Difference between code and encoded [%d]" % encoded)
print("*********************")
