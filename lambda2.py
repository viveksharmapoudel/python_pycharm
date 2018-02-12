shivaRandiHo= lambda x,y:x+y

print("sum is:",shivaRandiHo(4,5))

shivaChikni = lambda  age: True if age>=18 else False
print("shiva is 24 years old and he is {} to vote".format(shivaChikni(24)))

shivaLado =[lambda x: x**2,
            lambda x: x**3,
            lambda x: x**4]

for function in shivaLado:
    print(function(4))