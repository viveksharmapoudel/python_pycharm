import re
randstr= "@ Get this string"

regex= re.compile(r"[^@\s].*$")
matches= re.findall(regex,randstr)

print(len(matches))

for i in matches:
    print(i)


#########example another one 
randstr="412-555-1212 412-555-1213 412-555-1214"
regex=re.compile(r"412-(.{8})")
matches=re.findall(regex,randstr)


for i in matches:
    print(i)
