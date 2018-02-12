import re

#1 to 20 lowecase and uppercase letter, numbers,plus ._%+-
#2. as @ symbol
#3. 2 to 20 lowercase and uppercase letter, numbers, plus .-
#4. A period
#5. 2to 3 lowercase and uppercase letters

emailList = "db@aol.com me@.com @apple.com db@.com eat@email.com"

print("email Matches:", len(re.findall("[\w.%+-]{1,20}@[\w.-]{2,20}\.[A-Za-z]{2,3}"
                                       ,emailList)))