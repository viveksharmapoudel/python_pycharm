import re


#(?! expression): negative look ahead
#(?<! expression): negative look behind


randstr= "8 apples $3, 1 Bread $1, 1 Cereal $4"


regex = re.compile(r"(?<!\$)\d+")
matches=re.findall(regex,randstr)

print(len(matches))

matches=[int(i) for i in matches]

from  functools import reduce

print("total Items{}".format(reduce(lambda x,y:x+y , matches)))