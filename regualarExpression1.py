import re

#first search example of regular expression 
if re.search("ape", "all apes are in apex"):
    print("yes there is")

#. after the pattern will display the whole word else only the pattern will be displayed
allApes= re.findall("ape.","all ape are in apex")

for str in allApes:
    print(str)

theStr= "the ape at the apex"

print("find the pattern and return to location and string also ")
for i in re.finditer("ape.", theStr):
    locTuple= i.span()
    print(locTuple)
    print(theStr[locTuple[0]:locTuple[1]])


