import random

fliplist=[]

for i in range(1,1000):
    fliplist+= random.choice(['H','T'])

#output of the result:
print("number of heads", fliplist.count("H"))
print("number of tails",fliplist.count("T"))
