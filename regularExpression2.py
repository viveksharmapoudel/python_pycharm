import re


animalStr="Cat rattt mat pat"

allAnimals= re.findall("[crmfp]at",animalStr)
print(allAnimals)