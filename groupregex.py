import re


bd = input("enter your birthday(m-d-y):")

bdRegex= re.search(r"(\d{1,2})-(\d{1,2})-(\d{4})",bd)

print("you were born on",bdRegex.group())
print("Birth month",bdRegex.group(1))
print("Birth Day",bdRegex.group(2))
print("Birth Year",bdRegex.group(3))
