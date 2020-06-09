#importing re module

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

