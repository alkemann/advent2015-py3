

# A nice string is one with all of the following properties:
#     It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#     It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd)
#     It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
def is_nice(s=""):
    if "ab" in s or "cd" in s or "pq" in s or "xy" in s:
        return False

    vowel_count = 0
    contains_double = False
    previous_character = ' '
    for char in s:
        if char in "aeiou":
            vowel_count += 1
        if char == previous_character:
            contains_double = True
        else:
            previous_character = char

    return contains_double and vowel_count >= 3


# Now, a nice string is one with all of the following properties:
#
# It contains a pair of any two letters that appears at least twice in the string without overlapping,
#   like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them,
#   like xyx, abcdefeghi (efe), or even aaa.
def is_nice_improved(s=""):
    has_the_gapped_combo = False
    has_the_double_string = False
    for i in range(0, len(s)):
        if s[i:i+2] in s[i+2:]:
            has_the_double_string = True
        if i >= 2 and s[i] == s[i-2]:
            has_the_gapped_combo = True

    return has_the_gapped_combo and has_the_double_string