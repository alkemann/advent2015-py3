import hashlib


# Santa needs help mining some AdventCoins (very similar to bitcoins)
# to use as gifts for all the economically forward-thinking little girls and boys.
#
# To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes.
# The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a
# number in decimal. To mine AdventCoins, you must find Santa the lowest positive number
# (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
def mine(key, zeros=5):
    i = 0
    while True:
        i += 1
        m = hashlib.md5()
        m.update("%s%d" % (key, i))
        md5 = m.hexdigest()
        if md5[:zeros] == "0" * zeros:
            return i

        # Backup to stop it from goign endlessly
        if i > 10000000:
            raise Exception("Too many tries")

