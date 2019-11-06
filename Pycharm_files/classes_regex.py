phoneRegex = re.compile(r'(\d{3})\.?-?(\d{3}\.?-?\d{4})')  # Regex for phone number
emailRegex = re.compile(r'\w+@\w+\.\w{2,}')


'''Character classes:'''


# Shorthand character class
#
# Represents
#
# \d...............................Any numeric digit from 0 to 9.
#
# \D...............................Any character that is not a numeric digit from 0 to 9.
#
# \w...............................Any letter, numeric digit, or the underscore character.
#                                  (Think of this as matching “word” characters.)
#
# \W...............................Any character that is not a letter, numeric digit, or the underscore character.
#
# \s...............................Any space, tab, or newline character. (Think of this as matching “space” characters.)
#
# \S...............................Any character that is not a space, tab, or newline.

'''###################################################################################################
REGEX SYMBOLS'''

# The ? matches zero or one of the preceding group.
#
# The * matches zero or more of the preceding group.
#
# The + matches one or more of the preceding group.
#
# The {n} matches exactly n of the preceding group.
#
# The {n,} matches n or more of the preceding group.
#
# The {,m} matches 0 to m of the preceding group.
#
# The {n,m} matches at least n and at most m of the preceding group.
#
# {n,m}? or *? or +? performs a nongreedy match of the preceding group.
#
# ^spam means the string must begin with spam.
#
# spam$ means the string must end with spam.
#
# The . matches any character, except newline characters.
#
# \d, \w, and \s match a digit, word, or space character, respectively.
#
# \D, \W, and \S match anything except a digit, word, or space character, respectively.
#
# [abc] matches any character between the brackets (such as a, b, or c).
#
# [^abc] matches any character that isn’t between the brackets.