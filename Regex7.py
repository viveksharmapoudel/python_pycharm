import re


randStr1= " cat cats "

regex = re.compile("[cat]+s?")
match= re.findall(regex,randStr1)

for i in match:
    print(i)


randStr2= "doctor doctors doctor's"

regex=re.compile("[doctor]+['s]*")
match=re.findall(regex,randStr2)
for i in match:
    print(i)