import re
match= re.search(r"\d{2}","The chcken weight 13 lbs")
print("Match:",match.group())
print("span:",match.span())
print("Start index:",match.start())
print("end index:",match.end())

