import  re

string = "ape is in the apexxx"

regex = re.findall("ape.",string)

for i in regex:
    print(i)


phn ="977-9849-656199"

if re.search("\w{3}-\w{4}-\w{6}",phn):
    print("this is phone number")


if re.search("\w{2,20}","vivek sharma poudel"):
    print("valid name")

if re.search("\w{2,20}\s\w{2,20}","tsohio makamuto"):
    print("valid name+ surname")