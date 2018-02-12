import re

#(?=expression)

randstr="one two three four"

regex=re.compile(r"\w+")
matches=re.findall(regex,randstr)
for i in matches:
    print(i)


