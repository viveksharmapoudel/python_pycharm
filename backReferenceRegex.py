import re


randstr=" <a href='#'><b>The link</b></a>"

regex=re.compile(r"<b>(.*?)</b>")

randstr=re.sub(regex,r"\1",randstr)
print(randstr)

