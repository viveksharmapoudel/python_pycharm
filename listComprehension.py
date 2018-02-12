import random


print([x*y for x in range(2,6) for y in range(12,16) if x*y%8 ==0])

    ##breaking a list comprehension first expression would give return type , second would give iteration third would give condition




print([x for x in [ i*2 for i in range(10)] if x%8==0])

##list comprehension inside list comprehension firstly one list is generated and then multiplied by 2 afterthat multiple of 8 is printed


print([x for x in [random.randint(1,1001) for i in range(50)] if x%9==0])