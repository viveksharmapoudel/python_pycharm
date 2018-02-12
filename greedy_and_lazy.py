import re

randStr= "<name>life on Mars</name><name>Freaks and Geeks</name>"

regex= re.compile("<name>.*?</name>")

matches=re.findall(regex,randStr)

for i in matches:
    print(i)

print("*****************see the importance of () ***************")

randStr= "<name>life on Mars</name><name>Freaks and Geeks</name>"

regex= re.compile("<name>(.*?)</name>")

matches=re.findall(regex,randStr)

for i in matches:
    print(i)


print("*****************see the importance of + ***************")

randStr= "<name>life on Mars</name><name>Freaks and Geeks</name>"

regex= re.compile("<name>(.+?)</name>")

matches=re.findall(regex,randStr)

for i in matches:
    print(i)