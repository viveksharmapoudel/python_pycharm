import re


location = '''I used to eb a  quiet person.

But now a days I am not so quiet. 

However, I would love to see quiet me to talkative me.'''



regex= re.compile("quiet")

location= print(regex.sub("quite", location))



print(type(location))