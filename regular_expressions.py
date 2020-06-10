"""
    importing re module
"""

import re

pattern = r"eggs"
# re.match
if re.match(pattern, "eggseggseggs"):
    print("Match found")
else:
    print("Match not found")

# re.search
if re.search(pattern, "eggs"):
    print("Search found")
else:
    print("Search not found")

# re.findall
print(re.findall(pattern, "baconeggseggsbacon"))

"""
    implementing sub module from RE module
"""

import re

mystring = "My name is John and my mother named me John because John Floyd was her favourite singer"

pattern = r"John"     # 'r' means raw, pattern should be a raw format and should be stored in a variable

variable = re.sub(pattern, "Shiyan", mystring)

print(variable)


"""
    re.match
"""

lmao = r"lo.....h"
if re.match(lmao, "logitech"):
    print("TRUE")