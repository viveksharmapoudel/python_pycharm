import  re

randStr = " F.B.I. I.R.S. CIA"

print("matches:",len(re.findall(".\..\..\.",randStr)))


randStr =''' this is a long string
 that goes on 
 for many lines'''


print(randStr)

regex=re.compile("\n")
randStr= regex.sub(" ", randStr)

print(randStr)