from advent.eight.eight import total, total_encoded


strings = open("data_eight.txt", "r").readlines()
total = total(strings)
encoded = total_encoded(strings)

print("*********************")
print(" Difference between code and content [%d]" % total)
print(" Difference between code and encoded [%d]" % encoded)
print("*********************")
