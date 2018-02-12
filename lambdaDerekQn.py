

import random

numList=[]

for i in range(1,100):
    numList += [int(random.choice(range(1,1000)))]

print(numList)

print(list(filter(lambda x:x%9==0,numList)))