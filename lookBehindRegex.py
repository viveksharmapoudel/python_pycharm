import re

randstr="1. bread 2. apples 3. juice"

regex= re.compile(r"(?<=\d.\s)\w+")

matches=re.findall(regex,randstr)

for i in matches:
    print(i)

    #### look ahead + look behind in the same code example

#just looking 
randstr ="<h1>I'm Important</h1> <h1>so am i</h1>"

regex= re.compile(r"(?<=<h1>).+?(?=</h1>)")
matches =re.findall(regex,randstr)

for i in matches:
    print(i)